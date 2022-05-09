import random
n = random.randint(1, 100)
#print(n)
while 1:
    guess = int(input("Input number :"))
    if guess == n:
        break
    if guess < n:
        print("Your number is too low")
    else:
        print("Your number is too high")

print (f"Well done you guessed the number, it was {n}")