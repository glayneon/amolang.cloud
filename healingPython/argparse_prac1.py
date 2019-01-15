#!python

import psutil
import os
import logging

import json
import random
import string
import time


class ShortLogger:
    '''This class is the shortest logger class for convinient use.

    This will return the instance of logger defined already to send message at STDOUT.

    Returns:
        Logger Instance only.
    '''

    def __init__(self):
        '''
        Initiator for logger.
        '''
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        l2 = logging.StreamHandler()
        l2.setLevel(logging.INFO)
        _fmt = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s - %(message)s")
        l2.setFormatter(_fmt)

        self.logger.addHandler(l2)
        self.logger.info("Start logging ...")


class RandomName(ShortLogger):
    '''This class is meant to return Random values.

    This will return Random values when you use the method 'randname'.

    Returns:
        Instance
    '''

    def __init__(self):
        '''
        Initiator for generating random value.
        '''
        super().__init__()

        self.logger.info("Start loadind RandomName class...")

    def randName(self):
        '''
        Return random name.
        '''

        temp_letters = random.sample(string.ascii_letters, 12) + random.sample(string.digits, 4)
        random.shuffle(temp_letters)

        random_name = os.getcwd() + os.sep + time.strftime("%Y%m%d") + os.sep + time.strftime("%H%M%S") + ''.join(temp_letters) + '.zip'

        self.logger.info("Generating {} ...".format(random_name))

        return random_name


class GetProcess(ShortLogger):
    '''Search Process using name and get instance.

    This will search for given name process in whole processes runing on system.

    Return:
        Instance
    '''

    def __init__(self, name):
        '''
        Initiator.
        '''

        self.name = name
        self.found = False
        super().__init__()

        if self.name and isinstance(self.name, str):
            pslist = psutil.process_iter(attrs=['name', 'pid'])

            for i in pslist:
                if i.info['name'].lower() == self.name.lower():
                    self.logger.info("Found Process {} and PID is {} ...".format(i.info['name'], i.info['pid']))
                    self.pid = psutil.Process(i.info['pid'])
                    self.found = True
            else:
                self.logger.info("Searching process is done...")
        else:
            raise TypeError


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', help='increase the level of verbosicy', action="store_true")
    parser.add_argument('-r', '--random', help='display the random name with the current location', action="store_true")
    parser.add_argument('-s', '--search', help='search a given name process in system', type=str)

    args = parser.parse_args()

    if args.verbose:
        print("{} : {}".format(__file__, os.getpid()))
    if args.random:
        RN = RandomName()
        print(RN.randName())
    if args.search:
        _a = GetProcess(name=args.search)
        if _a.found:
            _a.pid.kill()
        else:
            print("There's no process named {}.".format(args.search))
