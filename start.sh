#!/bin/bash
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 wordle.py
    else
        echo "Sorry, this version of Python is not supported by Wordle Helper. Please download Python3 at: https://www.python.org/downloads/"
    fi
else
    echo "You need to install Python3 to run Wordle Helper at its full potential. You can download it here: https://www.python.org/downloads/" >&2
fi