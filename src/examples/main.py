from pathlib import Path

from bibiflags import BibiFlags

if __name__ == '__main__':
    flags = BibiFlags(root=str(Path(__file__).parent))
    print(flags.parameters)
