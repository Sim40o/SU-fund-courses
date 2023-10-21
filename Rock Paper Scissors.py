from random import randint

rock = "Rock"
paper = "paper"
scissors = "Scissors"

games = 0
wins = 0
draws = 0
loses = 0

while True:
    if games > 0 :
        print("""
If you've had [e]nough we can stop, otherwise... """)
    print ("Choose [r]ock, [p]aper or [s]cissors: " , end = "")
    player_choice = str(input())
    if games > 0 :
        if player_choice == "e":
            break
    if player_choice == "r":
        player_choice = rock
    elif player_choice == "p":
        player_choice = paper
    elif player_choice == "s":
        player_choice = scissors
    else :
        print ("Invalid input, please try again: ")
        continue

    computer_choice = randint(1,3)
    if computer_choice == 1:
        computer_choice = rock
    elif computer_choice == 2:
        computer_choice = paper
    elif computer_choice == 3:
        computer_choice = scissors
    print(f"The computer chose {computer_choice}")
    games += 1

    if player_choice == rock and computer_choice == scissors \
    or player_choice == paper and computer_choice == rock \
    or player_choice == scissors and computer_choice == paper :
        wins += 1
        print ("You win!")
    elif player_choice == computer_choice:
        draws += 1
        print ("It's a draw?!")
    else :
        loses += 1
        print ("You lost...")

print (f"""
Your performance:
Wins: {wins}
Draws: {draws}
Loses: {loses}
Bye!""")