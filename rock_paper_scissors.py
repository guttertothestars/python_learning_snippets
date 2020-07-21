continue_program = True
while(continue_program):

    options = ["ROCK", "PAPER", "SCISSORS"]
    print("Let's play Rock Paper Scissors!\n")

    #Get player one input and make sure it is appropriate format
    player_one_input = input("Player One-Rock, Paper, or Scissors? ")
    player_one_input = player_one_input.upper()
    if player_one_input not in options:
        print("You a goof")

    #Get player two input and insure is is appropriate format
    player_two_input = input("Player Two-Same question! ")
    player_two_input = player_two_input.upper()
    if player_two_input not in options:
        print("You a goof")




    #while loop for player one choosing rock
    while player_one_input == "ROCK":
        if player_two_input == "ROCK":
            print("Draw!")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break
    
        elif player_two_input == "PAPER":
            print("Player Two covers for the win!")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break
    
        else:
            print("Player One smashing victory")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break

    #while loop for player one choosing paper
    while player_one_input == "PAPER":
        if player_two_input == "PAPER":
            print("draw!")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break
    
        elif player_two_input == "ROCK":
            print("Player One covers for the win!")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break
    
        else:
            print("Player Two cut chop boogaloo")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break

    #while loop for player one choosing scissors
    while player_one_input == "SCISSORS":
        if player_two_input == "SCISSORS":
            print("draw!")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break
    
        elif player_two_input == "ROCK":
            print("Player Two smashing victory!")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break

        else:
            print("Player One cutting it Close")
            continue_text = input("Would you like to continue? Y/N :")
            if(continue_text.lower() == "n"):
                continue_program = False
                break
            break

