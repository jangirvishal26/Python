from flask import Flask, redirect, request

app = Flask(__name__)

def get_user_input():
    # Source: Obtaining user input
    return request.args.get('url')

def generate_redirect_url(redirect_path):
    # Sink: Generating the redirect URL
    base_url = "http://example.com"
    return f"{base_url}{redirect_path}"

@app.route('/redirect', methods=['GET'])
def redirect_user():
    redirect_path = get_user_input()
    redirect_url = generate_redirect_url(redirect_path)
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
