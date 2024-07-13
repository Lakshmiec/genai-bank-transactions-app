# This file contains the function to interact with the OpenAI ChatCompletion API.

import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.getenv('OPENAI_API_KEY')


def get_chat_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0  # Degree of randomness
    )
    return response.choices[0].message["content"]