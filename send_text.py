from twilio.rest import TwilioRestClient

account_sid = "AC33812c3272fb680aaf37269e6803df81" # Your Account SID from www.twilio.com/console
auth_token  = "113ed614bc6b6f0b3293f66e5695e913"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+12176490661",    # Replace with your phone number
    from_="+12175744113") # Replace with your Twilio number

print(message.sid)
