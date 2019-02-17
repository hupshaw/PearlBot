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

    if score < 0:
        for item in range(len(jsonObj["low"])):
            print ("low")


    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    return score


def analyze(message):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(message, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Calls values from function above
    printMessage = print_result(annotations)

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
