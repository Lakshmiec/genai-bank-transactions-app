import streamlit as st
# import openai
import pandas as pd
import os
from data_retriever import get_response_data
from intent_handler import IntentHandler

# Initialize the IntentHandler
intent_handler = IntentHandler()
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) # read local .env file

# openai.api_key  = os.getenv('OPENAI_API_KEY')
# Streamlit UI
st.title('🏦 Bank Transaction Analysis with GenAI')
st.write('Ask questions about your recent bank transactions.')

user_query = st.text_input('Enter your question here:')

if user_query:
    # Get the response data based on the user's query
    intent, category, transaction_type, dates = get_response_data(user_query)
# Call the appropriate function based on the intent and display the response in the UI

if intent == "RetrieveTransactionList":
    result = intent_handler.retrieve_transaction_list(dates)
    st.write(result)
# elif intent == "RetrieveExpenditureSummary":
#     result = retrieve_expenditure_summary(dates)
#     st.write(result)
elif intent == "RetrieveCategoryTransactions":
    result = intent_handler.retrieve_category_transactions(category, dates)
    st.write(result)
elif intent == "RetrieveCategoryTransactionTotal":
    result = intent_handler.retrieve_category_transaction_total(category, transaction_type)
    st.write(result)
elif intent == "RetrieveTransactions":
    result = intent_handler.retrieve_transactions(dates)
    st.write(result)
elif intent == "RetrieveTransactionsAmount":
    result = intent_handler.retrieve_transactions(dates, transaction_type)
    st.write(result)
else:
    st.write(f"Unknown intent: {intent}")
