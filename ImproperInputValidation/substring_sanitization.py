from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

# Not safe, as "evil-example.net/example.com" would be accepted

@app.route('/some/path/bad1')
def unsafe1(request):
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)

# Not safe, as "benign-looking-prefix-example.com" would be accepted

@app.route('/some/path/bad2')
def unsafe2(request):
    target = request.args.get('target', '')
    if target.endswith("example.com"):
        return redirect(target)



#Simplest and safest approach is to use an allowlist

@app.route('/some/path/good1')
def safe1(request):
    allowlist = [
        "example.com/home",
        "example.com/login",
    ]
    target = request.args.get('target', '')
    if target in allowlist:
        return redirect(target)

#More complex example allowing sub-domains.

@app.route('/some/path/good2')
def safe2(request):
    target = request.args.get('target', '')
    host = urlparse(target).hostname
    #Note the '.' preceding example.com
    if host and host.endswith(".example.com"):
        return redirect(target)
