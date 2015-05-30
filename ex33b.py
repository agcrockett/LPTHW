
numbers = []


def for_loop(input_range, input_increment):
	i = 0
	for i in range(0, input_range):
		print "i is now %s" % i
		numbers.append(i)
		
		i = i + input_increment
		print "Numbers now: ", numbers
		print "After this loop, i is now %s" % i

user_range = int(raw_input("What is your upper limit? "))
user_increment = int(raw_input("By how much would you like to increment? "))

for_loop(user_range, user_increment)

print "The numbers: "

for num in numbers:
	print num