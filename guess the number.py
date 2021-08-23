import random
n = random.randint(0, 100)
print("Guess a number between 0 and 100")
while True:
    num=int(input("enter a number:"))
    if num < n:
        print("lesser")
        continue
    elif num > n:
        print("greater")
        continue
    else:
        print("Congrats, you guessed the right number.")
        break
