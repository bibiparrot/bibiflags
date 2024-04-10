from pathlib import Path
from pprint import pformat,pprint

from bibiflags.bibiflags import BibiFlags

if __name__ == '__main__':
    flags = BibiFlags(root=str(Path(__file__).parent))
    pprint(flags.parameters)
