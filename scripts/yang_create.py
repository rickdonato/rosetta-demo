#!./venv/bin/python 

from ntc_rosetta import get_driver
import argparse
import json

parser = argparse.ArgumentParser(description='Rosetta merge from Yang')
parser.add_argument('-n','--nos', help='nos', required=True)
parser.add_argument('-c','--config', help='config', required=True)

args = vars(parser.parse_args())

def load_driver(nos):
    nos = get_driver(nos, "openconfig")
    return nos()

def create_yang(nos, config):
    nos_driver = load_driver(nos)

    with open(config, "r") as f:
        config = f.read()

    parsed = nos_driver.parse(native={"dev_conf": config})
    return json.dumps(parsed.raw_value(), indent=4)

print(create_yang(**args))
