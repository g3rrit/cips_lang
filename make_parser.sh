#!/bin/bash

DIR="$( cd "$( dirname "$0" )" >/dev/null 2>&1 && pwd )"

python -m grako --name CLS --outfile "${DIR}/src/ast/_gen.py" grammar.y