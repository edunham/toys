"""
After first cutting there's A2, A3, A4, and A5. 

Expected # of times there's ONLY ONE SHEET LEFT

max # of times would be if all but A2 got used, then all but A3 got used, then
all but A4. 

Min # of times is if he always draws the largest piece, so only once will
there be a single sheet, when it's the last. 
"""
import random

class PaperDudeSim():
    def __init__(self):
        self.reset()

    def reset(self):
        self.envelope = [2, 3, 4, 5]
        self.hadJustOne = 0

    def draw(self):
        page = random.choice(self.envelope)
        self.envelope.remove(page)
        if len(self.envelope) == 0:
            self.hadJustOne += 1
        if page == 2:
            self.envelope = self.envelope + [3,4,5]
        if page == 3:
            self.envelope = self.envelope + [4,5]
        if page == 4:
            self.envelope = self.envelope + [5]
        if page == 5:
            if len(self.envelope) == 0:
                self.hadJustOne -= 1
                return False
        return True

    def run(self):
        # draw sheets till we fail
        while self.draw():
            pass

    def timesHadOne(self):
        return self.hadJustOne

def simulatePaperDudes(n):
    dude = PaperDudeSim()
    singlepages = 0.0
    for i in range(n):
        dude.run()
        singlepages += dude.timesHadOne()
        dude.reset()
    print format(singlepages/n, '.6f')

if __name__ == "__main__":


    print """I expect that the printer always grabs the largest page left,
    because it is the first one his hand comes to when he reaches into the
    envelope. Thus, the number of times which he is expected by me to find
    only a single sheet is 0.000000, since the directions said to exclude the
    final remaining A5 sheet.\n"""

    print """However, if you want to simulate a bunch of highly unrealistic
    little paper dudes who sort past a larger paper to get at a small one for
    the sake of 'randomness', here goes."""

    simulatePaperDudes(10000000)
