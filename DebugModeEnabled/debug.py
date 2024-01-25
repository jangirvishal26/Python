import logging

def process_payment(user_data):
    # ... payment processing logic ...

    # Debug code left active in production, logging sensitive information
    logging.debug(f"Payment processed for user: {user_data['username']}, amount: {user_data['amount']}")

    # ... more payment processing logic ...

# Production code that calls the function
user_data = {
    'username': 'example_user',
    'amount': 100.00,
    # ... other sensitive information ...
}

process_payment(user_data)
