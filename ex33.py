
numbers = []

def while_loop(range, increment):
	i = 0
	
	while i < range:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom, i is %d" % i

user_range = int(raw_input("What is your upper limit? "))
user_increment = int(raw_input("By how much would you like to increment? "))

while_loop(user_range, user_increment)

print "The numbers: "

for num in numbers:
	print num