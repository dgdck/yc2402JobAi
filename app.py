'''
Vragen voor AI:
what is the average salary of agile master 

what are the major skills of: C# programmer, and which questions for a job interview should I prepare for
Trainee gekoppeld aan vacature bijvoorbeeld c# programmer >> advies over major skills en  job interview
'''

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

aikey = os.environ.get('OURENVKEY')
