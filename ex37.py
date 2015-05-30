## Keywords to learn http://www.tutorialspoint.com/python/

# assert - done

# def KelvinToFahrenheit(Temperature):
	# assert (Temperature >= 0), "Colder than absolute zero!"
	# return ((Temperature-273)*1.8)+32
	
# print KelvinToFahrenheit(273)
# print int(KelvinToFahrenheit(505.78))
# print KelvinToFahrenheit(-5)

#####################################################################

## Exception Handling

# except 

# try

# raise

# finally

# try:
	# fh = open("testfile", "w")
	# try:
		# fh.write("This is my test file for exception handling!")
	# finally:
		# print "Going to close the file"
		# fh.close()
# except IOError:
	# print "Error: can\'t find file or read data"

# def temp_convert(var):
	# try:
		# return int(var)
	# except ValueError, Argument:
		# print "The argument does not contain numbers\n", Argument
# temp_convert("xyz");

#####################################################################

# continue - ignore the rest of the loop for a given iteration

# for letter in 'Python':
	# if letter == 'h':
		# continue
	# print 'Current Letter :', letter

# var = 10
# while var > 0:
	# var = var - 1
	# if var == 5:
		# continue
	# print 'Current variable value :', var
# print 'Good bye!'

# exec

# exec 'print 5'

# exec 'if True: print 6'

# is

# a = 500
# b = 500
# a == b # True
# a is b # False

# lambda

# sum = lambda arg1, arg2: arg1 + arg2;

# print "Value of total : ", sum(10, 20)
# print "Value of total : ", sum(20, 20)

# pass

# for letter in 'Python':
	# if letter == 'h':
		# pass
		# print "This is pass block!"
	# print 'Current letter ;', letter
	
# print "Good bye"

# with

# with open('output.txt', 'w') as f:
    # f.write('Hi there!')

# yield

