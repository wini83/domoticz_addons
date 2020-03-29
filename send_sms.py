#!/usr/bin/python3

import sys
import json
from clickatell.http import Http

import logging

logging.basicConfig(filename='sendsms.log', level=logging.DEBUG)

API_KEY = "d13f-4sSQLGizZmGZpC73A=="

DEST = ["+48606105025", "+48781935566"]


def print_raw_json(status_idx):
    print(json.dumps(status_idx, indent=4, sort_keys=True))


def send_sms(number, content):
    clickatell = Http(API_KEY)
    logging.info(content)
    response = clickatell.sendMessage([number], str(content))
    print(response)  # Returns the headers with all the messages


# print_raw_json(response)
# for entry in response['messages']:
# print(entry) #Returns all the message details per message
# print(entry['apiMessageId'])
# print(entry['to'])
# print(entry['accepted'])
# print(entry['error'])

if len(sys.argv) == 2:
    logging.info('Content:' + str(sys.argv[1]))
    send_sms(DEST[0], str(sys.argv[1]))
    send_sms(DEST[1], str(sys.argv[1]))
else:
    logging.warning('Wrong Parameter')

