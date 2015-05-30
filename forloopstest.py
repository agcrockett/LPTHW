# Nested loops
print "Nested loops"

for x in xrange(1, 11):
    for y in xrange(1, 11):
        print '%d * %d = %d' % (x, y, x*y)

# Early exit	

print "Early exit"

for x in xrange(3):
    if x == 1:
        break

# For..Else

print "For..Else"	

for x in xrange(3):
    print x
else:
    print 'Final x = %d' % (x)

# Strings as an iterable

print "Strings as an iterable"

string = "Hello World"
for x in string:
    print x

# Lists as an iterable

print "Lists as an iterable"

collection = ['hey', 5, 'd']
for x in collection:
    print x

# Lists of lists

print "Lists of lists"

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print x

# Creating your own iterable

print "Creating your own iterable"

class Iterable(object):

    def __init__(self,values):
        self.values = values
        self.location = 0

    def __iter__(self):
        return self

    def next(self):
        if self.location == len(self.values):
            raise StopIteration
        value = self.values[self.location]
        self.location += 1
        return value

# range vs xrange

print "range vs xrange"

import time

start = time.clock()
for x in range(10000000):
    pass
stop = time.clock()

print stop - start

start = time.clock()
for x in xrange(10000000):
    pass
stop = time.clock()

print stop - start

# Time on small ranges

print "Time on small ranges"

import time

start = time.clock()

for x in range(1000):
    pass
stop = time.clock()

print stop-start

start = time.clock()
for x in xrange(1000):
    pass
stop = time.clock()

print stop-start

# Your own range generator using yield

print "Your own range generator using yield"

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(1, 10, 0.5):
    print x