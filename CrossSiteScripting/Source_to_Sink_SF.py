from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/combined')
def combined():
    # Source and sink are combined in the same function
    user_input = request.args.get('name', '')
    
    # Processing the input (sink)
    response_content = "Your name is " + escape(user_input)

    # Returning the response
    return make_response(response_content)

if __name__ == '__main__':
    app.run(debug=True)
