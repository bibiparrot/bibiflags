from pathlib import Path
from pprint import pprint, pformat
from loguru import logger

from bibiflags.bibiflags import BibiFlags


def test_bibiflags():
    flags = BibiFlags(root=Path(__file__).parent)
    logger.info(pformat(flags.parameters))
    assert len(flags.parameters) == 5
