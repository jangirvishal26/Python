from flask import Flask, request, abort

app = Flask(__name__)

# BAD: Server Information Exposure
@app.route('/divide')
def divide():
    try:
        numerator = int(request.args.get('numerator'))
        denominator = int(request.args.get('denominator'))
        
        result = numerator / denominator

        return f"The result of the division is: {result}"

    except ZeroDivisionError as e:
        # BAD: Exposing server information
        return f"Error: Division by zero. {str(e)}"

    except Exception as e:
        # BAD: Exposing server information
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
