from flask import Flask, render_template

app = Flask(__name__)

# This route renders a page that loads resources from any domain (unsafe)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
