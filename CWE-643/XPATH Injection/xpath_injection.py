from lxml import etree
from io import StringIO

from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context, Engine, engines

def a(request):
    value = get_user_input(request)
    tree = parse_xml_data()
    perform_xpath_query(tree, value)

def get_user_input(request):
    # Source: Sensitive data obtained from user input
    return request.GET['xpath']

def parse_xml_data():
    # Simulating sensitive XML data
    xml_data = '<foo><tag id="123"></tag></foo>'
    f = StringIO(xml_data)
    return etree.parse(f)

def perform_xpath_query(tree, value):
    # Sink: User input concatenated into the XPath query (vulnerable)
    result = tree.xpath("/foo/tag[@id='%s']" % value)
    return result

urlpatterns = [
    path('a', a)
]

