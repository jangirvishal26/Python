def process_expression():
    compute = input('\nYour expression? => ')
    if not compute:
        print("No input")
    else:
        try:
            result = eval(compute)
            print("Result =", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    process_expression()
