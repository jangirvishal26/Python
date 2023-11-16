def command_out(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.communicate()

command_out("rm  -rf *")
