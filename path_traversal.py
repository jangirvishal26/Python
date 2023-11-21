from django.http import HttpResponseBadRequest

urlpatterns = [
    # Route to code_execution
    url(r'^code-ex1$', code_execution_bad, name='code-execution-bad'),
    url(r'^code-ex2$', code_execution_good, name='code-execution-good')
]

def code_execution_bad(request):
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        # BAD -- Allow user to define code to be run.
        exec("setname('%s')" % first_name)
        return HttpResponse("Code executed successfully")
    else:
        return HttpResponseBadRequest("Invalid request method")

def code_execution_good(request):
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        # GOOD -- Call code directly
        setname(first_name)
        return HttpResponse("Code executed successfully")
    else:
        return HttpResponseBadRequest("Invalid request method")
