#!python

import psutil
import logging
import random
import string
import time
import json
import argparse
import os



class slogger:
    '''Make logger instance that will send message to STDOUT by default.

    This class will make an instance using logging module.

    Returns:
        logging instance.
    '''

    _FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __init__(self):
        '''
        Initiator
        '''
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        log2std = logging.StreamHandler()
        log2std.setLevel(logging.INFO)
        logFormat = logging.Formatter(self._FMT)
        log2std.setFormatter(logFormat)

        self.logger.addHandler(log2std)
        self.logger.info("{} : Complete setting logger ...".format(self.__class__))


class randomFile(slogger):
    '''Make the absolute path consists of sub-folder comprised to date and filename using random characters with 16 letters.

    This class will make the absolute file path and name using random, string and time modules.

    Returns:
        random path instance.
    '''

    def __init__(self, verbose=False):
        '''
        Initiator
        '''
        super().__init__()
        self.cwd = os.getcwd()
        if verbose:
            self.logger.info("Verbose mode is On ...")

    def randomPath(self, targetDir=None):
        '''
        return random path
        '''
        self.targetDir = targetDir
        tmpName = random.sample(string.ascii_letters, 12) + random.sample(string.digits, 4)
        random.shuffle(tmpName)

        if isinstance(self.targetDir, str):
            self.randomName = self.targetDir + os.sep + time.strftime("%Y%m%d") + os.sep + ''.join(tmpName) + "_" + time.strftime("%H%M%S")
        else:
            self.targetDir = self.cwd
            self.randomName = self.targetDir + os.sep + time.strftime("%Y%m%d") + os.sep + ''.join(tmpName) + "_" + time.strftime("%H%M%S")

        self.logger.info("{} is generating now ...".format(self.randomName))
        return self.randomName


class processStatus(slogger):
    '''Check process status and return its status.

    This class will check and return.

    Parameters:
        ProcessName (string)

    Returns:
        status instance.
    '''

    def __init__(self, verbose=False):
        '''
        Initiator
        '''
        super().__init__()
        if verbose:
            self.logger.info("Verbose mode is On ...")

    def searchProcess(self, processName=None):
        '''
        Search Process using processName variable.
        '''
        _foundit = False

        if isinstance(processName, str):
            self.processName = processName
            self.logger.info("Start searching {} in all processes ...".format(self.processName))

            self.pslistNow = psutil.process_iter(attrs=['name', 'pid'])

            for i in self.pslistNow:
                if i.info['name'].lower() == self.processName.lower():
                    self.targetProcess = psutil.Process(i.info['pid'])
                    self.logger.info("{} status : {} ...".format(i.info['name'], self.targetProcess.status))
                    _foundit = True
            else:
                if _foundit:
                    self.logger.info("Searching is done ... ")
                else:
                    self.logger.info("There's no named {} process now.".format(i.info['name']))


if __name__ == '__main__':
    _verbose = False

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase the level of verbosity', action="store_true")
    parser.add_argument('-d', '--dir', help='generate random filename using a given path', action='append')
    parser.add_argument('-p', '--process', help='check the status of a given process', action='append')

    args = parser.parse_args()

    if args.verbose:
        _verbose = True
    if args.dir:
        a = randomFile(verbose=_verbose)
        for i in args.dir:
            fileName = a.randomPath(targetDir=i)
            a.logger.info("Random Path is {} ...".format(fileName))
    if args.process:
        b = processStatus(verbose=_verbose)
        for i in args.process:
            b.searchProcess(processName=i)
