from art import logo
# using recursion functionality

# Adding
def add(n1, n2):
    return n1 + n2

# Substraction
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

function = operations["+"]
function(2, 3)

def calculator():
    print(logo)
    quit = False
    num1 = float(input("what's the first number?: \n"))
    while not quit:
        num2 = float(input("what's the next number?: \n"))

        # loop through dictionary and print the keys
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: \n")
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(
            f"Enter 'y' if you want to continue calculating with {answer}, or type 'n' to start new calculation: \n")
        if choice == "y":
            num1 = answer
            quit = False
        elif choice == "n":
            quit = True
            calculator()

calculator()




