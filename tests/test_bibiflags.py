from pathlib import Path
from pprint import pprint, pformat
import argparse

from bibiflags.bibiflags import BibiFlags


def test_bibiflags():
    flags = BibiFlags(root=Path(__file__).parent)
    pprint(pformat(flags.parameters))
    assert len(flags.parameters) == 5
