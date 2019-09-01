#!./venv/bin/python -i

from ntc_rosetta import get_driver
from copy import deepcopy
import argparse
import json

parser = argparse.ArgumentParser(description='Rosetta merge from Yang')
parser.add_argument('-n','--nos', help='nos', required=True)
parser.add_argument('-c','--candidate', help='candidate', required=True)
parser.add_argument('-r','--running', help='running', required=True)

args = vars(parser.parse_args())

def load_driver(nos):
    nos = get_driver(nos, "openconfig")
    return nos()

def merge_yang(nos, running, candidate):
    nos_driver = load_driver(nos)

    with open(running, "r") as f:
        running_config = json.load(f)

    with open(candidate, "r") as f:
        candidate_config = json.load(f)

    candidate = deepcopy(candidate_config)
    running = deepcopy(running_config)

    config = nos_driver.merge(
        candidate=candidate,
        running=running
    )
    return config

print(merge_yang(**args))
