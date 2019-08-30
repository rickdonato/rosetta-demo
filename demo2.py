from ntc_rosetta import get_driver

junos = get_driver("junos", "openconfig")
junos_driver = junos()

with open("data/junos/dev_conf.xml", "r") as f:
    config = f.read()

print(config)

parsed = junos_driver.parse(native={"dev_conf": config})

import json
print(json.dumps(parsed.raw_value(), indent=4))

with open("data/junos/dev_conf.xml", "r") as f:
    running_config = f.read()

with open("data/junos/new_dev_conf.xml", "r") as f:
    candidate_config = f.read()

parsed_candidate = junos_driver.parse(native={"dev_conf": candidate_config})
parsed_running = junos_driver.parse(native={"dev_conf": running_config})

config = junos_driver.merge(
    candidate=parsed_candidate.raw_value(),
    running=parsed_running.raw_value()
)
print(config)
print("====================")
ios = get_driver("ios", "openconfig")
ios_driver = ios()

with open("data/ios/dev_conf.txt", "r") as f:
    config = f.read()

print(config)

parsed = ios_driver.parse(native={"dev_conf": config})

import json
print(json.dumps(parsed.raw_value(), indent=4))

with open("data/ios/dev_conf.txt", "r") as f:
    running_config = f.read()

with open("data/ios/new_dev_conf.txt", "r") as f:
    candidate_config = f.read()

parsed_candidate = ios_driver.parse(native={"dev_conf": candidate_config})
parsed_running = ios_driver.parse(native={"dev_conf": running_config})

print("--")


config = ios_driver.merge(
    candidate=parsed_candidate.raw_value(),
    running=parsed_running.raw_value()
)

print(config)
