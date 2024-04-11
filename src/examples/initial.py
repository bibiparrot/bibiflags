from pathlib import Path
from pprint import pprint, pformat
import argparse

from bibiflags import BibiFlags

from pathlib import Path

from bibiflags import BibiFlags

if __name__ == '__main__':
    '''
    https://docs.python.org/3/library/argparse.html
    '''
    # parser = argparse.ArgumentParser(
    #     prog='ProgramName',
    #     description='What the program does',
    #     epilog='Text at the bottom of help')
    # parser.add_argument('filename')  # positional argument
    # parser.add_argument('-c', '--count')  # option that takes a value
    # parser.add_argument('-v', '--verbose',
    #                     action='store_true')  # on/off flag
    flags = BibiFlags(root=str(Path(__file__).parent),
                      app_name='initial')

    print(flags.parameters)
