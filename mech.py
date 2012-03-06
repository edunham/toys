from cite import Book
from obj import God_Obj
import random

class Converser(object):
	def __init__(self, triggers, objections, outputs, DEBUG):
		"""
		Unpack tuple of triggers into useful little tuples... eventually
		Triggers in form: 
			- Greetings
			- Agrees
			- Disagrees
			- Cite
		outputs also a big tuple full of little lists
			- Redundant
			- Offtopic
		debug is whether we want things in debug mode
		"""
		self.DEBUG = DEBUG
		self.greetings, self.agrees, self.disagrees, self.cite, self.quits = triggers
		self.objections = objections
		self.redundant, self.offtopic, self.goodbyes = outputs

	def startconvo(self):	
		print "%s, human." % self.getrand(self.greetings) 
		topic = self.getrand(self.objections) 
		print topic.opn() 
		return (raw_input("> "), topic)

	def newtopic(self, theysaid):
		"""
		True if we should move on to a new topic.
		False if they'd still like to keep talking about the old one
		"""
		DEBUG = self.DEBUG
		if DEBUG:
			print "DEBUG: in newtopic method, they said %s" % theysaid
		for a in self.agrees:
			if a in theysaid:
				if DEBUG:
					print "DEBUG: Found %s so they agree" % a
				return False
		for d in self.disagrees:
			if d in theysaid:
				if DEBUG:
					print "DEBUG: Found %s, so they disagree" % d
				return False
		return True

	def followup(self, theysaid, topic):
		"""
		Assume that newtopic method returned False. 
		This follows up on their remark based on what's available. 
		"""
		DEBUG = self.DEBUG
		if DEBUG:
			print "DEBUG: entering followup. They said %s, topic is %s" % (theysaid, topic)
		for d in self.disagrees:
			if d in theysaid:
				if topic.has_snarks():
					if DEBUG:
						print "DEBUG: the topic has snarks"
					print topic.rand_snark()
					return topic
				else:
					if DEBUG:
						print "DEBUG: the topic has no snarks. redundant, then win."
					print self.getrand(self.redundant)
					print topic.win()
					topic = 'offtopic'
					return topic
		for a in self.agrees:
			if a in theysaid:
				if DEBUG:
					print "DEBUG: they agreed. Printing topic win."
				print topic.win()
				topic = 'offtopic'
				return topic
			

	def getrand(self, fromthese):
		"""
		mainly for redundants and offtopics
		"""
		return fromthese[random.randint(0,len(fromthese)-1)]

	def parse(self, theysaid):
		"""
		I'll only hand text to this if it looks like the human 
		might have segued to a new topic. This'll identify the topics 
		triggered by the new comment, and prep them for pickreply
		"""
		if self.DEBUG:
			print "DEBUG: entering parse method. They said %s" % theysaid
		topics = []
		for o in self.objections:
			for t in o.triggers:
				if t in theysaid:
					if self.DEBUG: 
						print "DEBUG: objection %s added by trigger %s" % (o,t)
					topics.append(o)
		return topics

	def pickreply(self, options):

		getrand = self.getrand
		DEBUG = self.DEBUG

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
						printy += getrand(self.redundant)
						printy += "\n"
						printy += o.win()
		if printy == '': # still haven't figured out what to say
			if DEBUG:
				print "DEBUG: still nothing to say. user must have been off-topic."
			printy += getrand(self.offtopic)
			topic = 'offtopic'
		return (printy, topic)

	def citewanted(self, theysaid):
		for c in self.cite:
			if c in theysaid:
				return True
		return False

	def quitwanted(self, theysaid):
		for q in self.quits:
			if q in theysaid:
				return True
		return False

	def saygoodbye(self):
		print self.getrand(self.goodbyes)
		quit()
