print(f"Please input first number: ")
firstterm = input() #string "15"
firstint = int(firstterm) # int 15

print(f"How many times you want to calulate: ")
lastterm = input() #string "15"
lastint = int(lastterm) # int 15

sum = 0

for i in range(lastint):
    if i%2==0 and firstint>15:
        currentterm = firstint * (-1)
        print(f"{currentterm} ", end="")
    else:
        currentterm = firstint
        if currentterm>15:
            print(f"+{currentterm} ", end="")
        else:
            print(f"{currentterm} ", end="")

    sum = sum + currentterm
    firstint = firstint + 5

print(f"Last sum:{sum}")
