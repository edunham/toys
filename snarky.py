# usr/bin/env/python
from obj import God_Obj
from mech import Converser

# massive pile of customization and setup... 
# may get outsourced to another fileeventually
greetings = ("hello","hi","what's up","g'day","greetings")
segues = ("","","","","")
agrees = ("sure","yes","re right","you win","i agree","absolutely","re correct","mmhmm")
disagrees = ("no","re wrong","i don't think so","but")
cite = ("cite","citation","who said","prove it")
quits = ("quit")
goodbyes = ["bye-bye", "see 'ya", "ciao"]
objections = [God_Obj(), Emo_Obj()]# Mech_Obj, Thought_Obj, Text_Obj, Puppet_Obj, Dumb_Obj, Math_Obj, Gender_Obj, Rel8_Obj, Logic_Obj
redundant = [	'That was redundant (1)',
		'That was redundant (2)',
		'That was redundant (3)',
		'That was redundant (4)',
		'That was redundant (5)']
offtopic = [	'That was off-topic (1)',
		'That was off-topic (2)',
		'That was off-topic (3)',
		'That was off-topic (4)',
		'That was off-topic (5)']
triggers = (greetings, agrees, disagrees, cite, quits)
outputs = (redundant, offtopic, goodbyes)

robot = Converser(triggers, objections, outputs, DEBUG=False)

# Ok now time for the actual program

whatnext, topic = robot.startconvo() 

while(True):

	if robot.citewanted(whatnext):
		topic.citethyself()

	if robot.quitwanted(whatnext):
		robot.saygoodbye()

	if not robot.newtopic(whatnext):
		topic = robot.followup(whatnext, topic)
	else:
		printy,topic = robot.pickreply(robot.parse(whatnext))
		print printy

	whatnext = raw_input("> ")

