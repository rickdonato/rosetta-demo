from ntc_rosetta import get_driver
import argparse

parser = argparse.ArgumentParser(description='Rosetta merge from Yang')
parser.add_argument('-n','--nos', help='nos', required=True)
parser.add_argument('-c','--candidate', help='candidate config', required=True)
parser.add_argument('-r','--running', help='running config', required=True)


args = vars(parser.parse_args())

def load_driver(nos):
    nos = get_driver(nos, "openconfig")
    return nos()

def merge_yang():
    nos_driver = load_driver(nos)

    with open(running, "r") as f:
        running_config = f.read()

    with open(candidate, "r") as f:
        candidate_config = f.read()

    config = nos_driver.merge(
        candidate=parsed_candidate.raw_value(),
        running=parsed_running.raw_value()
    )
    return config


