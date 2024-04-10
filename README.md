![bibiflags](./docs/source/_static/bibiflags.png)
===

bibiflags is a python tool to import YAML configs into Arguments for Python . 

It provides 2 ways to use it:

- **Parse all Arguments from YAML**:  see example ![main.py](./src/examples/main.py).
- **Merge Arguments form YAML and existing argparse.ArgumentParser**:  see example ![prog.py](./src/examples/prog.py).

## Getting Started

### Requirements and Installation

- Python version >= 3.8
- libaries:
  -- "PyYAML>=6.0.1"
  -- "OmegaConf>=2.3.0"
  -- "loguru>=0.7.2"

```bash
pip install bibiflags
```

Install from source via:

```bash
pip install git+https://github.com/bibiparrot/bibiflags.git
```


Or clone the repository and install with the following commands:

```bash
git clone git@github.com:bibiparrot/bibiflags.git
cd bibiflags
pip install -e .
```


## Usage

### Parse all Arguments from YAML
```
from pathlib import Path
from pprint import pformat

from loguru import logger

from bibiflags.bibiflags import BibiFlags

if __name__ == '__main__':
    flags = BibiFlags(root=str(Path(__file__).parent))
    logger.info(pformat(flags.parameters))

```

### Merge Arguments form YAML and existing argparse.ArgumentParser
```
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

```

## Changelog

### Version 0.1.0 2024-4-10