from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/xss')
def xss_vulnerable():
    # vulnerable cross site scripting code
    user_input = request.args.get('name', '')
    
    # Sink: Incorporating user input into an HTML template without proper escaping
    html_template = """
    <html>
    <head><title>XSS Vulnerable Page</title></head>
    <body>
        <h1>Hello, {{ user_input | safe }}!</h1>
    </body>
    </html>
    """
    
    # Rendering the template without proper escaping
    rendered_template = render_template_string(html_template, user_input=user_input)

    return rendered_template

if __name__ == '__main__':
    app.run(debug=False)
