from pathlib import Path
from pprint import pformat

from loguru import logger

from bibiflags.bibiflags import BibiFlags

if __name__ == '__main__':
    flags = BibiFlags(root=str(Path(__file__).parent))
    logger.info(pformat(flags.parameters))
