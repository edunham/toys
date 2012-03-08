# usr/bin/env/python

# For some damn reason, plain old "import obj" breaks things
from obj import Offtopic
from robot import BuildStandard

robot = BuildStandard(DEBUG=True)

topic = robot.say_hello()

theysay = raw_input("> ")

while(True):
	topix = robot.topics_opened(theysay) # tuple of all new topics opened
	agree = robot.agrees(theysay) # bool, did they say yes-word?
	disagree = robot.disagrees(theysay) # bool, did they say no-word?
	

