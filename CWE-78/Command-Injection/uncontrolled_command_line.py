from django.conf.urls import url
import subprocess

urlpatterns = [
    # Route to command_execution
    url(r'^command-ex1$', command_execution_unsafe, name='command-execution-unsafe'),
    url(r'^command-ex2$', command_execution_safe, name='command-execution-safe')
]

COMMANDS = {
    "list": "ls",
    "stat": "stat"
}

def pre_execution_hook(action):
    # Log the command about to be executed
    with open('command_log.txt', 'a') as log_file:
        log_file.write(f"Executing command: {action}\n")

def post_execution_hook(action, result):
    # Log the result of the command execution
    with open('command_log.txt', 'a') as log_file:
        log_file.write(f"Command execution result for {action}: {result}\n")

def command_execution_unsafe(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        # BAD -- No sanitizing of input
        pre_execution_hook(action)
        result = subprocess.check_output(["application", action], text=True)
        post_execution_hook(action, result)

def command_execution_safe(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        # GOOD -- Use an allowlist
        pre_execution_hook(action)
        result = subprocess.check_output(["application", COMMANDS.get(action, "default_command")], text=True)
        post_execution_hook(action, result)
