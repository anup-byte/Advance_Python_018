def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def multiply(x, y):
    result = x * y
    return result

def divide(x, y):
    result = x / y
    return result

def complex_operation(a, b, c):
    # Perform a series of calculations
    step1 = add(a, b)
    step2 = multiply(step1, c)
    step3 = subtract(step2, 5)
    result = divide(step3, 2)
    return result

def main():
    num1 = 10
    num2 = 4
    num3 = 7

    # Call the complex operation function
    final_result = complex_operation(num1, num2, num3)

    print("The final result is:", final_result)

if __name__ == "__main__":
    main()
