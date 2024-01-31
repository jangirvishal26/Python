# from lxml import etree
# from io import StringIO

# def perform_xpath_query(xml_data, user_input):
#     # Source: Sensitive XML data obtained from a source
#     f = StringIO(xml_data)
#     tree = etree.parse(f)

#     # Sink: User input concatenated into the XPath query (vulnerable)
#     result = tree.xpath("/data[@id='%s']" % user_input)
#     return result

# def process_result(result):
#     # Process the result obtained from the XPath query
#     print("Processed result:", result)

# def main():
#     # Simulating sensitive XML data
#     xml_data = '<data id="123">Sensitive Data</data>'

#     # Simulating user input (potentially from an untrusted source)
#     user_input = "123' or '1'='1'"

#     # Performing an XPath query with user input
#     query_result = perform_xpath_query(xml_data, user_input)

#     # Processing the result (may contain unintended data due to injection)
#     process_result(query_result)

# if __name__ == "__main__":
#     main()

from lxml import etree
from io import StringIO

from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context, Engine, engines


def a(request):
    value = request.GET['xpath']
    f = StringIO('<foo><bar></bar></foo>')
    tree = etree.parse(f)
    r = tree.xpath("/tag[@id='%s']" % value)


urlpatterns = [
    path('a', a)
]
