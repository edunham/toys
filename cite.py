# usr/bin/env/python

import random

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
