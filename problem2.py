"""
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hi-
score whenever the game() function breaks the Hi-score.
"""
import random

def game():
    
    print("\nComputer is choosing your score based on your luck...")
    score = random.randint(1,100)
    print(f"Your Score is {score}")

    with open("Hi-score.txt", "r") as f:
        highscore = f.read()
        if highscore=="":
            highscore=0
        else:
            highscore=int(highscore)
        print(f"Last High Score was {highscore}")

    #RESETING THE SCORE
    if score==100:
        with open("Hi-score.txt","w") as f:
            f.write("0")
        highscore=0
        print("""MAX SCORED REACHED
RESETING THE HIGH SCORE TO ZERO\n""")
            
    #CONDITIONS
    elif score>highscore:
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
        print(f"Yeyyyyyy, New High Score is {score}\n")
    elif score==highscore:
        print("Same as High Score\n")
    else:
        print("Bad luck :( \n")
   
game()