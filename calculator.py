import time

def showmenu():
    print("""
==================================================
PYTHON CALCULATOR v1.0 - By @manannjoshi on Github
==================================================
          """)
    print("""
Choose an operation

1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

    inp = int(input("Enter choice >>> "))
    return inp


def getNum():
    print()
    num = int(input("Enter first number  >>> "))
    num2 = int(input("Enter second number >>> "))
    return (num, num2)


def add(x, y):
    z = x + y
    return z


def sub(x, y):
    z = x - y
    return z


def mul(x, y):
    z = x * y
    return z


def div(x, y):
    z = x / y
    return z


while True:
    try:
        ans = showmenu()

        if ans == 1:
            print("Addition Selected")
            nums = getNum()
            x, y = nums

            print()
            print("Calculating...")
            time.sleep(0.5)
            print("┌" + "─" * 41 + "┐")
            print(f"│ Result : {add(x, y):<31}│")
            print("└" + "─" * 41 + "┘")
            print("-" * 45)
            print()
            again = input("Perform another calculation? [Y/N] >>> ")
            if again.lower() != "y":
                print()
                print("=" * 45)
                print("Thank you for using")
                print("Python Calculator")
                print("Created by Manan")
                print("=" * 45)
                input("Press ENTER to exit...")
                break

            print()

        elif ans == 2:
            print("Subtraction Selected")
            nums = getNum()
            x, y = nums

            print()
            print("Calculating...")
            time.sleep(0.5)
            print("┌" + "─" * 41 + "┐")
            print(f"│ Result : {sub(x, y):<31}│")
            print("└" + "─" * 41 + "┘")
            print("-" * 45)
            print()
            again = input("Perform another calculation? [Y/N] >>> ")
            if again.lower() != "y":
                print()
                print("=" * 45)
                print("Thank you for using")
                print("Python Calculator")
                print("Created by Manan")
                print("=" * 45)
                input("Press ENTER to exit...")
                break

            print()

        elif ans == 3:
            print("Multiplication Selected")
            nums = getNum()
            x, y = nums
            print("Calculating...")
            time.sleep(0.5)
            print()
            print("┌" + "─" * 41 + "┐")
            print(f"│ Result : {mul(x, y):<31}│")
            print("└" + "─" * 41 + "┘")
            print("-" * 45)
            print()
            again = input("Perform another calculation? [Y/N] >>> ")
            if again.lower() != "y":
                print()
                print("=" * 45)
                print("Thank you for using")
                print("Python Calculator")
                print("Created by Manan")
                print("=" * 45)
                input("Press ENTER to exit...")
                break

            print()

        elif ans == 4:
            print("Division Selected")
            nums = getNum()
            x, y = nums
            print()
            if y == 0:
                print("Division by zero is not allowed.")
                print("-" * 45)
                print()
                again = input("Perform another calculation? [Y/N] >>> ")
                if again.lower() != "y":
                    print()
                    print("=" * 45)
                    print("Thank you for using")
                    print("Python Calculator")
                    print("Created by Manan")
                    print("=" * 45)
                    input("Press ENTER to exit...")
                    break
                print()
            else:
                print("Calculating...")
                time.sleep(0.5)
                print("┌" + "─" * 41 + "┐")
                print(f"│ Result : {div(x, y):<31}│")
                print("└" + "─" * 41 + "┘")
                print("-" * 45)
                print()
                print()
                again = input("Perform another calculation? [Y/N] >>> ")
                if again.lower() != "y":
                    print()
                    print("=" * 45)
                    print("Thank you for using")
                    print("Python Calculator")
                    print("Created by Manan")
                    print("=" * 45)
                    input("Press ENTER to exit...")
                    break
                else:
                    print("Invalid choice!")
                    print()
                    print("=" * 45)
                    print("Thank you for using")
                    print("Python Calculator")
                    print("Created by Manan")
                    print("=" * 45)
                    input("Press ENTER to exit...")
                    break
                    

                print()

        else:
            print()
            print("Invalid choice!")
            print("Please select an option between 1 and 4.")
            print()

    except ValueError:
        print()
        print("Invalid input!")
        print("Please enter numbers only.")
        print()