import random

class Converser(object):
	def __init__(self, triggers, objections, outputs, DEBUG):
		self.DEBUG = DEBUG
		self.greetings, self.agree, self.disagree, self.cite, self.quits = triggers
		self.objections = objections
		self.redundant, self.offtopic, self.movingon, self.goodbyes = outputs

	def getrand(self, fromthese):
		return fromthese[random.randint(0,len(fromthese)-1)]

	def topics_triggered(self, comment):
		if self.DEBUG:
			print "DEBUG: in topics_triggered w/ comment '%s'" % comment
		topix = []
		for o in self.objections:
			if self.DEBUG:
				print "DEBUG: objection %s" % o
			if o.triggered_by(comment):
				if self.DEBUG: 
					print "DEBUG: %s was triggered, appending" % o
				topix.append(o)
		if self.DEBUG:
			print "DEBUG: finishing with topics_triggered, returning topix %s" % topix
		return topix

	def citey(self, theysaid, topic):
		for c in self.cite:
			if c in theysaid:
				print topic.citethyself()
				return

	def followup(self, topic, theysaid):
		if self.DEBUG: 
			print "DEBUG: in followup, topic %s, they said %s" %(topic, theysaid)
		if not self.agrees(theysaid):
			if not self.disagrees(theysaid):
				print self.getrand(self.offtopic)
			# trytosnark being implemented, needs getrand access
			if topic.has_snarks():
				print topic.rand_snark()
			else:
				print self.getrand(self.redundant)
				print topic.win()
			return
		else:
			print topic.win()
			return

	def getbest(self, topix):
		good = []
		ok = []
		for t in topix:
			if not t.is_opened():
				good.append(t)
			elif not t.is_closed():
				ok.append(t)
		if len(good)>0:
			return self.getrand(good)
		if len(ok)>0:
			return self.getrand(ok)
		self.say_goodbye()

	def agrees(self, comment):
		for a in self.agree:
			if a in comment:
				return True
		return False

	def disagrees(self, comment):
		for d in self.disagree:
			if d in comment:
				return True
		return False

	def quitty(self, theysaid):
		for q in self.quits:
			if q in theysaid:
				self.say_goodbye()

	def say_hello(self):
		print "%s, human!" % self.getrand(self.greetings)
		topic = self.getrand(self.objections)
		print topic.opn()
		return topic

	def say_goodbye(self):
		print self.getrand(self.goodbyes)
		quit()

	def changesubject(self):
		newtopic = self.getbest(self.objections)
		if self.DEBUG:
			print "DEBUG: in changesubject, new topic is %s" % newtopic
		if newtopic.is_closed():
			self.say_goodbye()
		print newtopic.open_or_comment()
		return newtopic
