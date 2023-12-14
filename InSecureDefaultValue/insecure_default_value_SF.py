# $user and $pass automatically set from POST request

if login_user(user, pass):
    authorized = True

if authorized:
    generate_page()
