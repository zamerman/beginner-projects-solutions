import random

score = {"player":0, "computer":0}
playing = True

score_format = 'Player: {0} / Computer: {1}'

while playing:
    print("\nRock Paper Scissors Game\n")
    print("Pick `rock`, `paper`, or `scissors`:")

    choices = ['rock', 'paper', 'scissors']
    choices_values = {'rock':0 , 'paper':1 , 'scissors': 2}

    player_choice = input()
    player_choice_value = choices_values[player_choice]

    computer_choice = random.choice(choices)
    print("\nComputer Choice: {0}\n".format(computer_choice))
    computer_choice_value = choices_values[computer_choice]

    diff_value = player_choice_value - computer_choice_value
    if diff_value == 0:
        print('Tie')
        print(score_format.format(score["player"], score["computer"]))
    elif diff_value == 1 or diff_value == -2:
        print('Player Wins')
        score["player"] += 1
        print(score_format.format(score["player"], score["computer"]))
    elif diff_value == -1 or diff_value == 2:
        print('Computer Wins')
        score["computer"] += 1
        print(score_format.format(score["player"], score["computer"]))

    continue_game = ""
    while continue_game != "y" and continue_game != "n":
        print("\nWant to play again? (y/n)")
        continue_game = input()

    if continue_game == "n":
        playing = False
