import random
import re
print ("The results of a random number times the integer value you input.")
ask = ""
def andAgain():
    y = input("Enter a value: ")
    test = (bool(re.match('^[0-9]+$', y)))
    if(not test) :
        ask = input ("Want to go again: Y(es) or N(o)?")
        bigAsk(ask)
    else: 
        while test :
            x = int(random.randint(1, 10))
            print ("randomly picked: ",  x)
            results = x * int(y)
            print ("times", y, "is: ", results)
            y = input("Enter a value: ")
            test = (bool(re.match('^[0-9]+$', y)))
            if(not test) :
                ask = input ("Want to go again: Y(es) or N(o)?")
                bigAsk(ask)
def bigAsk(ask):
            if (ask == "Y" or ask == "Yes" or ask == "y") :
                andAgain()
            else :
                print("You decided to exit")
                exit            
andAgain()        




