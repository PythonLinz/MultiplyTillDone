import random
import re
print ("The results of a random number times the integer value you input.")
askDirection = ""
valueInput, randomInteger = 0, 0
testForInteger, doRunFunction = True, True

def andAgain(valueInput):    
    while testForInteger:
            randomInteger = int(random.randint(1, 10))
            print ("randomly picked: ",  int(randomInteger), "x", 
            int(valueInput), "= ", int(randomInteger) * int(valueInput))
            promptTwice()
def bigAsk(askDirection):
            askDirection = input("Would you like to try again? (y/n): ")
            if (askDirection == "Y" or askDirection == "Yes" or askDirection == "y"):
                promptTwice()
                andAgain(valueInput)
            else:
                print("You decided to exit")
                exit()
def promptTwice():
            valueInput = input("Enter Integer value: ")
            testForInteger = (bool(re.match('^[0-9]+$', valueInput)))
            if(not testForInteger):
                bigAsk(askDirection)
            else:
                andAgain(valueInput)                             
if (doRunFunction):                
    promptTwice()
doRun = False
andAgain()         




