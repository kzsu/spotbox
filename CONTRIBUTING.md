# Working on the Spotbox

## Prerequisites

You need to have:

- Python 2.7 (for now, sorry 😢) and `pip` installed
- The `pipenv` tool ([See here for installation instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv))

## Setting up your environment

- Clone this repo
- In the repo directory, run `pipenv install`. This should create a virtual environment and install the necessary dependencies for you.

To run the spotbox, you can either:

- Start a shell in the spotbox virtual environment
  - Run `pipenv shell` to get a shell into the virtual environment.
  - In this shell, run `python spotbox/spotbox.py` to launch the Spotbox.
- Run `pipenv run python spotbox/spotbox.py` to run the Spotbox in the virtual environment directly without starting a shell first.
