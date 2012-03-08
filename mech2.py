from cite import Book
from obj import God_Obj, Emo_Obj, Offtopic
import random

class Converser(object):
	def __init__(self, triggers, objections, outputs, DEBUG):
		self.DEBUG = DEBUG
		self.greetings, self.agree, self.disagree, self.cite, self.quits = triggers
		self.objections = objections
		self.redundant, self.offtopic, self.movingon, self.goodbyes = outputs

	def getrand(self, fromthese):
		return fromthese[random.randint(0,len(fromthese)-1)]

	def topics_opened(self, comment):
		topix = []
		for o in self.objections:
			if o.triggered_by(comment):
				topix.append(o)
		return topix

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

	def say_hello(self):
		print "%s, human!" % self.getrand(self.greetings)
		topic = self.getrand(self.objections)
		print topic.opn()
		return topic
	def say_goodbye(self):
		print self.getrand(self.goodbyes)
		quit()
