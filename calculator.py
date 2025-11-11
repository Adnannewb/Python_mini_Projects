import os, re

HISTORY_FILE = "history.txt"

def view_history():
    if not os.path.exists(HISTORY_FILE):
        print("No History Recorded")
        return
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No History Recorded")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    open(HISTORY_FILE, 'w').close()
    print("History Cleared!")

def save_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = re.split(r'\s*([+\-*/])\s*', user_input.strip())
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g. 8 + 8)")
        return

    num1, op, num2 = parts
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Please enter valid numbers.")
        return

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only +, -, *, /")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_history(user_input, result)

def main():
    print("-------> Simple Calculator <-------")
    while True:
        print("""
1 for calculation
2 for view history
3 for clear history
4 for exit
""")
        try:
            num = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number (1-4).")
            continue

        if num == 1:
            user_input = input("Enter calculation (e.g. 8 + 8 or 8+8): ")
            calculate(user_input)
        elif num == 2:
            view_history()
        elif num == 3:
            clear_history()
        elif num == 4:
            print("Thank you for using my calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
