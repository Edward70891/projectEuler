#!/bin/bash

if [[ $1 ]]; then
    printf "#!/bin/env python3\n\n# Problem at:\n# https://projecteuler.net/problem=$1\n\n\n" > $1.py
    chmod +x $1.py
    nvim $1.py
fi
