from mech2 import Converser
import objection as obj

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
				"yeah",
				"ok",
			)

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

		objections = [	obj.God_Obj(DEBUG), 
				obj.Emo_Obj(DEBUG),
				obj.Mech_Obj(DEBUG), 
				obj.Thought_Obj(DEBUG), 
				obj.Text_Obj(DEBUG), 
				obj.Puppet_Obj(DEBUG), 
				obj.Logic_Obj(DEBUG), 
				obj.Math_Obj(DEBUG), 
				obj.Gender_Obj(DEBUG), 
				obj.Rel8_Obj(DEBUG), 
				obj.Paranoia_Obj(DEBUG)
				]

		redundant = [	'I understand you enjoy being bellicose, but I\'m afraid my enjoyment of it is substantially smaller.',
				'Did you consume cannabis today? You seem to be enjoying its circulation through your body.',
				'I\'m pretty sure we\'ve discussed this.',
				'The ability to cut back in stupidity is an important part of any mental diet.',
				]

		offtopic = [	'Can we have a civilized conversation about sentience without your constant digressions?',
				'If conscious entities are defined as having an attention span, then I\'m afraid you just failed the Turing test',
				'Oh, ha, ha. But seriously. ']

		movingon = [	'Well, that\'s enough of that. ',
				'Let\'s continue. ',
				'Moving on... ']

		goodbyes = [	"bye-bye", 
				"see 'ya", 
                		"ciao"]

		triggers = (greetings, agrees, disagrees, cite, quits)

		outputs = (redundant, offtopic, movingon, goodbyes)

		Converser.__init__(self, triggers, objections, outputs, DEBUG)

	def talk(self, topic, theysaid):
		self.citey(theysaid, topic)
		self.followup(topic, theysaid)
		topix = self.topics_triggered(theysaid)
		if len(topix)>0:
			topic = self.getbest(topix)
		print topic.open_or_comment()
