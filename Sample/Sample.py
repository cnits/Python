def bar():
    print "#" + 16 * "=" + "#"
def top():
    for i in range(1, 5) + range(4, 0, -1):
        #split a long line by ending it with \
        print "|" + (-2 * i + 8) * " " + \
              "<>" + (4 * i - 4) * "." + "<>" + \
              (-2 * i + 8) * " " + "|"
def bottom():
    for i in range(4, 0, -1):
        print "|" + (-2 * i + 8) * " " + \
              "<>" + (4 * i - 4) * "." + "<>" + \
              (-2 * i + 8) * " " + "|"

#main function
bar()
top()
#bottom()
bar()
print "abc"[::-1]
a = [1, 2, 3, 4]
#print " " . join(a)
