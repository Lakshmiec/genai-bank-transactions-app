import streamlit as st
# import openai
import pandas as pd
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')
# Streamlit UI
st.title('🏦 Bank Transaction Analysis with GenAI')
st.write('Ask questions about your recent bank transactions.')

user_query = st.text_input('Enter your question here:')
csv_file_uploaded = st.file_uploader(label="Upload your CSV File here")