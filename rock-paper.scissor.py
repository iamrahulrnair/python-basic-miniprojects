import random

wins=0
losses=0
ties=0

print("Hi user, please choose:\nRock-->r\nScissor-->s\nPaper-->p")
while(True):
    _choice=['r','p','s']
    user_move=input("Enter your move: ")
    ai_move=random.choice(_choice)

    if user_move=='q':
        print("Thanks for playing.")
        break
    if user_move==ai_move:
        ties+=1
    elif user_move=='r' and ai_move=='s' or user_move=='s' and ai_move=='p':
        wins+=1
    elif user_move=='p'and ai_move=='s' or user_move=='r' and ai_move=='p':
        losses+=1
    else:
        print("Please provide correct input.")
    print(f"You chose {user_move}\n AI chose {ai_move}")
    print(f"Score : Win--->{wins} Lose--->{losses} Ties--->{ties}")

    
