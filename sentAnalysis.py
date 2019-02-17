import argparse
import json
import random

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#TODO: convert to return
def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    jsonfile = open("data.json", "r")
    jsonObj = json.load(jsonfile)
    jsonfile.close()
    message = ""

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score

    if sentence_sentiment < 0 and sentence_sentiment >= -.3:
       r = random.randint(0,len(jsonObj["low"]))
       #print(len(jsonObj["low"]))
       #print("low " + str(r))
       message = jsonObj["low"][r]
    elif sentence_sentiment < -.3 and sentence_sentiment >= -.6:
       r = random.randint(0,len(jsonObj["medium"]))
       #print("med " + str(r))
       message = jsonObj["medium"][r]
    else:
       r = random.randint(0,len(jsonObj["high"]))
       #print("high " +str(r))
       message = jsonObj["high"][r]



    return (sentence_sentiment,message)


def analyze(message):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()
    document = types.Document(
        content=message,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Calls values from function above
    score = print_result(annotations)
    return score

#main
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'message',
        help='The user message from Slack Bot')
    args = parser.parse_args()

    analyze(args.message)
