import os
import openai
from config import apikey
# from openai import OpenAI

openai.api_key =apikey
# client = OpenAI()

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt="write an email to my boss for resignation",
    temperature=1,
    max_tokens=100,  # Use a lower value like 100 to test
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)