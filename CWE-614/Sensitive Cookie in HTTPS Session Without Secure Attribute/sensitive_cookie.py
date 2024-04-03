from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def set_secure_cookie():
    # Source: Sensitive information in the form of a cookie
    sensitive_data = "This is sensitive information"

    # Sink: Setting a cookie without the 'Secure' attribute (vulnerable)
    response = make_response("Cookie set!")
    response.set_cookie('sensitive_cookie', value=sensitive_data, httponly=True)
    
    return response

if __name__ == '__main__':
    # Run the application on a development server
    app.run(debug=True)
