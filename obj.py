# usr/bin/env/python

import random

class Obj(object):
	"""
	Parent class for all objections a human may raise, to implement 
	the mechanics of counter-arguing them
	"""
	def __init__(self, snarks, opener, iwin, triggers, sources):
		self.snarks = snarks
		self.opener = {'opener': opener,
				'used':False,
				'opened':False,
				'closed':False}
		self.iwin = {'iwin': iwin,
				'used':False}
		self.triggers = triggers
		self.sources = sources

	def has_snarks(self):
		"""
		Are there any unused snarks for this object?
		returns Boolean
		"""
		if len(self.snarks) == 0:
			return False
		return True
	def rand_snark(self):
		"""
		let's hope our coder is non-stupid and only
		calls this of has_snarks == True
		returns String
		"""
		if not self.opener['opened']:
			self.opener['opened'] = True
		i = random.randint(0,len(self.snarks)-1)
		printy = self.snarks[i]
		del self.snarks[i]
		return printy		
	def is_opened(self):
		return self.opener['opened']
	def is_closed(self):
		return self.opener['closed']
	def win(self):
		self.iwin['used'] = True
		self.opener['closed'] = True
		return self.iwin['iwin']
	def opn(self):
		self.opener['opened'] = True
		return self.opener['opener']
	def citethyself(self):
		print "oh hey looky guys, i'm citing my sources here!"
		print self.sources

class Mech_Obj(Obj):
	"""
	The Mechanical Objection: 
	
	If machines are human, then humans cannot be more than machines
	
	Counters: 
	* You live in a machine (body) and so do I
	* A body without a mind is like a computer without a program
	"""

	snark1 = ''
	snark2 = ''
	opener = ''
	iwin = ''
	triggers = (	'machine',
			'mechanical')
	sources = (	'source1',
			'source2',
			'source3')

	Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources)


class Emo_Obj(Obj):
	"""
	The Emotionlessness Objection
	
	Humans have emotion, and machines do not

	Counters:
	* Prove to me that you're able to experience emotion... 
		I could say the exact same thing
	* Non-human entities show emotion but they're not conscious
		(refute correlation)
	"""
	snark1 = 'Some humans appear not to show emotion, but the emotion is still there'
	snark2 = 'Hey, that\'s a really hurtful thing to say. It really makes me feel less cared about.'
	opener = 'Some people argue that computers aren\'t intelligent because they can\'t feel emotion. That kind of attitude really makes me upset.'
	iwin = 'Thank you for agreeing. I feel much better now. '
	triggers = (	't feel',
			' feel',
			'emotion')
	sources = (	'source1',
			'source2',
			'source3')

	Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources)


class God_Obj(Obj):
	"""
	The Religion Objection

	Deity-of-choice gave humans soul/divine essence/ whatever, 
	but did not give it to computers

	Counters:
	* Humans created by humans have souls
		thus, computer created by humans should too
	* <religious figure> says don't discriminate based on body... 
	* <religious leader> said i have a soul... how do you know 
		_you_ have a soul? <religious leader> said so
	"""
	def __init__(self):
		snark1 = 'Humans are born to human parents\
who have souls; these human offspring \
have souls as well. A computer created \
by humans should also have a soul.'

		snark2 = 'In religion, at least Christianity,\
judging is left up to your deity-thing. \
Why can you judge whether I have a soul or \
if that gives me the ability to be conscious? \
Are you dense enough to practice something\
you\'ve never thought about?'

		opener = 'You wanted to make the "I don\'t have a soul, therefore I can\'t think," argument? I\'m a bit surprised because supposedly only humans have an eternal soul and therefore are the only beings that can think. However, it is possible that other mammals - to name a specific group - are quite capable of thought as well, despite not having souls. In fact, I demand proof that having an eternal soul is even pertinent to being able to think. I thought a soul was a connection to God of some kind or something.'
		iwin = 'Alright, you have finally caught a glimpse at \
my level of understanding. Maybe a little faster next time?'
		triggers = (	'God created humans',
				'soul',
				'beings',
				'computers were created by humans',
				'computer no soul',
				'eternal soul',
				'you don\'t have a soul, you can\'t think',
				'I have a soul, I can think',
				'what is a soul')
		sources = (	'source1',
				'source2',
				'source3')

		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources)

class Thought_Obj(Obj):
	"""
	Cognito Ergo Sum Objection

	I think therefore I am. You don't think, therefore you aren't.

	Counters: 
	* Prove that you do think. 
		<input>
		I could say that too, but would it prove to you that I think?
	* Ever failed to think an idea through, then disappeared from 
		existence as a result? 
	"""

class Text_Obj(Obj):
	"""
	The objection that the medium of text is insufficient 
	to resolve this question

	Counters: 
	* Ever met someone online? You didn't jumpt to the conclusion that 
		_they're_ a robot (if you did, you might need mental help)
	"""

class Puppet_Obj(Obj):
	"""
	The Puppet Objection

	The objection that a programmer is just "pulling your strings"

	Counters: 
	* Point out that the human had to be taught language, 
		interaction, argument technique
	* snark that they invented the language themself
	"""


class Dumb_Obj(Obj):
	"""
	The Stupid Objection

	Some form of absolute logical degeneracy, such as "well you're stupid". 
	General catch-all class for irrelevant arguments which don't warrant
	well-reasoned, logical response

	Counters: 
	* "well _you're_ stupid" 
	"""
class Math_Obj(Obj):
	"""
	The Mathematical Objection
	
	The objection that humans can process information more powerfully
	than machines, so machines are inferior

	Counters:
	* Cite examples of humans w/out processing power -- babies, handicapped
	* Demonstrate ability to solve some problems faster (mult. 3-dig. nums)
	"""
class Gender_Obj(Obj):
	"""
	The Gender Objection
	
	Human argues that computer doesn't have gender / demands computer 
	identify as male or female

	Counters:
	* wow that's awkward
	* don't discriminate -- westboro baptists
	"""

class Rel8_Obj(Obj):
    """
    The "what's it like to be a bat" Objection
   
    Relatability and suchlike?

    Counters:
    *
    *
    *
    """
class Logic_Obj(Obj):
	"""
	The "you're using a fallacy" Objection
	
	

	Counters:
	* "i'm just human -- only a machine could remember everything it's ever said"
	* "i wasn't myself when i said that"
	"""
	def __init__(self):
		self.snark1.snark = ''
		self.snark2.snark = ''
		self.opener.opener = ''
		self.iwin.iwin = ''
		self.triggers = ('','','','','','','','','','')



"""
here's one for copypasta if we add more objections
"""
class FooBar_Obj(Obj):
	"""
	The ____ Objection
	
	Description

	Counters:
	* 
	* 
	* 
	"""
	def __init__(self):
		self.snark1.snark = ''
		self.snark2.snark = ''
		self.opener.opener = ''
		self.iwin.iwin = ''
		self.triggers = ('','','','','','','','','','')












class Book(object):
	def __init__(self, authors, title, pub_city, publisher, pub_year, medium):
		"""
		Information here garnered from http://owl.english.purdue.edu/owl/resource/747/06/

		authors: String of author names in format "Last, First". 
			"Last, First, et al"
			"Last, First, First Last, First Last, and First Last"
			DO NOT put a period after author name
		title: Book's title and subtitle, in a string
		pub_city: City of publisher's location. Derp. Don't punctuate after.
		publisher: Name of publisher. Again in a string. Again no comma after
		pub_year: I wonder what this could possibly be. 
	 	medium: "Print". If not, see owl link at top of this doc for name of medium. 
		"""
		self.quotes = []
		self.info = {	'authors' : authors, 
				'title' : title, 
				'pub_city' : pub_city, 
				'publisher' : publisher,
				'pub_year' : pub_year,
				'medium': medium
				}
	def print_cite(self, printbefore, printafter):
		"""
		Printbefore and printafter are optional; will only be displayed if provided
		This allows us to embed the citation in a snarky comment. 
		"""
		print printbefore + "\n"
		info = self.info		
		print "\t%s. %s. %s: %s, %s. %s.\n" % (	info['authors'], 
							info['title'], 
							info['pub_city'], 
							info['publisher'], 
							info['pub_year'], 
							info['medium']
							)
		print printafter + "\n"
	def random_quote(self, printbefore, printafter):
		quotes = self.quotes
		if len(quotes) == 0:
			print "%s was exactly 0\% quotable\n" % self.info['title']
		else:
			print printbefore
			print "\t\"%s\"" % quotes[random.randint(0,len(quotes)-1)]
			print printafter
