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

def get_user_from_cookie(cookie):
    try:
        # Source: Reading 'auth_cookie' and decoding the JWT
        payload = jwt.decode(cookie, 'secret_key', algorithms=['HS256'])
        username = payload['username']
        return user_database.get(username)
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        return None

def modify_user_balance(user, amount):
    # Sink: Modifying the user's balance
    user.balance -= amount

@csrf_exempt
def csrf_transfer_money(request):
    if request.method == 'POST':
        user = get_user_from_cookie(request.COOKIES.get('auth_cookie'))

        if user is not None:
            amount = int(request.POST.get('amount', 0))
            modify_user_balance(user, amount)

            return render(request, 'csrf_dashboard.html', {'balance': user.balance})
        else:
            return redirect('/login/')
    else:
        return render(request, 'csrf_transfer_form.html')
