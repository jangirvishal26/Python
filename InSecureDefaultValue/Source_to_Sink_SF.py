# $user and $pass automatically set from POST request
user = request.form.get('user')  # Assuming Flask-like request object
passw = request.form.get('pass')  # Assuming Flask-like request object

def login_user(user, passw):
    # Assuming login_user is a function that checks the credentials
    # and returns True if the user is successfully logged in
    return login_user(user, passw)

authorized = False

if login_user(user, passw):
    authorized = True

if authorized:
    generate_page()
