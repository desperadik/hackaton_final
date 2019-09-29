from urllib.parse import urlparse
from xml.etree import ElementTree as ET

from vacancy.models import Category, Vacancy


def run():

    file_xml = '/home/des/Загрузки/data2.xml'

    tree = ET.iterparse(file_xml, events={'start'})
    vacansy_dict = {}
    for event, element in tree:
        if element.tag=='industry' and event == "start":

            fragment = urlparse(element.attrib['resource']).fragment
            category = Category.objects.get_or_create(code=fragment)
            vacansy_dict.update({
                'category': category
            })
            if element.tag=='creationDate':
                vacansy_dict.update({
                    'created_dt': element.text
                })
            if element.tag == 'identifier' and len(element.tag) == 36:
                vacansy_dict.update({
                    'id_service': element.text
                })

            if element.tag=='salary':
                vacansy_dict.update({
                    'salary': element.text
                })
            if element.tag=='salaryMin':
                vacansy_dict.update({
                    'salary_min': element.text
                })
            if element.tag == 'salaryMax':
                vacansy_dict.update({
                    'salary_max': element.text
                })
            if element.tag=='title':
                vacansy_dict.update({
                    'title': element.text
                })

            if element.tag == 'employmentType':
                vacansy_dict.update({
                    'employment': element.text
                })
            if element.tag == 'workHours':
                vacansy_dict.update({
                    'schedule': element.text
                })
            if element.tag == 'responsibilities':
                vacansy_dict.update({
                    'duty': element.text
                })
            if element.tag == 'otherBenefits':
                vacansy_dict.update({
                    'description': element.text
                })
            if element.tag == 'educationType':
                vacansy_dict.update({
                    'education': element.text
                })
            if element.tag == 'experienceRequirements':
                vacansy_dict.update({
                    'experience': element.text
                })
            if element.tag == 'qualifications':
                vacansy_dict.update({
                    'qualification': element.text
                })
                print (vacansy_dict)
                Vacancy.objects.get_or_create(**vacansy_dict)
        # # address = ''
        # # if element.tag == 'address' or element.tag == 'additionalAddressInfo':
        # #     address += ' ' + element.text
        # #     print(address)
        #     if element.tag == 'responsibilities':
        #         print(element.text)
        #     if element.tag == 'otherBenefits':
        #         print(element.text)



#
# from lxml import etree
#
#
# def parseBookXML(xmlFile):
#     with open(xmlFile) as fobj:
#         xml = fobj.read()
#
#     root = etree.fromstring(xml)
#
#     book_dict = {}
#     books = []
#     for book in root.getchildren():
#         for elem in book.getchildren():
#             print(elem.text)
#         #     if not elem.text:
#         #         text = "None"
#         #     else:
#         #         text = elem.text
#         #     print(elem.tag + " => " + text)
#         #     book_dict[elem.tag] = text
#         #
#         # if book.tag == "book":
#         #     books.append(book_dict)
#         #     book_dict = {}
#
#     return books
#
#
# def run():
#     parseBookXML('/home/des/Загрузки/data2.xml')
