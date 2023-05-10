# T1A3 Terminal Application

**Name:** Joshua Davis

**Student Number:** 14209

| Assessment Component | Link |
| --- | --- |
| GitHub repository | https://github.com/joshuadavis1990/wordle-helper |
| Video presentation link | Insert link here |
| Trello link | https://trello.com/b/jSdMjDvb/wordle-helper |

## Features of Wordle Helper

*Wordle Helper* is an intelligent command line application that:

1. Assists the user in solving *Wordle* puzzles by locally prompting them throughout their six attempts at https://www.nytimes.com/games/wordle/index.html
1. Dynamically searches through the current *Wordle* dictionary of approximately 2000 5 letter words to narrow down the possible word candidates each day
1. Provides a small list of random words from the Wordle dictionary the user may choose to input at the start of the program
1. Includes an easy coding system for the user to input *Wordle* data: G = Green, Y = Yellow, X = Grey (e.g. XXXYG)
1. Reads and responds to the symbols in the user's input
1. Presents the user with, after each of their six possible attempts, a short list of words that contain the most frequent letters used in the Wordle word bank

## Styling Conventions

*Wordle Helper* uses the *PEP 8 – Style Guide for Python Code* by Guido van Rossum: https://peps.python.org/pep-0008/

## Help Documentation

To run Worlde Helper using the python3 interpreter, fork and then clone the following GitHub repository using:

```
git clone git@github.com:joshuadavis1990/wordle-helper.git
```

Then, run the app by changing into the `wordle-helper` directory and entering the following into the command line:

```
python3 wordle_helper.py
```

You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application

## Implementation Plan

Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item