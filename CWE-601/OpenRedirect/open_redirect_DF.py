from flask import Flask, redirect, request

app = Flask(__name__)

def get_redirect_path():
    # This is the source - user input for the redirect path
    return request.args.get('url')

def generate_redirect_url(redirect_path):
    # This is the sink - constructing the redirect URL
    # This is a vulnerability (CWE-601) - Redirecting to an untrusted site
    base_url = "http://example.com"
    return f"{base_url}{redirect_path}"

@app.route('/redirect', methods=['GET'])
def redirect_user():
    redirect_path = get_redirect_path()
    redirect_url = generate_redirect_url(redirect_path)
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
