#3 5 3 and 5
firstmeow = 0

for i in range(1, 200):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzMeow")
        if firstmeow == 0:
            firstmeow = i
    elif i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz")
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print(f"Buzz")
    else:
        print(i)
print(f"Lowest FizzBuzzMeow is {firstmeow}")