"""Parse data content
"""
import logging
import re

from db import util as db_util
#from utils import vm_soup
from utils import util

CHARSETVM = 'CP1251'

def parse_city(file_path):
    """Parse input data string from file

    :Parameters:
        -`file_path`: path to txt file
    """
    logger = util.get_logger()
    logger.debug('Reading data from %s' % file_path)
    content = util.read_data_from_file(file_path)
    data_dict = _create_dict_from_txt(content)
    logger.debug('Set information from %s to db' % file_path)
    db_util.set_region_and_city(data_dict)
    logger.debug('Parse information from file %s complete success' % file_path)

def parse_district(file_path, city_id):
    """Parse input data string from file

    :Parameters:
        -`file_path`: path to txt file
        -`city_id`: id city in db
    """
    logger = util.get_logger()
    logger.debug('Reading data from %s' % file_path)
    content = util.read_data_from_file(file_path)
    data_dict = _create_dict_from_txt(content)
    logger.debug('Set information from %s to db' % file_path)
    db_util.set_district_and_street(data_dict, city_id)
    logger.debug('Parse information from file %s complete success' % file_path)

def _create_dict_from_txt(content):
    """Create dictionary format txt file

    :Parameter:
        -`content`: information from file

    :Return:
        data dictionary
    """
    data_dict = {}
    if content:
        data = content.split('\n')
        for line in data:
            line = line.split(',')
            if len(line) == 2:
                data_dict.setdefault(line[1].strip(), [])
                data_dict[line[1].strip()].append(line[0].strip())
    return data_dict

def data_from_vm():
    """Parse information from url
    """
    urls = db_util.get_urls()
    for url in urls:
        print url
        content = util.get_page(url.name, CHARSETVM)
        if content is not None:
            type_poster = url.type_url
            soup = util.html_soup(content)
            page = _count_page_vm_url(soup)
            _insert_data_vm_to_db(_parser_vm_data(soup), type_poster)
            if page > 1:
                for i in range(2, page+1):
                    link = '{0}&page={1}'.format(url.name, i)
                    content = util.get_page(link, CHARSETVM)
                    soup_inner = util.html_soup(content)
                    _insert_data_vm_to_db(_parser_vm_data(soup_inner),
                                           type_poster)

def _insert_data_vm_to_db(data, type_poster):
    """
    """
    for i in range(len(data['street'])):
        flat = {}
        street_obj = db_util.get_street(data['street'][i])
        if len(street_obj) >= 1:
            district_obj = db_util.get_district_by_id(street_obj[0].district_id)
            city = db_util.get_city_by_id(district_obj.city_id)
            region = db_util.get_region_by_id(city.region_id)
            flat['street'] = street_obj[0]
            flat['district'] = district_obj
            flat['city'] = city
            flat['region'] = region
            flat['type_room'] = data['type_room'][i]
            flat['count_room'] = data['count_room'][i]
            flat['floor'] = data['floor'][i]
            flat['max_floor'] = data['max_floor'][i]
            flat['price'] = data['price'][i]
            flat['full_price'] = data['full_price'][i]
            flat['s_live'] = data['s_live'][i]
            flat['s_cook'] = data['s_cook'][i]
            flat['description'] = data['description'][i]
            flat['phone'] = data['phone'][i]
            flat['image'] = data['image'][i]
            flat['type_poster'] = type_poster
            db_util.set_flat(flat)

