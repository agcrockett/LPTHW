name = 'Zed A. Shaw'
age = 35 # not a lie
imp_height = 74 # inches
imp_weight = 180 # lbs
met_height = imp_height * 2.54
met_weight = imp_weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % imp_height
print "He's %d pounds heavy." % imp_weight
print "That's about %d centimetres and %d kilograms for you antipodes." % (met_height, met_weight)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# tricky line
print "If I add %d, %d, and %d I get %d." % (age, imp_height, imp_weight, age + imp_height + imp_weight)
