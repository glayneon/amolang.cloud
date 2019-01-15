#!python

import argparse
import random
import string
import keyring
import time
import logging
import os


class shortLogger:
    def __init__(self):
        self.logger = logging.getLogger("Chase")
        self.logger.setLevel(logging.INFO)

        std = logging.StreamHandler()
        std.setLevel(logging.INFO)
        _fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname) - %(message)s")

        std.setFormatter(_fmt)

        self.logger.addHandler(std)
        self.logger.info("Initializing logging instance ...")


class randomPath(shortLogger):
    def __init__(self):
        super().__init__()

    def randomName(self, targetDir=None):
        self.targetDir = targetDir

        tempName = random.sample(string.ascii_letters, 12) + random.sample(string.digits, 4)
        random.shuffle(tempName)
        self.randName = os.getcwd() + os.sep + self.targetDir + os.sep + time.strftime("%Y%m%d") + os.sep + ''.join(tempName) + '_' + time.strftime("%H%M%S")

        self.logger.info("Generated random Name ... {}".format(self.randName))

        return self.randName


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='Increase Verbosity level', action='store_true')
    parser.add_argument('-r', '--random', help='Show random name', action='append')

    args = parser.parse_args()

    if args.verbose:
        print("Verbose is On ...")
    if args.random:
        RP = randomPath()
        for i in args.random:
            RP.randomName(targetDir=i)
