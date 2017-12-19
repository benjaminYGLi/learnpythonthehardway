my_name = 'Benjamin Li'
my_age = 35
my_height = 172
my_weight = 74
my_eyes = 'Grown'
my_teeth = 'White'
my_hair = 'Black' # almost

print "Let's talk about %r." % my_name
print "He is %d cm tall." % my_height
print "He is %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He is got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the tea." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight,
        my_age + my_height + my_weight)
