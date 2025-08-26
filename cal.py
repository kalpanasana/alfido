
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

OPS = {
    "+": ("Addition", add),
    "-": ("Subtraction", sub),
    "*": ("Multiplication", mul),
    "/": ("Division", div),
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Basic Calculator ===")
    while True:
        print("\nChoose operation: +  -  *  /    (q to quit)")
        op = input("Op: ").strip()
        if op.lower() == "q":
            print("Goodbye!")
            break
        if op not in OPS:
            print("Invalid operation.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            result = OPS[op][1](a, b)
            print(f"{OPS[op][0]} result: {result}")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()
