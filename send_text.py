from twilio.rest import TwilioRestClient

account_sid = "{{ get your own :) }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ get your own :) }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+12176490661",    # Replace with your phone number
    from_="+12175744113") # Replace with your Twilio number

print(message.sid)
