"""Project utility functions.
"""

import logging
import codecs
import re
import socket
import smtplib
import urllib2
import urlparse

try:
    #import BeautifulSoup version 4
    from bs4 import BeautifulSoup
except:
    #import BeautifulSoup version 3
    from BeautifulSoup import BeautifulSoup


VERBOSITY = (0, 1, 2, 3)

def html_soup(page):
    """BeautifulSoup obj

    :Parameters:
        -`page`: string html

    :Return:
        obj data
    """
    soup = BeautifulSoup(page)
    soup.prettify()
    return soup


def clear_html(data):
    """Clear html

    :Parameters:
        -`data`: html string

    :Return:
        return clear html
    """
    data = re.sub(r'<(script|style|noscript).*?</\1>(?s)', '', data)
    data = data.replace('onsubmit="";', '')
    data = data.replace('ua', '')
    return data

def get_page(url, charset):
    """Parse content from url page

    :Parameters:
        -`url`: url address

    :Return:
        content url address
    """
    try:
        response = urllib2.urlopen(url)
        data = response.read().decode(charset)
        if data:
            return data
    except (urllib2.HTTPError, urllib2.URLError):
        return None


def read_data_from_file(filepath):
    """Read content from a file

    :Parameters:
        -`filepath`: full path with file name

    :Return:
        data from file
    """

    logger = get_logger()
    try:
        fopen = codecs.open(filepath, 'r', encoding='utf8')
        data = fopen.read()
        if data:
            return data
        else:
            logger.error('it is not a valid %s' % filepath)
    except (IOError, OSError):
        logger.error('File %s dosen\'t existing or not a permission' % filepath)
    return None

def get_logger():
    """Get loggin object
    :Return:
        loggin object
    """
    return logging.getLogger();

def change_verbosity(level):
    """Set verbosity level

    :Parameters:
        -`level`: number from tuple (0, 1, 2, 3)
    """
    # We will log to syslog all the messages with verbosity configured
    # via log.conf and we will log to stdout with user-defined verbosity.

    # VERBOSITY - tuple (0, 1, 2, 3) with log levels
    if level == VERBOSITY[2]:
        logging.getLogger().setLevel(logging.INFO)
    elif level == VERBOSITY[0]:
        logging.getLogger().setLevel(logging.CRITICAL)
    elif level == VERBOSITY[1]:
        logging.getLogger().setLevel(logging.ERROR)
    else:
        logging.getLogger().setLevel(logging.DEBUG)
