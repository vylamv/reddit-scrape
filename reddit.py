# import twilio client from the dependency
from twilio.rest import Client 

# Twilio Account SID and Auth Token
# client = Client("ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

# send SMS text messages
client.messages.create(to="+1xxxxxxxx",
                        from_="xxxxxxx",
                        body="this is a test message")

