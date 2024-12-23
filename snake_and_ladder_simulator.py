from random import randint

def snake_and_ladder():
    input("Hit enter to start snake and ladder")
    player_one_die_count = 0
    player_one_position = 0
    player_two_die_count = 0
    player_two_position = 0
    while(True):
        input("Player 1 : Roll the die")
        player_one_die_count += 1
        die_value = randint(1, 6)
        check_option = randint(1, 3)
        if check_option == 1:
            print("check option : No Play")
        elif check_option == 2:
            print("check option : Ladder")
            if player_one_position + die_value <= 100:
                player_one_position += die_value
                if player_one_position == 100:
                    break
        elif check_option == 3:
            print("check option : Snake")
            player_one_position -= die_value
            if player_one_position < 0:
                player_one_position = 0
        print(f"Player 1 Position : {player_one_position}", end="\n\n")

        input("Player 2 : Roll the die")
        player_two_die_count += 1
        die_value = randint(1, 6)
        check_option = randint(1, 3)
        if check_option == 1:
            print("check option : No Play")
        elif check_option == 2:
            print("check option : Ladder")
            if player_two_position + die_value <= 100:
                player_two_position += die_value
                if player_two_position == 100:
                    break
        elif check_option == 3:
            print("check option : Snake")
            player_two_position -= die_value
            if player_two_position < 0:
                player_two_position = 0
        print(f"Player 2 Position : {player_two_position}", end="\n\n")
    
    if player_one_position == 100:
        print("Player one won")
        print(f"Die count : {player_one_die_count}")
    else:
        print("Player two won")
        print(f"Die count : {player_two_die_count}")

snake_and_ladder()