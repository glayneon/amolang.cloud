#!python

import logging


class ShortLogger:
    '''Create logger instance.

    It'll create logger instance to send message at STDOUT.

    Return:
        Logger Instance.
    '''

    def __init__(self):
        '''
        Initirator
        '''
        _FMT = r"%(asctime)s - %(name)s - %(levelname)s - %(message)s"

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        l2 = logging.StreamHandler()
        l2.setLevel(logging.INFO)
        _FORMAT = logging.Formatter(_FMT)
        l2.setFormatter(_FORMAT)

        self.logger.addHandler(l2)

        # print test
        self.logger.info("Generating logger instance is successful...")






if __name__ == '__main__':
    a = ShortLogger()
