from sys import argv

script, cnt = argv

numbers = []

def my_func(count):
    i = 0
    while i < count:
        print "At the top i is %d" % i
        numbers.append(i)

        i+=1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

my_func(int(cnt))

print "The numbers: "

for num in numbers:
    print num

for i in range(5, 11):
    print "At the top i is %d" % i
    numbers.append(i)

    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

