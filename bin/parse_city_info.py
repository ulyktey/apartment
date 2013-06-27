#!/usr/bin/env python
"""
Script verification input data and insert their in db
:Author:ylyktei
"""
import argparse
import logging
import logging.config
import sys
import os

sys.path.append('/usr/home/ylyktei/work_dir/apartment/')

from db import util as db_util
from utils import util
import parse_content

logging.config.fileConfig('/usr/home/ylyktei/work_dir/apartment/etc/log-config.conf')

def main():
    parser = argparse.ArgumentParser(description='Parse data from file.')
    parser.add_argument('-id', '--city_id', dest='city_id', type=int,
                        required=True, help='please write city_id from your db')
    parser.add_argument('-f','--file', dest='filename', type=str,
                        required=True, help='please write path to file')
    parser.add_argument('-v','--verbosity', dest='verbosity', type=int,
                        choices=[0, 1, 2, 3], default=3,
                        help='please chouse verbosity level (0, 1, 2, 3)')

    args = parser.parse_args()
    util.change_verbosity(args.verbosity)
    logger = util.get_logger()
    logger.info('Start process...')
    args.filename = os.path.abspath(args.filename)

    if not os.path.exists(args.filename):
        logger.error('File %s doesn\'t exist' % args.filename)
    elif db_util.get_city_by_id(args.city_id) is None:
        logger.error('Object with id = %s doesn\'t exist' % args.city_id)
    else:
        parse_content.parse_district(args.filename, args.city_id)

if __name__ == '__main__':
    sys.exit(main())
