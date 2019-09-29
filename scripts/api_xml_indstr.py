from xml.etree import ElementTree as ET
from urllib.parse import urlparse

from vacancy.models import Category


def run():

    file_xml = '/home/des/Загрузки/industries.xml'

    tree = ET.parse(file_xml)

    root = tree.getroot()
    for child in root:
        model_dict = {}
        model_dict.update({
            'is_from': 1,
            'code': child.find('code').text,
            'name': child.find('name').text
        })

        Category.objects.create(**model_dict)

