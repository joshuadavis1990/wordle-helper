#!/bin/bash
echo "Thank you for installing Wordle Helper."
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        echo "Check complete. You have the correct version of Python installed."
    else
        echo "Sorry, this version of Python is not supported by Wordle Helper. Please download Python 3 at: https://www.python.org/downloads/" >&2
    fi
else
    echo "You need to install Python 3 to run Wordle Helper. You can download it here: https://www.python.org/downloads/" >&2
fi
echo "Creating virtual environment..."
python3 -m venv .venv
echo "Activating virtual environment..."
source .venv/bin/activate
echo "Installing dependencies..."
pip3 install -r requirements.txt
echo "Opening the application..."
python3 wordle.py
deactivate