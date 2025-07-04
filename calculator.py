num1= int(input("enter 1st number :  "))
num2= int(input("enter 2nd number :  "))

print (type(num1))
print (type(num2))

choice = input("choose the operator : + - * % /    : "  )

if choice == "+" :
    sum = num1 + num2
    print ("it is additon", sum)

elif choice == "-":
    sub = num1-num2
    print ("it is substraction", sub )

elif choice == "*":
    prod = num1 * num2
    print (" it is multipliacation", prod)

elif choice == "/":
    div = num1 / num2
    print (" it is division", div)

elif choice == "%":
    mod = num1 % num2
    print (" the remainder is ", mod)

else :
    print ("your selection is invalid")
