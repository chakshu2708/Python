number = int(input("Enter the Natural Number: "))

for j in range(1, number +1):
    a = []

    for i in range(1, j+1):
        print(i, sep=" ", end=" ")
        if(i<j):
            print("+", sep=" ", end=" ")
        a.append(i)
    print("=", sum(a))

print()