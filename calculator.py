def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Simple Calculator")
    ops = {'+': add, '-': sub, '*': mul, '/': div}
    while True:
        a = get_number("Enter first number: ")
        op = input("Enter operator (+ - * /), or q to quit: ").strip()
        if op.lower() == 'q':
            print("Goodbye!")
            break
        if op not in ops:
            print("Invalid operator. Try again.")
            continue
        b = get_number("Enter second number: ")
        try:
            result = ops[op](a, b)
        except ZeroDivisionError as e:
            print("Error:", e)
            continue
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
# Small update to trigger commit