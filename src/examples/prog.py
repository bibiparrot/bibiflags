from pathlib import Path
from pprint import pformat, pprint

from loguru import logger
from bibiflags.bibiflags import BibiFlags

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    flags = BibiFlags(argparser=parser,
                      root=str(Path(__file__).parent),
                      app_name='main')

    pprint(flags.parameters)
