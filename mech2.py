from cite import Book
from obj import God_Obj, Emo_Obj, Offtopic
import random

class Converser(object):
	def __init__(self, triggers, objections, outputs, DEBUG):
		self.DEBUG = DEBUG
		self.greetings, self.agrees, self.disagrees, self.cite, self.quits = triggers
		self.objections = objections
		self.redundant, self.offtopic, self.movingon, self.goodbyes = outputs

	def getrand(self, fromthese):
		return fromthese[random.randint(0,len(fromthese)-1)]

