#! /usr/bin/env python3

from ics import Calendar, Event
from random import randrange, choice
from datetime import timedelta, datetime
import click
import calendar
from dateutil import parser

class Pronoun:
  def __init__(self, they="they", them="them", their="their", theyre = "they're"):
    self.they = they
    self.them = them
    self.their = their
    self.theyre = theyre

def encourage(name, pn):
    encouragements = [
        f"{name} would love to hear from you",
        f"give {name} a compliment!",
        f"when did you last talk to {name}?",
        f"{name} misses you",
        f"can you make a plan with {name} today?",
        f"send {name} a cute gif",
        f"write a poem for {name}",
        f"don't just leave {name} on read",
        f"send some random emoji to {name}",
        f"ask {name} about their pets and family",
        f"what is {name} up to these days?",
        f"what's the best book that {name} has read lately?",
        f"what's {name}'s favorite movie this year?",
        f"quick, draw {name} from memory!",
        f"You have been selected for the Talk To {name} Challenge",
        f"Welcome to {name}'s World of Tomorrow, where we chat more often",
        f"{name}. {pn.theyre} pretty great.",
        f"{name}-{name}-{name}, {name}, {name}-{name}",
        f"{name} means so much to you that you wrote a computer program to remind {pn.them} that you love t{pn.them}",
        f"{name} thought about you today",
        f"{name} would be pleasantly surprised if you reached out",
    ]
    output = choice(encouragements)
    return output

def pronounulate(name):
    if name[-1:] in ['a', 'e', 'i', 'o', 'u', 'y']:
        return Pronoun("she","her","her", "she's") 
    else:
        return Pronoun("he","him","his", "he's") 


@click.command()
@click.option("--start", "-s", default=str(datetime.now()), help="earliest permissible reminder, datetime")
@click.option("--duration", "-d", default=365, help="days past start of last permissible reminder")
@click.option("--recipients", "-r", multiple=True, default=["someone"], help="names of people to be reminded about")
@click.option("--prompts", "-p", default=52, help="number of reminders about each person to place on calendar" )
@click.option("--filename", "-f", default="output.ics", help="filename to write calendar")
@click.option("--endnag", "-e", default=True, help="whether to place a renewal reminder at the end of the calendar")
@click.option("--guesspn", "-g", default=False, help="Guess pronouns. Badly.")
def caladornication(start, duration, recipients, prompts, filename, endnag, guesspn):
    """
    This script generates a .ics file of random reminders to talk to people you care about. 
    
    """
    url="https://github.com/edunham/toys/tree/master/ics/myics.py"
    c = Calendar()
    start = parser.parse(start)
    duration = timedelta(days=duration)
    for recipient in recipients:
        pronoun = Pronoun()
        if guesspn:
            pronoun = pronounulate(recipient)
        for i in range(prompts):
            e = Event()
            txt = encourage(recipient, pronoun)
            e.name = f"{txt} (#{i})"
            e.begin = start + timedelta(days=randrange(duration.days))
            e.make_all_day()
            c.events.add(e)

    if endnag: 
        e = Event()
        reciplist = " and ".join(recipients)
        totalreminds = len(recipients) * prompts
        prettyduration = duration.days
        prettystart=start.strftime("%b %d, %Y")
        txt = f"On {prettystart}, you ran {url} and created {totalreminds} reminders over {prettyduration} days, telling you to interact with {reciplist}. They are now finished. Would you do it all again?"
        e.name = txt
        e.begin = start + duration
        e.make_all_day()
        c.events.add(e)
    with open(filename, "w") as cal:
        cal.writelines(c)


if __name__ == '__main__':
    caladornication()
