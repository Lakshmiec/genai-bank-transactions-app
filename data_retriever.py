
from chat_completion import get_intent, get_date
import json

def get_response_data(user_query):

    # Get responses
    intent_response = get_intent(user_query)
    date_response = get_date(user_query)

    # Parse the JSON responses
    intent_data = json.loads(intent_response)
    date_data = json.loads(date_response)

    # Extract intent and parameters
    intent = intent_data["intent"]
    start_date = date_data.get("start_date")
    end_date = date_data.get("end_date")
    single_date = date_data.get("date")
    category = intent_data.get("category")
    transaction_type = intent_data.get("transaction_type")

    # Load date values into a list
    dates = [start_date, end_date] if start_date and end_date else [single_date]
    
    return intent, category, transaction_type, dates




