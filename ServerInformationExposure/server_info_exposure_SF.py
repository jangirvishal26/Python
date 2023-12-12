from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/divide')
def divide():
    try:
        numerator = int(request.args.get('numerator'))
        denominator = int(request.args.get('denominator'))

        # Processing the user input (source and sink combined)
        try:
            result = numerator / denominator
            return f"The result of the division is: {result}"
        except ZeroDivisionError as e:
            # Log the error for internal use
            app.logger.error(f"Error: Division by zero. {str(e)}")
            # Return a generic message to the client
            abort(400, "Invalid input. Cannot divide by zero.")
        except Exception as e:
            # Log the error for internal use
            app.logger.error(f"An error occurred: {str(e)}")
            # Return a generic message to the client
            abort(500, "An unexpected error occurred.")

    except ValueError as e:
        # Log the error for internal use
        app.logger.error(f"Error: Invalid input. {str(e
