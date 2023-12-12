from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

# Separate source and sink for better security

def is_valid_target(target):
    # Check if the target is valid according to your criteria
    return target.endswith("example.com")

def redirect_to_target(target):
    # Redirect only if the target is valid
    return redirect(target)

@app.route('/some/path/bad2')
def unsafe2():
    target = request.args.get('target', '')
    if is_valid_target(target):
        return redirect_to_target(target)

# Not safe, as "evil-example.net/example.com" would be accepted
@app.route('/some/path/bad1')
def unsafe1():
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)

# Simplest and safest approach is to use an allowlist
@app.route('/some/path/good1')
def safe1():
    allowlist = [
        "example.com/home",
        "example.com/login",
    ]
    target = request.args.get('target', '')
    if target in allowlist:
        return redirect(target)

# More complex example allowing sub-domains.
@app.route('/some/path/good2')
def safe2():
    target = request.args.get('target', '')
    host = urlparse(target).hostname
    # Note the '.' preceding example.com
    if host and host.endswith(".example.com"):
        return redirect(target)

if __name__ == '__main__':
    app.run(debug=True)
