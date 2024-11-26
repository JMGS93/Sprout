import random
min_num = 1
max_num = 100
running = True
bingo = random.randint(min_num, max_num)

while running:
    
    user = int(input("Enter your guess: "))
    if user < bingo:
            print("That's too low!")
    elif user > bingo:
            print("That's too high!")
    else:
        print(f"BINGO!\n{bingo} was the correct number!")
        play_again = input("Do you want to play again? (y/n): ").lower()
        
        if not play_again == "y":
                running = False
                print("Thanks for playing!")
        bingo = random.randint(min_num, max_num)