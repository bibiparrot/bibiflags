from pathlib import Path

from bibiflags import BibiFlags

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("echo", action='store_true')
    flags = BibiFlags(argparser=parser,
                      root=str(Path(__file__).parent),
                      app_name='main')

    print(flags.parameters)
