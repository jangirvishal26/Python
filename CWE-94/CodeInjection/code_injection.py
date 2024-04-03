from django.urls import path
from django.http import HttpResponse
import base64

urlpatterns = [
    # Route to code_execution
    path('code-ex1', code_execution_bad, name='code-execution-bad'),
    path('code-ex2', code_execution_good, name='code-execution-good')
]

def get_user_input(request):
    if request.method == 'POST':
        return base64.decodestring(request.POST.get('first_name', ''))
    return None

def execute_code_bad(user_input):
    # BAD -- Allow user to define code to be run.
    exec("setname('%s')" % user_input)

def execute_code_good(user_input):
    # GOOD -- Call code directly
    setname(user_input)

def code_execution_bad(request):
    user_input = get_user_input(request)
    if user_input:
        execute_code_bad(user_input)
    return HttpResponse("Code executed successfully")

def code_execution_good(request):
    user_input = get_user_input(request)
    if user_input:
        execute_code_good(user_input)
    return HttpResponse("Code executed successfully")
