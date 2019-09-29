import json
import time

import requests

from vacancy.models import Vacancy, Employer, Category


class Parser(object):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://opendata.trudvsem.ru/api/v1/'
    api_url = ''
    options = None
    modifiedFrom = ''

    def get_company(self, company=None):
        try:
            inn = company['inn']
        except:
            inn = None
        if inn:
            try:
                company = Employer.objects.get(inn=inn)
            except Employer.DoesNotExist:
                company = Employer(
                    name=company['name'],
                    ogrn=company['ogrn'],
                    companycode=company['companycode'],
                    inn=inn
                )
                company.save()
        else:
            try:
                company = Employer.objects.get(
                    name=company['name']
                )
            except Employer.DoesNotExist:
                company = Employer(
                    name=company['name'],
                    ogrn=company['ogrn'],
                    companycode=company['companycode'],
                )
                company.save()

        return company

    def get_category(self, category=None):
        try:
            category = Category.objects.get(
                name=category['specialisation']
            )
        except Category.DoesNotExist:
            category = Category(
                name=category['specialisation'],
                is_from=1
            )
            category.save()

        return category

    def get_options(self, offset=None, limit=None, modifiedFrom=None, modifiedTo=None):
        options = ''
        if offset:
            options += 'offset={}'.format(offset)
        if limit:
            options += '&limit={}'.format(limit)
        if modifiedFrom:
            options += '&modifiedFrom{}'.format(modifiedFrom)
        if modifiedTo:
            options += '&modifiedTo{}'.format(modifiedTo)
        return options

    def vacancies(self, **kwargs):
        vacancies = []
        self.api_url = 'vacancies'
        self.options = self.get_options(**kwargs)
        if self.options:
            self.api_url += '?{}'.format(self.options)

        api_url = "{}{}".format(self.url, self.api_url)
        print("Запрос к апи: {}".format(api_url))

        with requests.Session() as session:
            try:
                response = session.get(api_url)
                json_data = json.loads(response.text)
                if json_data['status'] == '200':
                    results = json_data['results']

                    for i in results['vacancies']:
                        vacancy = i['vacancy']
                        # Обработка вакансии
                        try:
                            obj = Vacancy.objects.get(
                                id_service=vacancy['id']
                            )
                        except Vacancy.DoesNotExist:
                            obj = Vacancy(
                                is_from=1,
                                id_service=vacancy['id'],
                                company=self.get_company(vacancy['company']),
                                created_dt=vacancy['creation-date'],
                                salary=vacancy['salary'],
                                salary_min=vacancy['salary_min'],
                                salary_max=vacancy['salary_max'],
                                title=vacancy['job-name'],
                                employment=vacancy['employment'],
                                schedule=vacancy['schedule'],
                                duty=vacancy['duty'],
                                category=self.get_category(vacancy['category']),
                                # education=vacancy['requirement']['education'],
                                # qualification=vacancy['requirement']['qualification'],
                                # experience=vacancy['requirement']['experience'],
                                # address=vacancy['addresses'][0]['location']

                            )
                            obj.save()
                        print(obj)
                else:
                    vacancies = False
            except Exception as inst:
                print(inst)

        return vacancies


def run():
    parser = Parser()
    i = 0
    limit = 100
    while i <= 5055:

        vacancies = parser.vacancies(offset=i + 1,
                                     limit=limit,
                                     )
        if vacancies == False:
            limit -= 1
        i += limit
        time.sleep(2)

run()
