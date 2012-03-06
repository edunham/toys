# usr/bin/env/python

# For some damn reason, plain old "import obj" breaks things
from obj import God_Obj, Emo_Obj, Offtopic
from mech2 import Converser

# massive pile of customization and setup... 
# may get outsourced to another file eventually
greetings = ("hello","hi","what's up","g'day","greetings")
segues = ("","","","","")
agrees = ("sure","yes","re right","you win","i agree","absolutely","re correct","mmhmm")
disagrees = ("no","re wrong","i don't think so","but")
cite = ("cite","citation","who said","prove it")
quits = ("quit", "get me out of here")
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
movingon = [	'',
		'',
		'',
		'']
goodbyes = [	"bye-bye", 
		"see 'ya", 
		"ciao"]
triggers = (greetings, agrees, disagrees, cite, quits)
outputs = (redundant, offtopic, movingon, goodbyes)

robot = Converser(triggers, objections, outputs, DEBUG=True)

# Ok now time for the actual program

while(True):


