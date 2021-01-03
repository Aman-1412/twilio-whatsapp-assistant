#!/usr/bin/env python

from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pprint import pprint
import logging

from indian_railways import check_pnr
from whatsapp_actions import open_chat

load_dotenv('../.env')
app = Flask(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')


def echo(msg="say something I'm giving up on you"):
    return msg

command_action_pair = {'echo': echo, 'pnr': check_pnr, 'chat': open_chat}

@app.route('/action', methods=['POST'])
def take_action():
    request_body = request.values['Body']
    pprint(f"Request received: {request_body}")
    command, data = request_body.strip().split(' ', 1) if request_body.startswith('/') else ("", request_body.strip())
    action = command_action_pair[command[1:].lower()] if command and command.startswith('/') else echo
    pprint(f"Selected action: {action}")
    result = action(data)
    pprint(f"Returned result: {result}")
    # logging.info(request.get_data())
    # pprint(dir(request))
    # pprint(request.values)
    resp = MessagingResponse()
    resp.message(result)
    return str(resp)

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0")
