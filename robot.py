from mech2 import Converser

class BuildStandard(Converser):
	def __init__(self, DEBUG):
		greetings = (	"hello",
				"hi",
				"what's up",
				"g'day",
				"greetings")

		agrees = (	"sure",
				"yes",
				"re right",
				"you win",
				"i agree",
				"absolutely",
				"re correct",
				"yeah")

		disagrees = (	"no",
				"re wrong",
				"i don't think so",
				"but")

		cite = (	"cite",
				"citation",
				"who said",
				"prove it")

		quits = (	"quit", 
				"get me out of here")

		objections = [	God_Obj(), 
				Emo_Obj(),
				# Mech_Obj, 
				# Thought_Obj, 
				# Text_Obj, 
				# Puppet_Obj, 
				# Dumb_Obj, 
				# Math_Obj, 
				# Gender_Obj, 
				# Rel8_Obj, 
				# Logic_Obj
				]

		redundant = [	'That was redundant (1)',
				'That was redundant (2)',
				'That was redundant (3)',]

		offtopic = [	'That was off-topic (1)',
				'',
				'']

		movingon = [	'',
				'',
				'']

		goodbyes = [	"bye-bye", 
				"see 'ya", 
                		"ciao"]

		triggers = (greetings, agrees, disagrees, cite, quits)

		outputs = (redundant, offtopic, movingon, goodbyes)

		Converser.__init__(triggers, objections, outputs, DEBUG)

