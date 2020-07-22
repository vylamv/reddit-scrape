# import twilio client from the dependency
from config import client 


# send SMS text messages
client.messages.create(to="+xxxxxxxxx",
                        from_="+xxxxxxxxxxx",
                        body="this is a test message")

