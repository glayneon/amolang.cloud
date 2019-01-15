#!python

import os
import sys
import time
import logging
import random
import string
import time


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("Chase")
        self.logger.setLevel(logging.INFO)

        stdlog = logging.StreamHandler()
        stdlog.setLevel(logging.INFO)
        _fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stdlog.setFormatter(_fmt)

        self.logger.addHandler(stdlog)
        self.logger.info("Initializing is success...")


class Output(Logger):
    # _DEBUG_PATH = os.getcwd() + os.sep + os.path.basename(__file__).split('.')[0]

    def __init__(self, original_func):
        super().__init__()
        global print
        print = self.logger.info
        print("it's loaded ...")
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        return self.original_func(*args, **kwargs)

@Output
class randomPath:
    def __init__(self):
        a = os.getcwd()
        filename = random.sample(string.ascii_letters, 12) + random.sample(string.digits, 4)
        random.shuffle(filename)

        random_name = os.getcwd() + os.sep + ''.join(filename)
        print("Generating name is...... {} ".format(random_name))



if __name__ == '__main__':
    a = randomPath()
    b = randomPath()
