from random import randint

def snake_and_ladder():
    input("Hit enter to start snake and ladder")
    position = 0 
    while(position != 100):
        input("Roll the die")
        die_value = randint(1, 6)
        check_option = randint(1, 3)
        if check_option == 1:
            print("check option : No Play")
        elif check_option == 2:
            print("check option : Ladder")
            position += die_value
        elif check_option == 3:
            print("check option : Snake")
            position -= die_value
            if position < 0:
                position = 0
        print(position)


snake_and_ladder()