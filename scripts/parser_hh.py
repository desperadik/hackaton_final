""" MSD - модуль сбора данных"""
import datetime
import random
from urllib.parse import urlencode, quote_plus

import re
import requests
from vacancy.models import Vacancy, Category, Employer
import time
from bs4 import BeautifulSoup as bs

#маскируемся под юзера
headers1 = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
headers2 = {'accept' : '*/*',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

#стандартная страница для парсера
base_url = 'https://hh.ru/search/vacancy'

def get_pages_from_query(query_url, session):
    page_urls = []

    request = session.get(query_url, headers = headers1)

    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        # получаем кол-во страниц на сайте для парсинга нескольких страниц
        try:
            pagination = soup.find_all('a', attrs={'data-qa': 'pager-page'})
            count_pages = int(pagination[-1].text)
            for i in range(count_pages):
            # for i in range(1):
                page_url ='{}&page={}'.format(query_url, i)
                page_urls.append(page_url)
        except:
            pass
    return page_urls

def get_vacancy_urls(page_urls, session):
    """  Формируем URL с Вакансиями"""

    for page_url in page_urls:
        # Получаем прямые URL вакансий.
        vacancy_urls = []

        session = requests.Session()
        request = session.get(page_url, headers=headers1)
        soup = bs(request.content,'lxml')
        # получаем блоки с вакансиями
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            link = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            print(link)
            vacancy_urls.append(link)

        return vacancy_urls

def get_vacancy_info(vacancy_urls, session):
    """  Заходим в каждый URL и получаем информацию о Вакансии. """

    for vacancy_url in vacancy_urls:
        vacancy_dict = {}

        request = session.get(vacancy_url, headers=headers1)
        soup = bs(request.content, 'lxml')
        div = soup.find_all('div', attrs={'itemtype': 'http://schema.org/JobPosting'})[0]
        service_id = div.find('meta', attrs={'itemprop': 'value'})['content']
        title = div.find('h1', attrs={'itemprop': 'title'}).text
        category = div.find('meta', attrs={'itemprop': 'industry'})['content']

        salary = ''

        try:
            salary_min = div.find('meta', attrs={'itemprop': 'minValue'})['content']
        except TypeError:
            salary_min = 0
        try:
            salary_max = div.find('meta', attrs={'itemprop': 'maxValue'})['content']
        except TypeError:
            salary_max = 0
        employment_prop = div.find('meta', attrs={'itemprop': 'employmentType'})['content']

        if salary_max == 0 and salary_min == 0:
            salary = 'Не указана'
        if employment_prop == 'FULL_TIME':
            employment_type = 'Полная занятость'
        else:
            employment_type = 'Частичная занятость'

        schedule = div.find('span', attrs={'itemprop': 'workHours'}).text

        description = div.find('div', attrs={'itemprop': 'description'}).text

        company_prop = div.find('meta', attrs={'itemprop': 'name'})['content'].lstrip()
        date_posted = div.find('meta', attrs={'itemprop': 'datePosted'})['content']

        # Проверка: Имеется ли данная вакансия в БД.
        try:
            vacancy = Vacancy.objects.get(title=title)
            if vacancy and vacancy.company.name == company_prop:
                continue


        except Vacancy.DoesNotExist:
            company, created_company = Employer.objects.get_or_create(name=company_prop)
            category, created_category = Category.objects.get_or_create(name=category, is_from=2)
            date_time_obj = datetime.datetime.strptime(re.sub(r'(?<=[+=][0-9]{2}):', '', date_posted), '%Y-%m-%dT%H:%M:%S.%f%z').date()

            Vacancy.objects.create(
                is_from=2,
                id_service=service_id,
                company=company,
                created_dt=date_time_obj,
                salary=salary,
                salary_min=salary_min,
                salary_max=salary_max,
                title=title,
                employment=employment_type,
                schedule=schedule,
                category=category,
                description=description
            )
            time.sleep(random.randint(1, 3))


def run():
    url_args = {
        'area': 113,            # Код региона
        'search_period': 3,     # Период поиска
        'text': 'python',       # Текст поиска
        'items_on_page': 100    # Элементы на странице
    }

    session = requests.Session()

    # Формируем URL относительно запроса
    query_url = '{}?{}'.format(base_url, urlencode(url_args, quote_via=quote_plus))

    # Получаем URLы всех страниц, которые доступны в поиске
    page_urls = get_pages_from_query(query_url, session)

    # Получаем URLы Вакансий
    vacancy_urls = get_vacancy_urls(page_urls, session)

    get_vacancy_info(vacancy_urls, session)