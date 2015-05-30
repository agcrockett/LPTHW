# import argument vector function from sys module
from sys import argv

# categorise necessary variables for argv
script, filename = argv

# create a variable named txt and store the contents of the file opened inside
txt = open(filename)

# give user feedback on what file was opened, then read and print the 
# contents of the variable txt
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# ask the user to type the filename a second time and accept input
#print "Type the filename again:"

# store user input in a new variable, as opposed to requiring it in
# the initial argv request
#file_again = raw_input("> ")

# open the contents of the new file and store to a new variable
#txt_again = open(file_again)

# read and print the contents of this file
#print txt_again.read()

