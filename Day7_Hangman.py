import random
words=["Werewolf","Vampire","Mormon","Dracula","Displeased","Tiramisu","Tropical","Pacific","Gorgyle","Spinster","Vintage","Protest",
      "Quit","Indigo","Parsley","Mint","Victory","Nike","Athens"]
answer=random.choice(words).lower()
print (answer)
printableAns=["_"]*len(answer)
strike = 5
hangman_stages = [
"""
   -----
   |   |
       |
       |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
       |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
   |   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\\  |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
---------
"""
]
guess=set()
while "_" in printableAns and strike>0:
    c=input("Please enter your guesses").lower()
    if len(c)>1 or not c.isalpha:
        print("Please only enter one alphabet at a time")
        continue
    if c in guess:
        print("Already guessed")
        continue
    else:
        guess.add(c)
    if c in answer:
        for i in range(0,len(answer)):
            if answer[i]==c:
                printableAns[i]=c
    else:
        print("Wrong guess!!")
        strike-=1
    print(hangman_stages[5-strike])
    print("".join(printableAns))

if "_" not in printableAns and strike>0:
    print("Congratulations, you won !!!")
    
else:
    print("You have exhausted your lives. Better luck next time")
 
    