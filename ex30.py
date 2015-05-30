people = int(raw_input("How many people are there? "))
cars = int(raw_input("How many cars? "))
buses = int(raw_input("How many buses? "))

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars or buses > people:
	print "That's a lot of buses."
elif buses < cars or (people / 4) > cars:
	print "Maybe we should take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."