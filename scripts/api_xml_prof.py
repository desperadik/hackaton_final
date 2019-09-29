from xml.etree import ElementTree as ET
from urllib.parse import urlparse

from vacancy.models import Profession


def run():

    file_xml = '/home/des/Загрузки/professions.xml'

    tree = ET.parse(file_xml)

    root = tree.getroot()
    for child in root:
        model_dict = {}
        fragment = urlparse(child.attrib['about']).fragment
        model_dict.update({
            'ident': fragment,
            'name': child.find('name').text,
        })
        try:
            Profession.objects.get(ident=fragment)
        except Profession.DoesNotExist:
            Profession.objects.create(**model_dict)
