def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division with zero is not possible"

while True:
    print("Choose your weapon")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")
    
    choice = input("Enter your choice [1-5]: ")
    if choice == '5':
        print("Bye-Bye")
        break
    elif choice in {'1', '2', '3', '4'}:
        x = float(input("Enter the first number- "))
        y = float(input("Enter the second number-"))
        if choice == '1':
            result = add(x, y)
            print(f"result:{result}")
        elif choice == '2':
            result = subtract(x, y)
            print(f"result:{result}")
        elif choice == '3':
            result = multiply(x, y)
            print(f"result:{result}")
        elif choice == '4':
            result = divide(x, y)
            print(f"result: {result}")
    else:
        print("!!choose a number within the range!! ")
