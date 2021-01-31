import argparse
from typing import TypeVar, Generic
import pipe

LANG_NAME = "cips"
FILE_ENDING = ".cps"


def parse_args() -> Generic:

    parser = argparse.ArgumentParser(
        description=f"Compile source files of the {LANG_NAME} language.")
    parser.add_argument("-c", "--compiler", type=str, dest="cc", default="gcc",
                        help="The compiler used for compiling the c ouput")
    parser.add_argument(dest="file", nargs="+",
                        help=f"The source files. (e.g.:{FILE_ENDING})")

    return parser.parse_args()


def main():

    args = parse_args()

    print(args.cc)
    print(args.file)

    pipe.pipe(args.file)


if __name__ == "__main__":
    main()
