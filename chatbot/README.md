It argues about AI. Grumpily.

```
python snarky.py
```

Try to argue back!


More details:

cite.py is the machine that makes citations magically happen... in theory.
	it should probably hold the citations themselves once they get added in.

// demo.py was for testing cite.py. it's currently unused.

mech.py is the mechanics of the robot's logic. You hand it a big bundle of
	nice specific triggers, and it magics them into coherent conversational
	submission.

// obj_backup.py was apparently from before i did something that i thought might
	break obj.py. i don't think it's useful at the moment, but better
	safe than sorry...

obj.py is holds Obj, the objection parent class with all the getters and
	logic-ful loveliness that keeps me from having to poke around inside
	the individual objection objects when i want their details. it also
	has each of the specific objection classes, which aren't reeeeally
	necessary but it's easier to jam all the static conversation bits into
	a side file than mess with tweaking a bunch of Obj objects in main

robot.py holds default configs (class BuildStandard(debug)) for yer ordinary
	run-of-the-mill teacher-replacing chatbot.

snarky.py... yay! yells at mech and makes there be a robot, then pokes and prods
	at various objections. as of this writing, the triggers passed to mech.py
	are hard-coded in this file rather than over there. Makes them more
	transparent-like.
