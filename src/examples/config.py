from pathlib import Path

from bibiflags import BibiFlags

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('filename')  # positional argument
    parser.add_argument('-c', '--count')  # option that takes a value
    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag
    flags = BibiFlags(argparser=parser,
                      root=str(Path(__file__).parent),
                      app_name='config')

    print(flags.configs)
