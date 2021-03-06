#! /usr/bin/env python

"""
travis2dockerfile

Dumb little script to turn .travis.yml build steps into a Dockerfile that
tries to install the deps and run the steps.

Currently also clones Servo, to avoid having to run it from a fork and keep
the fork up to date and all that unpleasantness.

"""

import yaml


def read_traviscfg(path=".travis.yml"):
    cfg = []

    # thanks http://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
    with open(".travis.yml", 'r') as stream:
        try:
            cfg =yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return cfg


def write_dockerfile(cfg, path="Dockerfile"):
    contents = "FROM ubuntu:16.04\n"
    contents += "RUN apt-get update --fix-missing\n"

    # Cloning will someday be unnecessary
    contents += "RUN apt-get install -y git\n"

    for f in cfg['matrix']['include'][1]['addons']['apt']['packages']:
        contents += "RUN apt-get install -y {0}\n".format(f)

    contents += "\n"
    contents += "RUN git clone https://github.com/servo/servo.git ~/servo\n"
    contents += "WORKDIR ~/servo\n"


    for f in cfg['matrix']['include'][1]['script']:
        contents += "RUN {0}\n".format(f)

    with open(path, "w") as f:
        f.write(contents)

if __name__ == "__main__":
    cfg = read_traviscfg()
    write_dockerfile(cfg)
