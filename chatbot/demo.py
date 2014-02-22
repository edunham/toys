# usr/bin/env/python
from cite import Book

library = []

elements_moral_philosophy = Book('Rachels, James','The Elements of Moral Philosophy','New York','Random House','1986','Print')
elements_moral_philosophy.quotes.append("Philosophy is not like physics. In physics, there is a large body of established truth... Physics instructors rarely invite freshmen to make up their own minds about the laws of thermodynamics.")
elements_moral_philosophy.quotes.append("Different cultures have different moral codes. What is thought right within one group may be utterly abhorrent to members of another group, and vice versa. ")
library.append(elements_moral_philosophy)



whatnext = raw_input("what shall we have? \n")

if "demo" in whatnext:
	mycite = Book("Schmoe, Joe", "A Boring Book", "Nothingtown", "Books R Us", "2014", "Print")
	mycite.print_cite("okay fine I'll tell you the citation...", "There now you know what book it was, are you happy?")
	are_you_happy = raw_input("> ")
	if 'yes' in are_you_happy: 
		print "good, glad you liked that citation\n"
	if 'more' or 'another' in are_you_happy:
		elements_moral_philosophy.print_cite("Well then here's an even more bookish book for you: ", 
							"And it has quotes! Would you like to see one?")
		quote = raw_input(">")
		if 'yes' in quote:
			elements_moral_philosophy.random_quote("ok here's a random quote for 'ya","byebye now")
	else:
		print "well damn, maybe you should go see a shrink or something\n"	

else:
	print "if you'd asked for a demonstration, i would have given you one..."
