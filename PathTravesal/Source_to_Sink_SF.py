from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import base64

urlpatterns = [
    url(r'^code-ex$', code_execution_combined, name='code-execution-combined'),
]

@csrf_exempt  # Exempt CSRF for demonstration purposes only; it is generally not recommended to disable CSRF protection
def code_execution_combined(request):
    if request.method == 'POST':
        try:
            # Combining source and sink in the same function
            first_name = base64.decodestring(request.POST.get('first_name', '').encode()).decode('utf-8')
            
            # Processing the input (sink)
            # BAD: Allowing user to define code to be run
            exec("setname('%s')" % first_name)
            
            # Or alternatively, if you want to use eval
            # eval("setname('%s')" % first_name, {'setname': setname}, {})

            return HttpResponse("Code executed successfully")
        except Exception as e:
            return HttpResponseBadRequest(f"Error: {e}")
    else:
        return HttpResponseBadRequest("Invalid request method")
