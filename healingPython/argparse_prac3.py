#!python

import random
import string
import time
import logging
import os
import argparse
import json
import re


class slogger:
    def __init__(self, verbose=False):
        self.logger = logging.getLogger(__name__)

        if verbose:
            self.logger.debug("Verbose mode is on ...")
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        stdHandler = logging.StreamHandler()
        stdHandler.setLevel(logging.INFO)
        _fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stdHandler.setFormatter(_fmt)

        self.logger.addHandler(stdHandler)

        self.logger.info("Start logging ...")


class timeLogger:
    EXC_TIME = time.strftime("%Y%m%d %H%M%S")

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(timeLogger.EXC_TIME)

        return self.original_func(*args, **kwargs)


@timeLogger
def RandomPath(targetPath=None):
    if not targetPath:
        targetPath = os.getcwd()

    randName = random.sample(string.ascii_letters, 12) + random.sample(string.digits, 4)
    random.shuffle(randName)
    filename = targetPath + os.sep + time.strftime('%Y%m%d') + os.sep + ''.join(randName) + '_' + time.strftime("%H%M%S")

    return filename



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help="target directory to generate random path.", action="append")

    args = parser.parse_args()

    if args.dir:
        for i in args.dir:
            print(RandomPath(targetPath=i))
    else:
        print(RandomPath())
