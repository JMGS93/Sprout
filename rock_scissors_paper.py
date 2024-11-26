import random 
options = ("rock", "scissors", "paper")
running = True
score1 = 1
score2 = 1
tie_score = 10
dic_puntos = [0,0]

while running:

   print("-------------")
   player = input("Enter a choice (rock, scissors, paper): ")
   print("-------------")
   computer = random.choice(options)

   while player not in options:
        print("-------------")
        print(input("Enter a choice (rock, scissors, paper): "))
        print("-------------")
   else:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("-------------")

        if player == computer:
           dic_puntos[0] = dic_puntos[0] + score1
           dic_puntos[1] = dic_puntos[1] + score2
           print("It's a tie!")
           print(f"Your score is {dic_puntos[0]}")
           print(f"Computer score is {dic_puntos[1]}")
           print(dic_puntos)
           if dic_puntos[0] >= 10 or dic_puntos[1] == 10:
               print("Its a tie!")
               print(dic_puntos)
               print("See you next time!")
               exit()
        elif player == "rock" and computer == "scissors":
            dic_puntos[0] = dic_puntos[0] + score1
            print("You win!")
            print(f"Your score is {dic_puntos[0]}")
            print(f"Computer score is {dic_puntos[1]}")
            print(dic_puntos)
            if dic_puntos[0] == 10:
               print("You win! Congrats!")
               print(dic_puntos)
               exit()
            elif dic_puntos[1] == 10:
               print("You lose!")
               print(dic_puntos)
               exit()
            else:
                pass
        elif player == "scissors" and computer == "paper":
           dic_puntos[0] = dic_puntos[0] + score1
           print("You win!")
           print(f"Your score is {dic_puntos[0]}")
           print(f"Computer score is {dic_puntos[1]}")
           print(dic_puntos)
           if dic_puntos[0] == 10:
               print("You win! Congrats!")
               print(dic_puntos)
               exit()
           elif dic_puntos[1] == 10:
               print("You lose!")
               print(dic_puntos)
               exit()
           else:
               pass
        elif player == "paper" and computer == "rock":
           dic_puntos[0] = dic_puntos[0] + score1
           print("You win!")
           print(f"Your score is {dic_puntos[0]}")
           print(f"Computer score is {dic_puntos[1]}")
           print(dic_puntos)
           if dic_puntos[0] == 10:
               print("You win! Congrats!")
               print(dic_puntos)
               exit()
           elif dic_puntos[1] == 10:
               print("You lose!")
               print(dic_puntos)
               exit()
           else:
               pass
        else:
           dic_puntos[1] = dic_puntos[1] + score2
           print("You lose!")
           print(f"Your score is {dic_puntos[0]}")
           print(f"Computer score is {dic_puntos[1]}")
           print(dic_puntos)
           if dic_puntos[1] == 10:
               print("Computer win!")
               exit()
print("-------------")