from flask import Flask, request, abort

app = Flask(__name__)

def divide_operation(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError as e:
        handle_zero_division_error(e)
    except Exception as e:
        handle_generic_error(e)

def handle_zero_division_error(error):
    # Log the error for internal use
    app.logger.error(f"Error: Division by zero. {str(error)}")
    # Return a generic message to the client
    abort(400, "Invalid input. Cannot divide by zero.")

def handle_generic_error(error):
    # Log the error for internal use
    app.logger.error(f"An error occurred: {str(error)}")
    # Return a generic message to the client
    abort(500, "An unexpected error occurred.")

@app.route('/divide')
def divide():
    try:
        numerator = int(request.args.get('numerator'))
        denominator = int(request.args.get('denominator'))
        result = divide_operation(numerator, denominator)
        return f"The result of the division is: {result}"
    except ValueError as e:
        handle_value_error(e)
    except Exception as e:
        handle_generic_error(e)

def handle_value_error(error):
    # Log the error for internal use
    app.logger.error(f"Error: Invalid input. {str(error)}")
    # Return a specific error message to the client
    abort(400, "Invalid input. Please provide valid numerical values.")

if __name__ == '__main__':
    app.run(debug=True)
