import streamlit as st
# import openai
import pandas as pd
import os
from data_retriever import get_response_data
from intent_handlers import IntentHandler

# Initialize the IntentHandler
intent_handler = IntentHandler()

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
    elif intent == "RetrieveCategoryTransactionsList":
        result = intent_handler.retrieve_category_transactions_list(category, dates)
        st.write(result)
    elif intent == "RetrieveCategoryTransactionTotal":
        result = intent_handler.retrieve_category_transaction_total(category, transaction_type, dates)
        st.write(result)
    elif intent == "RetrieveTransactions":
        result = intent_handler.retrieve_transactions(dates)
        st.write(result)
    elif intent == "RetrieveTransactionTotal":
        result = intent_handler.retrieve_transaction_total(dates, transaction_type)
        st.write(result)
    else:
        st.write(f"Unknown intent: {intent}")
