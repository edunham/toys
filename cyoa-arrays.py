texts = [
    "You are walking through the woods.",                   # 0
    "You see a bear! What do you do?",                      # 1
    "The bear eats you and you die.",                       # 2
    "You don't have a sandwich!",                           # 3
    "You find a sandwich!",                                 # 4
    "The bear is very angry at you for stealing its food.", # 5
    "The bear becomes your friend! You win!"                # 6
    ]

options = [
    ["ok..."],                                              # 0
    ["punch it", "give it a sandwich"],                     # 1
    [],                                                     # 2
    ["Run away!", "Look for a sandwich."],                  # 3
    ["Eat it", "Give it to the bear"],                      # 4
    ["uhoh"],                                               # 5
    []                                                      # 6
    ]

results = [
    # each result should have as many states as the corresponding options
    [1],                                                    # 0
    [2, 3],                                                 # 1
    [],                                                     # 2
    [2, 4],                                                 # 3
    [5, 6],                                                 # 4
    [2],                                                    # 5
    []                                                      # 6
    ]

playing = True
state = 0
while(playing):
    print texts[state]
    for opt in enumerate(options[state]):
        print str(opt[0]) + ' : ' + opt[1]
    if len(results[state]) > 0:
        choice = raw_input("> ")
        state = results[state][int(choice)]
    else:
        print "Game Over!"
        playing = False
