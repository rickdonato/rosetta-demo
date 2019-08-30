from ntc_rosetta import get_driver
import sys

candidate = sys.argv[1]
running = sys.argv[2]
nos = sys.argv[3]

def load_driver(nos):
    print("load driver")
    nos = get_driver(nos, "openconfig")
    return nos()

def merge_from_yang():
    nos_driver = load_driver(nos)

    print(running)
    print("open configs (yang)")
    with open(running, "r") as f:
        running_config = f.read()

    with open(candidate, "r") as f:
        candidate_config = f.read()

    print("merge")
    config = nos_driver.merge(
        candidate=parsed_candidate.raw_value(),
        running=parsed_running.raw_value()
    )
    return config

def convert_native_to_yang():
    load_driver()

merge_from_yang()
