print("***Welcome to My calculator***")

start = input("Press enter to use the calculater : ").lower()
while(start != "yes"):
    try:
        num1 = int(input("Enter the first number : "))

        num2 = int(input("Enter the second number : "))

        print("##What kind of operation you want to perform##")
        print("Press + for addition\nPress - for subtraction\nPress / for division\nPress * for multiplication")

        operation = input("Enter Operation : ")

        match operation:
            case "+":
                print(f"The result is : {num1+num2}")
            case "-":
                print(f"The result is : {num1-num2}")
            case "*":
                print(f"The result is : {num1*num2}")
            case "/":
                print(f"The result is : {num1/num2}")
            case _:
                print("There was an error")
        start = input("Want to  quit the calculator?(yes/no) : ").lower()
    except Exception as e:
        print("Enter a valid value of a and b")
    
print("Exiting the program")
