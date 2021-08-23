import random
rn = random.randint(0, 100)
print("Guess a number between 0 and 100")
guesses_left=5
print("guesses left:", guesses_left)
while True:
    num=int(input("enter a number:"))
    if guesses_left>0:
       if num < rn:
        print("lesser")
        guesses_left=guesses_left-1
        print("guesses left:", guesses_left)
        continue

       elif num > rn:
        print("greater")
        guesses_left=guesses_left-1
        print("guesses left:", guesses_left)
        continue

       else:
         print("Congrats, you guessed the right number.")
         print("SCORE:", guesses_left)

         print("To try again press 'y', to exit press 'n'")
         choice = str(input("Your choice:"))
         if choice == "y":
             guesses_left = 5
             continue
         elif choice == "n":
             break


    else:
     print("You were not able to guess the number, it was:", rn)
     print("To try again press 'y', to exit press 'n'")
     choice = str(input("Your choice:"))
     if choice == "y":
       guesses_left=5
       continue
     elif choice == "n":
       break



