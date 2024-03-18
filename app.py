'''
Vragen voor AI:
what is the average salary of agile master

what are the major skills of: C# programmer, and which questions for a job interview should I prepare for
Trainee gekoppeld aan vacature bijvoorbeeld c# programmer >> advies over major skills en  job interview
'''

from flask import Flask
from flask_cors import CORS
# from flask_cors import cross_origin
import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

os.environ['API_USER'] = 'username'
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

aikey = os.environ.get('OURENVKEY')


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/<jobrole>")
def hello_world(jobrole):
    client = OpenAI(api_key=aikey)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": f"what are the major skills of: {jobrole}, and which questions for a job interview should I prepare for"
        }],
        temperature=0.5,
        max_tokens=256
    )
    #print(response)
    return response.choices[0].message.content
