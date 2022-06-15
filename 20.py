x=input("Enter a number:")
try:
    val = int(x)
    if(x) == str(x)[::-1]:
        print("The number is palindrone")
    else:
        print("The number is not plaindrone")
except ValueError:
    print("Enter a valid number")
