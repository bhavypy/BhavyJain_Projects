#CALCULATOR
while True:

    first_number=int(input("enter the first number :: "))
    second_number=int(input("enter the second number :: "))
    choice=input("enter your choice '+','-','/','*' :: ")
    if choice=="+":
        print("Sum of the numbers = ",first_number+second_number)
    elif choice=="-":
        print("Subtraction of the numbers = ", first_number - second_number)
    elif choice=="/":
        print("Division of the numbers = ", first_number / second_number)
    elif choice=="*":
        print("Multiplication of the numbers = ", first_number * second_number)
    else:
        print("please recheck the entries")
    calculation=input("if you want calculate more type 1 other wise type 2 :: ")
    if calculation=="2":
        print("😊THANKS FOR USING😊")
        break

