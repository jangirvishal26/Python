from flask import request
import re

@app.route('/lookup')
def lookup():
  regex = request.args['regex']
  data = request.args['data']

  re.search(regex, data) # Noncompliant
