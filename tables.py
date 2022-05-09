num1 = range(1,13)

for i in num1:
    for j in num1:
        if j == 1:
            print(f"--------------------\n{i} times table")
        print(f"{i} x {j} = {i * j}")