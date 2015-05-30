x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# assign values to complete string y
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y 

# repeat above prints using %r/%s to call whole strings, including appended strings
print "I said: %r." % x
print "I also said: '%s'." % y 

# assign values
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print using variable and string references
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# print a string comprised of the above variables
print w + e

