#ALL THIS CODE IS FROM :
#   https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

import os
import time
import re
from slackclient import SlackClient

# instantiate Slack SlackClient
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

if slack_client.rtm_connect():
    print("Connected")
    while True:
        events = events = slack_client.rtm_read()
        for event in events:
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                user = event['user']
                text = event['text']

                    # Helena calls the Google API, gets sentiment score
                        #score =
                if len(text) > 1:
                # Helena looks the sentiment score from API up in Database
                # Helena returns to you a string (message) to be posted by the slack bot to the user
                    slack_client.api_call(
                        "chat.postMessage",
                        channel="im.open", user=user
                        text="This is a DM"
                        print("DM Sent")
                    )
                else:
                    print("All Good")


        time.sleep(1)
else:
    print('Connection failed, invalid token? Big sad')
