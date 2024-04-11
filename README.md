![bibiflags](https://github.com/bibiparrot/bibiflags/blob/main/docs/source/_static/bibiflags.png)
===

bibiflags is a python tool to import YAML configs into Arguments for Python . 

It provides 2 ways to use it:

- **Parse all Arguments from YAML**:  see example ![main.py](https://github.com/bibiparrot/bibiflags/blob/main/src/examples/main.py).
- **Merge Arguments form YAML and existing argparse.ArgumentParser**:  see example ![prog.py](https://github.com/bibiparrot/bibiflags/blob/main/src/examples/prog.py).

## Getting Started

### Requirements and Installation

- Python version >= 3.8
- libaries:
  * "PyYAML>=6.0.1"

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

YAML file


```
flags:
  - default: string-type-arguments
    dest: str_arg
    help: string type args
    option_strings:
      - --str_arg
      - -sa
    type: str

  - const: true
    default: false
    dest: bool_arg
    help: bool type args
    nargs: 0
    option_strings:
      - --bool_arg
      - -ba
    type: bool

  - default: 8
    dest: int_arg
    help: int type args
    option_strings:
      - --int_arg
      - -ia
    type: int

  - default: 0.1
    dest: float_arg
    help: float type args
    option_strings:
      - --float_arg
      - -fa
    type: float

  - default:
      - 1
      - 2
      - 3
      - 4
    dest: list_arg
    help: list type args
    nargs: +
    option_strings:
      - --list_arg
      - -la
    type: int
```


### Parse all Arguments from YAML
```
from pathlib import Path

from bibiflags import BibiFlags

if __name__ == '__main__':
    flags = BibiFlags(root=str(Path(__file__).parent))
    print(flags.parameters)


```

### Merge Arguments form YAML and existing argparse.ArgumentParser
```
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


```

## Changelog

### Version 0.1.3 2024-4-12