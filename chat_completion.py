# This file contains the function to interact with the OpenAI ChatCompletion API.

import os
from date_query_templates import  system_instruction_date, system_instruction_intent
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Define the model configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

# Create the model for intent extraction
model_intent = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction_intent
)

# Create the model for intent extraction
model_date = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction_date
)


def get_intent(prompt):
    # Start the chat session
    chat_session = model_intent.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    prompt,
                ],
            }
        ]
    )

    # Send the message and get the response
    response = chat_session.send_message(prompt)
    return response.text

def get_date(prompt):
    # Start the chat session
    chat_session = model_date.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    prompt,
                ],
            }
        ]
    )

    # Send the message and get the response
    response = chat_session.send_message(prompt)
    return response.text


