import random # imports functions necessary for code

user_choice = int(input("Pick number of faces: ")) # Watch asks for user's input by initializing as only intergers


random_number = random.randint(1, user_choice)  # Watch chooses random number between 1 and user's input 

print("Random Number:", random_number) # Watch prints number 

# Things to add; gif animation, more than one dice a session, pvp 21 game where two players can roll up to 21 to win but not pass it.