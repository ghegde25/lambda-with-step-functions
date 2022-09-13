from __future__ import print_function

import json
import urllib
import boto3
import datetime

print('Loading Function')

def refund(message, context):
    print('Received Message From Step Function')
    print(message)
    response = {}
    response['TransactionType'] = message['TransactionType']
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    response['Message'] = 'Inside Refund function'

    return response