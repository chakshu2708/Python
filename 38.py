def canMakeSame(str):
    zeros = 0
    ones = 0


    for i in range(0, len(str)):
        ch = str[i]
        if(ch == '0'):
            zeros+= 1
        else:
           ones+= 1 

    return (zeros == 1 or ones == 1);

if(canMakeSame("101")):
    print("yes\n")
else:
    print("No\n")