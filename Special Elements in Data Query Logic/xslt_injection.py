from flask import Flask, request
from lxml import etree

app = Flask(__name__)

# Sample XML data
xml_data = """
<data>
  <user>John Doe</user>
</data>
"""

# Endpoint for transforming XML using user-supplied XSLT stylesheet
@app.route('/transform')
def transform():
    xslt_stylesheet = request.args.get('stylesheet', '')

    # Load XML data
    xml_tree = etree.fromstring(xml_data)

    try:
        # Load XSLT stylesheet (vulnerable to injection)
        xslt = etree.fromstring(xslt_stylesheet)

        # Perform XSLT transformation
        transformed_result = etree.XSLT(xslt)(xml_tree)

        return str(transformed_result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
