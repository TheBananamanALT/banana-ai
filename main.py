import time
userInput = input("Hi! My name is BananaAI Model x35y2 (the instant text-based A.I). How are you today?: ")

if userInput == "Good" or userInput == "good" or userInput =="Nice" or userInput == "nice":
    print("That's good!")
    time.sleep(1)
userInput2 = input('How may I help today? (try something like a cake recipe)')

if userInput2 == "Cake recipe" or userInput2 == "cake Recipe" or userInput2 == "cake recipe" or userInput2 == "Cake Recipe":
   print("Try going here: https://www.rainbowtrust.org.uk/get-involved/fundraise/great-rainbow-bake/chocolate-cake-recipe?gad_source=1&gclid=EAIaIQobChMIiun-14PHhQMVEFxHAR3jIgcrEAAYASAAEgKtePD_BwE") 
   time.sleep(3)
else: print('Sorry, but I do not understand.')
