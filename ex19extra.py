def multiply(first_value, second_value):
	print "Your first value is %d, while your second value is %d" % (first_value, second_value)
	result = first_value * second_value
	print "By multiplying these, we get %d" % result
	
# 1. raw_input() - working (raw_input needs to be converted to integer)
# print "Simple multiplication program."
# first_user_number = int(raw_input("Enter your first number: "))
# print "Thanks."
# second_user_number = int(raw_input("Enter your second number: "))

# multiply(first_user_number, second_user_number)


# 2. input() - works only with numbers, else crashes
# print "Simple multiplication program."
# first_user_number = input("Enter your first number: ")
# print "Thanks."
# second_user_number = input("Enter your second number: ")

# multiply(first_user_number, second_user_number)

# 3. argv input / command line - Working

# from sys import argv

# script, first_user_number, second_user_number = argv

# first_user_number = int(first_user_number)
# second_user_number = int(second_user_number)

# print "Your numbers have been accepted."

# multiply(first_user_number, second_user_number)

# 4. pre-defined variables input

# 5. variable + numeric

# 6. calculation based

first_user_number = input("Enter your first number: ")
print "Thanks."
second_user_number = input("Enter your second number: ")
print "Thanks."

multiply(first_user_number + 10, second_user_number + 10)