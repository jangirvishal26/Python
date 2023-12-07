from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import jwt

# Simulating a user model
class CSRFUser:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

# Simulating a user database
user_database = {
    'alice': CSRFUser('alice', 1000),
    'bob': CSRFUser('bob', 500),
}

def authenticate_user(request):
    try:
        # Simulating JWT authentication
        cookie = request.COOKIES.get('auth_cookie')
        payload = jwt.decode(cookie, 'secret_key', algorithms=['HS256'])
        username = payload['username']
        return user_database.get(username)
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        return None

@csrf_exempt
def csrf_transfer_money(request):
    if request.method == 'POST':
        user = authenticate_user(request)

        if user is not None:
            amount = int(request.POST.get('amount', 0))
            user.balance -= amount  # Sink: Modifying the user's balance

            return render(request, 'csrf_dashboard.html', {'balance': user.balance})
        else:
            return redirect('/login/')
    else:
        return render(request, 'csrf_transfer_form.html')
