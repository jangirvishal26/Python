def get_expression():
    compute = input('\nYour expression? => ')
    if not compute:
        print("No input")
        return None
    return compute

def process_expression(expression):
    try:
        result = eval(expression)
        print("Result =", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    expression = get_expression()
    if expression:
        process_expression(expression)
