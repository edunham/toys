# usr/bin/env/python
from cite import Book
from obj import God_Obj
import random
DEBUG = False 
greetings = ("hello","hi","what's up","g'day","greetings")
segues = ("","","","","")
agrees = ("yes","re right","i agree","absolutely","re correct","mmhmm")
disagrees = ("no","re wrong","i don't think so","but")
cite = ("cite","citation","who said","prove it")

"""
mech = Mech_Obj()
emo = Emo_Obj()
"""
god1 = God_Obj()
god2 = God_Obj()
"""
think = Thought_Obj()
txt = Text_Obj()
puppet = Puppet_Obj()
dumb = Dumb_Obj()
math = Math_Obj()
sex = Gender_Obj()
rel8 = Rel8_Obj()
log = Logic_Obj()

objections = (mech, emo, god, think, txt, puppet, dumb, math, sex, rel8, log)
"""
objections = [God_Obj(), God_Obj()]

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

def newtopic(theysaid):
	"""
	True if we should move on to a new topic.
	False if they'd still like to keep talking about the old one
	"""
	if DEBUG:
		print "DEBUG: in newtopic method, they said %s" % theysaid
	for a in agrees:
		if a in theysaid:
			if DEBUG:
				print "DEBUG: Found %s so they agree" % a
			return False
	for d in disagrees:
		if d in theysaid:
			if DEBUG:
				print "DEBUG: Found %s, so they disagree" % d
			return False
	return True

def followup(theysaid, topic):
	"""
	Assume that newtopic method returned False. 
	This follows up on their remark based on what's available. 
	"""
	if DEBUG:
		print "DEBUG: entering followup. They said %s, topic is %s" % (theysaid, topic)
	for d in disagrees:
		if d in theysaid:
			if topic.has_snarks():
				if DEBUG:
					print "DEBUG: the topic has snarks"
				print topic.rand_snark()
				return topic
			else:
				if DEBUG:
					print "DEBUG: the topic has no snarks. redundant, then win."
				print getrand(redundant)
				print topic.win()
				topic = 'offtopic'
				return topic
	for a in agrees:
		if a in theysaid:
			if DEBUG:
				print "DEBUG: they agreed. Printing topic win."
			print topic.win()
			topic = 'offtopic'
			return topic
		

def getrand(fromthese):
	"""
	mainly for redundants and offtopics
	"""
	return fromthese[random.randint(0,len(fromthese)-1)]

def parse(theysaid):
	"""
	I'll only hand text to this if it looks like the human 
	might have segued to a new topic. This'll identify the topics 
	triggered by the new comment, and prep them for pickreply
	"""
	if DEBUG:
		print "DEBUG: entering parse method. They said %s" % theysaid
	topics = []
	for o in objections:
		for t in o.triggers:
			if t in theysaid:
				if DEBUG: 
					print "DEBUG: objection %s added by trigger %s" % (o,t)
				topics.append(o)
	return topics

def pickreply(options):
	if DEBUG: 
		print "DEBUG: entering pickreply method. Options are %s" % options
	printy = ''
	for o in options:
		if not o.is_opened(): # look for a new topic
			if DEBUG: 
				print "DEBUG: found unopened option %s, adding random snark" % o
			printy += o.rand_snark()
			topic = o
			break
	if printy == '': # didn't find an unopened topic
		for o in options:
			if not o.is_closed():
				if o.has_snarks():
					if DEBUG:
						print "DEBUG: Found opened topic %s, with snarks available" % o
					printy += o.rand_snark()
					topic = o		
				else: # the topic wasn't closed, but its snarks are all used up
					if DEBUG: 
						print "DEBUG: Found not-closed topic %s, but it's out of snarks" % o
					printy += getrand(redundant)
					printy += "\n"
					printy += o.win()
	if printy == '': # still haven't figured out what to say
		if DEBUG:
			print "DEBUG: still nothing to say. user must have been off-topic."
		printy += getrand(offtopic)
		topic = 'offtopic'
	return (printy, topic)

def citewanted(theysaid):
	for c in cite:
		if c in theysaid:
			return True
	return False

def cite(topic):
	tocite = topic.getcite()
	for c in tocite:
		c.print_cite()
	
print "%s, human ." % getrand(greetings)
topic = getrand(objections)
print topic.opn()

whatnext = raw_input("> ")
while(True):
	"""
	if citewanted(whatnext):
		topic.cite()
	"""
	if not newtopic(whatnext):
		topic = followup(whatnext, topic)
	else:
		printy,topic = pickreply(parse(whatnext))
		print printy

	whatnext = raw_input("> ")
"""
if "demo" in whatnext:
	mycite = Cite("Schmoe, Joe", "A Boring Book", "Nothingtown", "Books R Us", "2014", "Print")
	mycite.print_cite("okay fine I'll tell you the citation...", "There now you know what book it was, are you happy?")
	are_you_happy = raw_input("> ")
	if 'yes' in are_you_happy: 
		print "good, glad you liked that citation\n"
	else:
		print "well damn, maybe you should go see a shrink or something\n"	

else:
	print "if you'd asked for a demonstration, i would have given you one..."
"""

