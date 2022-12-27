import requests
import twilio

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = twilio.Client(account_sid, auth_token)

# The phone number you want to send the SMS from (must be a Twilio number)
from_number = 'YOUR_TWILIO_PHONE_NUMBER'

# The phone number you want to send the SMS to
to_number = 'RECIPIENT_PHONE_NUMBER'

# Call the API to generate a message
response = requests.get('https://api.api-ninjas.com/v1/quotes?category=faith')
data = response.json()
message = data['quote']

# Send the SMS
message = client.messages.create(
    body=message,
    from_=from_number,
    to=to_number
)
