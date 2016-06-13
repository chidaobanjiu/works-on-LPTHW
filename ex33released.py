def increase_to(*args):
    top, count = args
    numbers = []
    for i in range(0, top, count):
        print "At the top i is %d" % i 
        numbers.append(i)  
	
        i+=count
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i 
		
    print "The numbers: "
    for num in numbers:
        print num ,

a = int(raw_input("The number will increase to:\n >>>"))
b = int(raw_input("and the incrementor will be:\n >>>"))

increase_to(a, b)
