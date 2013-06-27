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

sys.path.append('/usr/home/ylyktei/work_dir/apartment')

from db import util as db_util
from utils import util
import parse_content

logging.config.fileConfig('/usr/home/ylyktei/work_dir/apartment/etc/log-config.conf')

def main():
    parser = argparse.ArgumentParser(description='Parse data from file.')
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
    else:
        parse_content.parse_city(args.filename)

if __name__ == '__main__':
    sys.exit(main())
