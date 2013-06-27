"""Vm flat parsers method
"""
import re
import urllib2

def parser_vm_data(soup):
    """Parse data from html

    :Parameters:
        -`soup: object beautifulsoup lib

    :Return:
        dictionary data
    """
    info = {'street': street_parser(soup),
            'count_room': count_room_parser(soup),
            'type_room': type_room_parser(soup),
            'floor': floor_parser(soup),
            'max_floor': max_floor_parser(soup),
            'price': price_parser(soup),
            'full_price': full_price_parser(soup),
            's_live': square_live_parser(soup),
            's_cook': square_cook_parser(soup),
            'description': description_parser(soup),
            'phone': phone_parser(soup),
            'image': image_parser(soup)}

    return info

def count_page_vm_url(soup):
    """Search pagenation in html

    :Parameters:
        -`soup: object beautifulsoup lib

    :Return:
        count page (integer)
    """
    string = soup.find('div', {'class': 'pagination'}).text
    if string is not None:
        val = re.findall(r'\d', string)
        if len(val) > 0:
            return int(val[-1])
    return 1

def street_parser(soup):
    """Parse street from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    street = soup.findAll('strong',
                 {'style': 'display:block; line-height:12px;'})

    list_obj = []
    for i in street:
        string = re.sub(r'\(.*\)', '', i.string)
        string = re.sub(r'.*\.', '', string).strip()
        list_obj.append(string)
    return list_obj

def count_room_parser(soup):
    """Parse count_room from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    count_room = soup.findAll('td',
             {'style': 'width:100%', 'valign': 'top'})
    list_obj = []
    for i in count_room:
        value = i.find('span', {'style': 'font-weight:bold'})
        if value is None:
            value = '1'
        else:
            value = value.text
        list_obj.append(value)
    return list_obj

def type_room_parser(soup):
    """Parse type_room from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    type_room = soup.findAll('td',
             {'valign': 'top', 'style': 'width:100%'})
    list_obj = []
    for i in type_room:
        str_type = i.text
        rezult = re.sub(r'.*\s|.*\:|.*\d', '', str_type.strip()).strip()
        if len(rezult) >= 8:
            list_obj.append(rezult[5:])
        else:
            list_obj.append(rezult)
    return list_obj

def floor_parser(soup):
    """Parse floor from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    floor = soup.findAll('td',
             {'style': 'width:width:50px; text-align:center'})
    list_obj = []
    for i in floor:
        floar_list = i.string.replace('-', '0').split('/')
        list_obj.append(floar_list[0])
    return list_obj

def max_floor_parser(soup):
    """Parse max floor from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    floor = soup.findAll('td',
             {'style': 'width:width:50px; text-align:center'})
    list_obj = []
    for i in floor:
        floar_list = i.string.replace('-', '0').split('/')
        list_obj.append(floar_list[1])
    return list_obj

def price_parser(soup):
    """Parse price from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    list_obj = []
    price = soup.findAll('td',
             {'style': 'text-align:right;'})
    for i in price:
        price_m = i.find('span')
        if price_m:
            price_m = price_m.text
            price_m = re.sub(r'\s+', '', price_m)
            if re.findall(r'\d+', price_m):
                list_obj.append(int(re.findall(r'\d+', price_m)[0]))
            else:
                list_obj.append(int('1'))
        else:
            list_obj.append(int('1'))
    return list_obj

def full_price_parser(soup):
    """Parse full price from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    price = soup.findAll('td',
             {'style': 'text-align:right;'})
    list_obj = []
    for i in price:
        full = i.find('strong')
        if full:
            full = full.text
            full = re.sub(r'\s+', '', full)
            if re.findall(r'\d+', full):
                list_obj.append(int(re.findall(r'\d+', full)[0]))
            else:
                list_obj.append(int('1'))
        else:
            list_obj.append(int('1'))
    return list_obj


def square_live_parser(soup):
    """Parse square live from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    square = soup.findAll('td',
             {'style': 'padding-left:0px;width:50px; text-align:center;'})
    list_obj = []
    for i in square:
        square_list = i.string.replace('-', '0').split('/')
        list_obj.append(int(square_list[1].split(',')[0]))
    return list_obj

def square_cook_parser(soup):
    """Parse square cook from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    square = soup.findAll('td',
             {'style': 'padding-left:0px;width:50px; text-align:center;'})
    list_obj = []
    for i in square:
        square_list = i.string.replace('-', '0').split('/')
        list_obj.append(int(square_list[2].split(',')[0]))
    return list_obj


def description_parser(soup):
    """Parse description from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    description = soup.findAll('div',
             {'class':'text_hidden_def'})
    list_obj = []
    for i in description:
        if i.string:
            list_obj.append(i.string)
        else:
            list_obj.append(' ')
    return list_obj

def phone_parser(soup):
    """Parse phones from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    list_obj = []
    phone = soup.findAll('span',
             {'class': 'ner-auto-tel'})
    for i in phone:
        list_obj.append(
                re.findall(r'\(\d{3}\)\d{3}\-\d{4}|\d{3}\-\d{4}', i.string))
    return list_obj

def image_parser(soup):
    """Parse image from html

    :Parameters:
        -`soup`: object beautifulsoup lib

    :Return:
        list data
    """
    list_obj = []
    image = soup.findAll('td',
             {'class': 'left_border_table top_border_table',
               'valign': 'top' })
    for val in image:
        rel = val.find('img').get('rel')
        flat_id = re.sub(r'[^\d+]','', rel)
        images_str = re.findall(r'\w{4}\_\w{6}\[' + flat_id + ']\=\".*\"', soup.prettify())
        if len(images_str) > 0:
            images = re.findall(r'\d+', images_str[0])
            if len(images) > 1:
                values = []
                for i in images[1:]:
                    try:
                      link = 'http://vashmagazin.ua/shop/img/pub_{0}.jpg'.format(i)
                      urllib2.urlopen(urllib2.Request(link))
                      values.append(link)
                    except urllib2.HTTPError:
                      pass

                list_obj.append(values)
            else:
                list_obj.append([])
        else:
            list_obj.append([])
    return list_obj
