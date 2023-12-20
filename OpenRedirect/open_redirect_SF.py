from flask import Flask, redirect, request

app = Flask(__name__)

def generate_redirect_url(redirect_path):
    # This is a vulnerability (CWE-601) - Redirecting to an untrusted site
    base_url = "http://example.com"
    return f"{base_url}{redirect_path}"

@app.route('/redirect', methods=['GET'])
def redirect_user():
    redirect_path = request.args.get('url')
    redirect_url = generate_redirect_url(redirect_path)
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
