from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pprint import pprint
import requests

app = Flask(__name__)

GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"


@app.route("/")
def hello():
    return "Hello, World"


@app.route('/sms', methods=['POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    responded = False

    if "hi" in incoming_msg:
        msg.body("Hello, my name is Twillio Sandbox. I was created by Uriel to fulfill his will,"
                 "I don't have a Artificial Intelligence yet, but for sure it'll come soon")
        responded = True
    if "uriel" in incoming_msg:
        msg.body("Do you want to know about Uriel? Look at his source: https://github.com/urielbrasil")
        responded = True
    if "clima" in incoming_msg:
        r = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=Calama&APPID=dd7df59e94769ea2b40185a297407600')
        msg.body(r.json())
        responded = True
    if 'hot' in incoming_msg:
        # return a quote
        msg.body("Yeah it's hot")
        responded = True
    if 'cold' in incoming_msg:
        # return a cat pic
        msg.body("For sure it's really cold!")
        responded = True
    if not responded:
        msg.body("I don't know")
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)


