from flask import Flask, render_template
import os

app = Flask(__name__)

# Set the template folder to the current directory
app.template_folder = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
