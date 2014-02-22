# usr/bin/env/python

# For some damn reason, plain old "import obj" breaks things
from robot import BuildStandard

robot = BuildStandard(DEBUG=False)

topic = robot.say_hello()

theysay = raw_input("> ")

while(True):
	topix = robot.topics_triggered(theysay) # tuple of all new topics opened
	agree = robot.agrees(theysay) # bool, did they say yes-word?
	disagree = robot.disagrees(theysay) # bool, did they say no-word?

	if agree or disagree:
		robot.followup(topic, theysay)

	robot.quitty(theysay)

	if len(topix)>0: # they brought up a new topic in their comment
		topic = robot.getbest(topix)
		print topic.opn()
	elif topic.is_closed(): # finished old topic and didn't bring up new one
		topic = robot.changesubject()
	else:
		robot.followup(topic, theysay)
	theysay = raw_input("> ")
