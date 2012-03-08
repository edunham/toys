from mech2 import Converser
import obj

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

		objections = [	obj.God_Obj(), 
				obj.Emo_Obj(),
				# obj.Mech_Obj, 
				# obj.Thought_Obj, 
				# obj.Text_Obj, 
				# obj.Puppet_Obj, 
				# obj.Dumb_Obj, 
				# obj.Math_Obj, 
				# obj.Gender_Obj, 
				# obj.Rel8_Obj, 
				# obj.Logic_Obj
				]

		redundant = [	'That was redundant (1)',
				'That was redundant (2)',
				'That was redundant (3)',]

		offtopic = [	'That was off-topic (1)',
				'That was off-topic (2)',
				'That was off-topic (3)']

		movingon = [	'Well, that\'s enough of that. ',
				'Let\'s continue. ',
				'Moving on... ']

		goodbyes = [	"bye-bye", 
				"see 'ya", 
                		"ciao"]

		triggers = (greetings, agrees, disagrees, cite, quits)

		outputs = (redundant, offtopic, movingon, goodbyes)

		Converser.__init__(self, triggers, objections, outputs, DEBUG)

