#ALL THIS CODE IS FROM :
#   https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

import os
import time
import re
from slackclient import SlackClient
from sentAnalysis import *

# instantiate Slack SlackClient
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

if slack_client.rtm_connect():
    print("Connected")
    #set image to regular

    while True:
        print("Listening...")
        events = events = slack_client.rtm_read()
        for event in events:
            if "subtype" not in event.keys():
                if (
                    'channel' in event and
                    'text' in event and
                    event.get('type') == 'message'
                ):
                    user = event['user']
                    text = event['text']

                    (score,message) = analyze(text)
                    print(score)
                    if score < 0:
                        user = event['user']
                    # Helena looks the sentiment score from API up in Database
                    # Helena returns to you a string (message) to be posted by the slack bot to the user
                        response = slack_client.api_call(
                            "im.open",
                            user=user
                        )
                        print(response["channel"]["id"])

                        slack_client.api_call(
                            "chat.postMessage",
                            channel=response["channel"]["id"],
                            text=message,
                            status_emoji=":angrypearl:"
                        )
                        #set to unpset image
                        print("DM Sent")
                    else:
                        #set to happy image
                        print("All Good")


        time.sleep(1.5)
else:
    print('Connection failed, invalid token? Big sad')
