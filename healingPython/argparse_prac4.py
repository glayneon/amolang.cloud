#!python

import os
import random
import string
import time



class CheckDir:
    def __init__(self, original_func):
       self.original_func = original_func


    def __call__(self, *args, **kwargs):
        if isinstance(kwargs['dirname'], str):
            return self.original_func(*args, **kwargs)
        else:
            kwargs['dirname'] = os.getcwd()
            return self.original_func(*args, **kwargs)


@CheckDir
class randomPath:
    def __init__(self, dirname=None):
        self.dirname = dirname

    def randPath(self):
        temp_path = random.sample(string.ascii_letters, 12) + random.sample(string.digits, 4)
        random.shuffle(temp_path)
        self.randName = self.dirname + os.sep + time.strftime("%Y%m%d%H%M%S") + os.sep + ''.join(temp_path) + '.zip'

        print("{} is generated ...".format(self.randName))

if __name__ == '__main__':
    c = randomPath(dirname=None)
    d = randomPath(dirname="chase")
    c.randPath()
    d.randPath()
