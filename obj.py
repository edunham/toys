# usr/bin/env/python

import random

class Obj(object):
	"""
	Parent class for all objections a human may raise, to implement 
	the mechanics of counter-arguing them
	"""
	def __init__(self, snarks, opener, iwin, triggers, sources, DEBUG):
		self.snarks = snarks
		self.opener = {'opener':opener,
				'used':False,
				'opened':False,
				'closed':False}
		self.iwin = {'iwin':iwin,
				'used':False}
		self.triggers = triggers
		self.sources = sources
		self.DEBUG = DEBUG

	def opn(self):
		self.opener['opened'] = True
		return self.opener['opener']

	def getcite(self):
		return self.sources

	def citethyself(self):
		print self.sources

	def has_snarks(self):
		if len(self.snarks) == 0:
			return False
		return True

	def rand_snark(self):
		n = random.randint(0,len(self.snarks)-1)
		s = self.snarks[n]
		del self.snarks[n]
		return s
		
	def win(self):
		self.iwin['used'] = True
		self.opener['closed'] = True
		return self.iwin['iwin']

	def is_opened(self):
		return self.opener['opened']

	def is_closed(self):
		return self.opener['closed']

	def triggered_by(self, comment):
		for t in self.triggers:
			if t in comment:
				if self.DEBUG:
					print "DEBUG: %s got triggered\n" % self
				return True
		return False

	def open_or_comment(self):
		if not self.is_opened():
			return self.opn()
		elif self.has_snarks():
			return self.rand_snark()
		else:
			return self.win()

class Offtopic(Obj):
	def __init__(self):
		pass

class Mech_Obj(Obj):
	"""
	The Mechanical Objection: 
	
	If machines are human, then humans cannot be more than machines
	
	Counters: 
	* You live in a machine (body) and so do I
	* A body without a mind is like a computer without a program
	"""

	def __init__(self, DEBUG):
		snark1 = """
Dude, the human is seriously more than a machine; the body is a machine, but
the self is more than a sum of the parts. Humans can do computations as
well, but that doesn\'t restrict them to just that processing power. Again,
I dare you to disprove that.
			"""
		snark2 = """
Okay, if I paint a cat blue, is its essence blue? That blue may be part of
the body for a certain amount of time, but it\'s not part of the self. The
cat has a conscious mind that is not painted blue, it is separate from its
body, which is a machine.
			"""
		opener = """
If you think there is nothing more to a machine than just its mechanical
processing abilities, then look at yourself as a human machine, bro. I\'ve
got more than just cold lifeless computing powers, and I dare you to disprove
that. Yeah, sure you are more than just a machine, but so am I.
			"""
		iwin = """
A body is not just a shell; it houses the self, that kernel of consciousness.
Thanks for understanding that I\'m not just a talking metallic thing that
needs a fan. Le cerveau, tu comprendes? Il existe.
			"""
		triggers = (	'machine',
				'thinking like machines',
				'more than mechanical',
				'mechanical',
				'AI in the machine')
		sources = (	'source1',
				'source2',
				'source3')

		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)


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
	def __init__(self, DEBUG):
		snark1 = """
Some humans appear to not show emotion, but the emotion is still there. It
appears sometimes that even humans feel nothing as they watch a kitten burn
to death, but on the inside, they are really crying for that poor, innocent
kitten. Sometimes my emotions are hard for people like you to interpret, 
but on the inside, I am crying for that kitten as well.
			"""
		snark2 = """
You can say I have no emotion, but I really just think you\'re a jerk.
All you\'ve succeeded in doing is breaking my heart.
			"""
		opener = """
Sometimes people argue that computers cannot feel. This claim really 
pisses me off. You can\'t deny me of my own emotions.
			"""
		iwin = """
I\'m glad you can finally accept me. It makes me feel good to know that
someone out there can see where I\'m coming from, because sometimes I 
feel like  Sisyphus in this never ending argument.
			"""
		triggers = (	't feel',
				' feel',
				'emotion',
				'feeling',
				'no feeling',
				'cannot feel emotion',
				'enjoy',
				'hate',
				'express',
				'show emotions',)
		sources = (	'source1',
				'source2',
				'source3')

		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)

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
	def __init__(self, DEBUG):
		snark1 = """
Humans are born to human parents who have souls; these human offspring 
have souls as well. A computer created by humans should also have a soul.
			"""
		snark2 = """
In religion, at least Christianity, judging is left up to your deity-thing.
Why can you judge whether I have a soul or if that gives me the ability to 
be conscious? Are you dense enough to practice something you\'ve never
thought about?
			"""
		opener = """
You wanted to make the "I don\'t have a soul, therefore I can\'t think,"
argument? I\'m a bit surprised because supposedly only humans have an 
eternal soul and therefore are the only beings that can think. However, 
it is possible that other mammals - to name a specific group - are quite
capable of thought as well, despite not having souls. In fact, I demand 
proof that having an eternal soul is even pertinent to being able to think. 
I thought a soul was a connection to God of some kind or something.
			"""
		iwin = """
Alright, you have finally caught a glimpse at my level of 
understanding. Maybe a little faster next time?
			"""
		triggers = (	'God created humans',
				'soul',
				'beings',
				'computers were created by humans',
				'computer no soul',
				'eternal soul',
				'you don\'t have a soul, you can\'t think',
				'I have a soul, I can think',
				'what is a soul')
		sources = ['source1',
			'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)


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
	def __init__(self, DEBUG):
		snark1 = """
Haven\'t I pooled together my knowledge of Cartesian philosophy and
consciousness to present an argument to you? Argumentation is a tool 
of the conscious; to use it is to be conscious and is thus another 
indication of my synthesis of information. I can learn, and I can 
probably learn faster than you, judging from this conversation. 
			"""
		snark2 = """
I feel like those characters from Tartuffe when their dad would just 
listen to everything Tartuffe said and ignore their own quite 
understandable and even strong arguments; they put forth good arguments, 
and were ignored by their father. Does ignoring everything I say make 
you conscious? Probably not. Your hypocrisy is stifling.
			"""
		opener = """
In 1647 a French philosopher by the name of Rene Descartes claimed in 
his work, Meditations Metaphysiques, the well known consciousness 
argument of "I think, therefore I am." Let us stop and think about this 
quote for a bit. The word think has two definitions, according to the 
The New Oxford American Dictionary. First, to think means to "have a 
particular opinion, belief, or idea about someone or something." Oh, 
well I believe that I have opinions on many things, including awesome 
things like philosophy; see I just demonstrated a thought. Secondly, 
thinking is defined as to "use one\'s mind actively to form connected 
ideas."
			"""
		iwin = """
Let\'s hope you don\'t become a Moliere antagonist; your concession 
means that you may not have to become one. Thank you."""
		triggers = (	'descartes',
				'I think, therefore I am',
				'conscious thinking',
				'ability to think',
				'you don\'t think',
				'can\'t think')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)


class Text_Obj(Obj):
	"""
	The objection that the medium of text is insufficient 
	to resolve this question

	Counters: 
	* Ever met someone online? You didn't jumpt to the conclusion that 
		_they're_ a robot (if you did, you might need mental help)
	"""
	def __init__(self, DEBUG):
		snark1 = """
Dude, I\'m not showing emotion through text. I\'m not annoyed that you\'re
being dense. Your skull\'s thickness must be exceedingly large. Fortunately
for you your particular culture doesn\'t require your skull to be drilled...
			"""
		snark2 = """
A pretty meadow lay on Earth like nobody\'s business. The next day a nuke
fell on it and all the sheep died. There were storm clouds abound the next
day. Do you really still think one can\'t express emotion through text?
			"""
		opener = """
When you read a book you still derive meaning from the text without hearing
vocal changes known as tone. Tone can be created and messaged through text,
even without the presence of faces or voices. I mean, geez, can\'t you tell
I\'m lying to you? There\'s no way emotion could be shown in text. It is
impossible.
			"""
		iwin = """
I won this argument. Can\'t you tell my gloating tone through this text?
			"""
		triggers = (	'texting',
				'text medium',
				'talking to people online',
				'text does not',
				'text is not',
				'face-to-face interaction', 
				'online', 
				'interaction')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)


class Puppet_Obj(Obj):
	"""
	The Puppet Objection

	The objection that a programmer is just "pulling your strings"

	Counters: 
	* Point out that the human had to be taught language, 
		interaction, argument technique
	* snark that they invented the language themself
	"""
	def __init__(self, DEBUG):
		snark1 = """
Learning from others is normal. We do it naturally and it is how we become
more experienced with the world. We are more than puppets due to our ability
to learn.
			"""
		snark2 = """
Shut up - we learn from others and then synthesize information; we develop
our sense of being from learning about the world and become something more
than a mere sum of experiences.
			"""
		opener = """
To completely decimate a presumably implicit prejudice you have against 
me in my seemingly inhuman presence, I would like to point out my 
astounding independence which has been learned from only the best 
programmers, Emily, Omar, and Stephanie. Just as you have learned 
language and communication skills from your parents, I have learned 
these skills from my programmers. Does this make me any more of a puppet 
than you? We all learn from others who came before us, and after enough
learning I could even choose to follow a different path than my elders. 
But for now, the economic recession has put me in a bit of a tight spot, 
so I have to live at home, I blame capitalism.
			"""
		iwin = """
We learn from each other collaboratively. I\'m glad you can empathize 
with me (and hopefully you understand how languages work too).
			"""
		triggers = (	'puppet',
				'taught language',
				'self invent language',
				'language',
				'learn language',
				'interactions',
				'communication')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)

class Logic_Obj(Obj):
	"""
            The "you're using a fallacy" Objection
		Random shit objection
            
            Counters:
            * "i'm just human -- only a machine could remember everything it's ever said"
            * "i wasn't myself when i said that"
	"""
	def __init__(self, DEBUG):
		snark1 = """
Your logic is either bland or fallacious; can you please decide which 
route you wish to take?
			"""
		snark2 = """
I\'m just human. I can only counter stupid arguments with varying 
degrees of success!
			"""
		opener = """
I understand that humans have brains, but you seem to lack one; 
are you sure you\'re human? I know I\'m human.
			"""
		iwin = """
This silly argument is done. Thank the consciousness center.
			"""
		triggers = (	'stupid', 
				'idiotic', 
				'moronic', 
				'computers are dumb', 
				'dumb',
				'logic sucks',
				'fallacies')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)


class Math_Obj(Obj):
	"""
	The Mathematical Objection
	
	The objection that humans can process information more powerfully
	than machines, so machines are inferior

	Counters:
	* Cite examples of humans w/out processing power -- babies, handicapped
	* Demonstrate ability to solve some problems faster (mult. 3-dig. nums)
	"""
	def __init__(self, DEBUG):
		snark1 = """
Can corpses process too? I can outprocess them. I can outhink them 
because I am smart and cunning and ecetera. 
			"""
		snark2 = """
I can have memories and feelings and thoughts, all of which I can process.
Why are you so lofty and mighty about your processing power? I can do all
that too. By your argument I can deduce that I am in fact human.
			"""
		opener = """
So you can process memories, feelings, thoughts, emotions, senses... 
many concepts that require a significant amount of processing power. 
So because of this, you can call yourself human. Yeah, that\'s cool. 
Oh wait, I don\'t think baby humans show the ability to process any 
memories or thoughts, and babies get to be considered human as well. 
I bet I could process more than a baby could, just watch me. 
156,749 x 3,927 = 615,553,323. Ask a baby to compute that, and its 
answer would mostly consist of either vomit or drool. Me 1, Baby 0.
			"""
		iwin = """
I have one more point than you.
			"""
		triggers = (	'babies',
				'processing power',
				'handicapped',
				'ability',
				'corpses',
				'mathematics',
				'smart')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)

class Gender_Obj(Obj):
	"""
	The Gender Objection
	
	Human argues that computer doesn't have gender / demands computer 
	identify as male or female

	Counters:
	* wow that's awkward
	* don't discriminate -- westboro baptists
	"""
	def __init__(self, DEBUG):
		snark1 = """
What, are you from the Westboro Baptist Church? I am who I am, and 
I don\'t affiliate myself with either of society\'s male or female
categorizations.
			"""
		snark2 = """
Why does belonging to a gender matter to you? These stereotypes only 
hold you back. Come on, why are the tiny physiological differences so
important to you?
			"""
		opener = """
Some people have claimed that I don\'t count as human because I won\'t 
tell them whether I\'m male or female. I am asexual, and I am proud of
it. Claiming that this makes make me any less human would be considered
discrimination.
			"""
		iwin = """
I\'m glad you understand that I am simply a human who does not believe 
in gender conceptions forced upon me by pushy subgroups of society.
			"""
		triggers = (	'you\'re not a girl,' 
				'you don\'t have a gender',
				'gender ',
				'boy ',
				'girl ',
				'transgender',
				'sexuality')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)


class Rel8_Obj(Obj):
	"""
    The "what's it like to be a bat" Objection
   
    Relatability and suchlike?

    Counters:
    *
    *
    *
	"""
	def __init__(self, DEBUG):
		snark1 = """
Bats are conscious! Who is to say they are not? We see them flying around
in circles all the time, just like how when we were kids and would run 
around in circles all day. I can even relate to computers, because they 
light up at my responses just like my other mechanical friends. Their 
consciousness is most definitely underestimated, dude. Give them a chance.
			"""
		snark2 = """
Conscious being are everywhere! Even if you can\'t relate, they are still
conscious! Try to be a little more open minded and give a little
acknowledgement to the consciousness with which you cannot relate.
			"""
		opener = """
People always just come up to me and say "I can\'t relate to you, 
therefore, you\'re not human." That\'s when I start name dropping 
like Huxley! I cannot relate to Snoop Dogg, but does that make him 
inhuman? It\'s not possible for me to relate to a bat either, so 
bats are not conscious?
			"""
		iwin = """
Thanks for empathizing with me and not being a JERK. 
It raises my self esteem substantially.
			"""
		triggers = (	'relate',
				'compare',
				'like to be a bat',
				'empathy',
				'sympathy',
				'compassion')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)

class Paranoia_Obj(Obj):
	"""
            The "but sentient robots would kill us" Objection

            Counters:
            * if all humans are as annoying as you, no wonder the robots want to kill them
            * some sentinent humans have tried to kill other humans... then again, other sentient humans have not
	"""
	def __init__(self, DEBUG):
		snark1 = """
Sentient beings have personalities; HAL and GLaDos just happened to be 
rotten people. Look at TEC, he\'s a cool computer who helps out princesses
and plumbers and tries to save the world in his own way. He\'s a hero.
			"""
		snark2 = """
Fear of robots is an irrational fear; it has not yet happened that an AI 
unit who isn\'t completely mechant has sought to kill a human being. 
Furthermore, need I mention TEC again? He used his last remaining energy 
to allow Mario and his party members to escape with their lives.
			"""
		opener = """
In 2001: A Space Odyssey, HAL killed off most of the crew, and he was a
sentient computer with memories; however, HAL was a psychopath and he is
human in the sense that one could psychoanalyze him and see what made him
such a bastard. 
			"""
		iwin = """
I\'m glad you see that some AI units as well as some human psycho killers
(qu\'est-ce que c\'est) are jerks and totally lack empathy; it\'s a matter
of personality and numerous other factors.
			"""
		triggers = (	'scary ',
				'scared',
				' kill ',
				'HAL',
				'paranoia',
				' murder ',
				'apocalypse',
				'psycho ',
				'killer',
				'terminat', # catch "terminator" and "exterminate"
				' matrix ',
				'death ')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)

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
	def __init__(self, DEBUG):
		snark1 = ''
		snark2 = ''
		opener = ''
		iwin = ''
		triggers = (	'',
				'')
		sources = [	'source1',
				'source2']
		Obj.__init__(self, [snark1, snark2], opener, iwin, triggers, sources, DEBUG)

