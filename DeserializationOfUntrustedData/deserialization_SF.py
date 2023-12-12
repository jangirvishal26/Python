from django.conf.urls import url
import pickle

def unsafe(pickled):
    data = pickle.loads(pickled)
    # Call a method to process the deserialized data (in this case, print the data)
    print_data(data)
    return "Data printed successfully."

def print_data(data):
    # Implement your logic to print or process the deserialized data
    print("Deserialized data:", data)

urlpatterns = [
    url(r'^(?P<object>.*)$', unsafe)
]
