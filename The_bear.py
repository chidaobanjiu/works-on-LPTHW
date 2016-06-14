def end(why):
    print "the game is over:",why
    
def dinner():
    print "---------------"
    print "You are having dinner with the bear."
    print "But there is nothing on the table."
    print "And you look at the bear."
    print "Find him smiling at you like he always do."
    end("I think the bear will enjoy his dinner.")

def house():
    print("Here you are in the bears house.")
    print("You have three boxes that the bear wants you to choose.\n 1 2 3")
    box = raw_input("Your choice is:")
	
    if int(box) == 1:
	    print "You get a jar of honey."
	    end('"It\'s a pleasure to meet you."')
    elif int(box) == 2:
    	print "You get the chance to have dinner with him."
        dinner()
    elif int(box) == 3:
	    print "You have to answer an qusetion to leave."
	    print "The answer for 123456*654321= is:"
	    answer = raw_input(">")
		
	    if answer == "807801805365":
	        print "You must be a genius. I love geniu's brain."
	        end("Your brain will be his dinner!")    
	    else :
		    print "It's ok that you are not so good at math"
		    end("You will never meet him again.")
   
    else :
		print "It's ok that you are not so good at math"
		end("You will never meet him again.")

		

		
		
def choose():
    choose = raw_input("Yes or No?\n>")
    if choose == "yes":
	    house()
    elif choose == "no":
	    end("The bear feels sorry but he believe there will be another time.\n end")
    else:
	    print("Just yes or not.")
	    choose()
		
def start():
    print "It's a beautiful day."
    print "You are walking in a national park."
    print "Suddenly, a bear walking out of the woods."
    print "What do you do? run or wait?"
	
    choice = raw_input("Your choice is:")
    
    if "run" in choice:
	    print "The bear run after you and he's faster than you..."
	    end("I'm sorry for your choice.")
    elif "wait" in choice:
	    print "The bear walk to you with a smile on his face."
	    print "He speaks English!"
	    print "And he asks if you wanna come to his house."
	    choose()
    else :
	    end("Don't do that next time you meet a bear.")
		
start()
