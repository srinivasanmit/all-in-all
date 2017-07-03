name = 'Srinivasan S. Subramanian'
age = 31 # not a lie
height = 66 # inches
weight = 81 # kgs
eyes = "black"
teeth = "white"
hair = "black"

print "Lets talk about %s" % name
print "He is %d inches tall" % height
print "He is %d kgs heavy" % weight
print "Actually that's not too heavy"
print "He has got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# this line is tricky. try to get it exactly right
print "If i add %d, %d and %d, I get %d " %(
    age, height, weight, age + height + weight)