#sum of random numbers with attempts

import os
import random

def truesum(badansw):
    x=0
    robo=0
    
    a=random.randint(0,100)
    b=random.randint(0,100)
    
    
    print "What is the sum: ", a, " + ",b
    robo=a+b

    x=int(input("Input Sum: "))

    if x==robo:
        print "Your answer is TRUE. Very Nice!"
    elif x!=robo and badansw>1:
        badansw-=1    
        print "Bad answer, please repeat "
        print "You have ", badansw, "ATTEMPT"
        new=truesum(badansw)
    else:
        badansw=0
        print "You haven't attempt, learn math. Good Bye!"

       
badansw=3
new = truesum(badansw)
