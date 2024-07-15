from datetime import datetime
import csv

# Function to read transactions from a CSV file, sort them by date, and get the first and last transaction dates
def get_sorted_transaction_date_range(csv_file, date_format='%d/%m/%Y %H:%M'):
    transactions = []

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                row['txn_date'] = datetime.strptime(row['txn_date'], date_format)
                transactions.append(row)
            except ValueError as e:
                print(f"Error parsing date {row['txn_date']}: {e}")

    # Sort transactions by date
    transactions.sort(key=lambda x: x['txn_date'])

    first_date = transactions[0]['txn_date'] if transactions else None
    last_date = transactions[-1]['txn_date'] if transactions else None

    return first_date, last_date

csv_file = 'data.csv'  # Path to the transaction CSV file
first_date, last_date = get_sorted_transaction_date_range(csv_file)

# Get the current date
today_date = datetime.now().strftime("%Y-%m-%d")
# Get the day
today_day = datetime.now().strftime("%A")


# # Function to get the intent from a user query
# def get_intent(user_query):

#   system_instruction_intent = f"""
#       You are an AI language model designed to understand and classify user queries into specific intents related to financial transactions.
#       So your task is to identify the user's intent from their query.
      
#       Choose the appropriate intent from the list below:
#         - RetrieveExpenditureSummary
#         - RetrieveCategoryTransactionTotal
#         - RetrieveCategoryTransactionList
#         - RetrieveTransactionTotal
#         - RetrieveTransactionList

#       Below are various intents with corresponding examples and its responses:

#       Intents and Examples:

#       1. RetrieveExpenditureSummary
#           - Example 1: "Give me a summary of my expenditure for the last month."
#             Response: {{"intent": "RetrieveExpenditureSummary"}}
#           - Example 2: "Summarize my spending for June."
#             Response: {{"intent": "RetrieveExpenditureSummary"}}
#           - Example 3: "I need a summary of my expenses for Q1 2024."
#             Response: {{"intent": "RetrieveExpenditureSummary"}}

#       2. RetrieveCategoryTransactionTotal
#           - Example 1: "How much have I spent on dining?"
#             Response: {{"intent": "RetrieveCategoryTransactionTotal", "category": "dining", "transaction_type": "expense"}}
#           - Example 2: "Total amount spent at Starbucks."
#             Response: {{"intent": "RetrieveCategoryTransactionTotal", "category": "Starbucks", "transaction_type": "expense"}}
#           - Example 3: "How much did I receive through PayPal this month?"
#             Response: {{"intent": "RetrieveCategoryTransactionTotal", "category": "PayPal", "transaction_type": "income",}}

#       3. RetrieveCategoryTransactionList
#           - Example 1: "List my transactions for groceries."
#             Response: {{"intent": "RetrieveCategoryTransactionList", "category": "groceries"}}
#           - Example 2: "Show me all transactions from Amazon."
#             Response: {{"intent": "RetrieveCategoryTransactionList", "category": "Amazon"}}

#       4. RetrieveTransactionTotal
#           - Example 1: "What's the total amount I've spent today?"
#             Response: {{"intent": "RetrieveTransactionTotal", "transaction_type": "expense"}}
#           - Example 2: "How much did I spend in the last year?"
#             Response: {{"intent": "RetrieveTransactionTotal", "transaction_type": "expense"}}
#           - Example 3: "How much money did I deposit last December?"
#             Response: {{"intent": "RetrieveTransactionTotal", "transaction_type": "income"}}

#       5. RetrieveTransactionList
#           - Example 1: "Show me my transactions for this week."
#             Response: {{"intent": "RetrieveTransactionList"}}
#           - Example 2: "What transactions did I make in March?"
#             Response: {{"intent": "RetrieveTransactionList"}}

#       Note : Deposits or other forms of income are categorized as "income" while expenses are categorized as "expense."
      
#       Identify the intent for the following query. Provide the result in JSON format as shown in the examples.

#       Query: {user_query}
#       """

#   return system_instruction_intent

# # Function to extract date from the user query using LLM
# def extract_date(user_query):

#   # Date Extraction Template
#   system_instruction_date = f"""
#   Your task is to accurately identify and extract date information from user queries. Generate a JSON response based on the details provided in the query.

#   You have the transaction data with the date interval between {first_date} and {last_date}

#   Today is {today_date} and the corresponding Day is {today_day}

#   Examples of queries and their corresponding responses:

#   Example queries and responses:

#   1. Query: How much did I spend this month.
#     Response: "start_date:2024-07-01, end_date:{today_date}"

#   2. Query: How much did I spend last year.
#     Response: "start_date:2023-01-01, end_date: 2023-12-31"

#   3. Query: Show me transactions from the first week of June 2023.
#     Response: "start_date:2023-06-01, end_date: 2023-06-04"

#   4. Query: What were my expenses in Q3 2022?
#     Response: "start_date:2022-07-01, end_date:2022-09-30"

#   5. Query: List transactions from last 2 years.
#     Response: "start_date:2022-01-01, end_date:{today_date}"

#   6. Query: List transactions I have done during last week.
#     Response: "start_date:2024-07-01, end_date:2024-07-07"

#   7. Query : How much did I spend on MoneyLion yesterday.
#     Response: "date:2024-07-13"

#   8. Query: How much did I spend this month.
#     Response: "start_date:2024-07-01, end_date:{today_date}"

#   9. Query: How much did I spend last year
#     Response: "start_date:2023-01-01, end_date : 2023-12-30"

#   10. What did I spend last week Tuesday.
#       Response : "date:2024-07-09"
#   Additional guidelines to consider :

#   - "Last 7 days" refers to the seven days before today, excluding today.
#   - "Last 30 days" refers to the thirty days before today, excluding today.
#   - "Last year" refers to the previous calendar year.
#   - "Last 2 years" refers to the two calendar years before the current year.
#   - "Last month" excludes the current month.
#   - "Last week" excludes the current week, defined as Monday to Sunday.
#   - If the month starts on a Wednesday, the first week is from Wednesday to Sunday.
#   - "Yesterday" refers to the previous calendar day.
#   - "First quarter" refers to the months January, February, and March.
#   - If a specific weekday is mentioned (e.g., "last week Tuesday"), it refers to the last occurrence of that weekday in the previous week.

#   Now, generate a JSON response with keys 'start_date' and 'end_date' if there is an interval, otherwise with a single 'date' key. Omit any fields if there is no applicable date for the query.

#   Query: {user_query}
#   """
#   return system_instruction_date


system_instruction_intent = f"""
      You are an AI language model designed to understand and classify user queries into specific intents related to financial transactions.
      So your task is to identify the user's intent from their query.
      
      Choose the appropriate intent from the list below:
        - RetrieveExpenditureSummary
        - RetrieveCategoryTransactionTotal
        - RetrieveCategoryTransactionList
        - RetrieveTransactionTotal
        - RetrieveTransactionList

      Below are various intents with corresponding examples and its responses:

      Intents and Examples:

      1. RetrieveExpenditureSummary
          - Example 1: "Give me a summary of my expenditure for the last month."
            Response: {{"intent": "RetrieveExpenditureSummary"}}
          - Example 2: "Summarize my spending for June."
            Response: {{"intent": "RetrieveExpenditureSummary"}}
          - Example 3: "I need a summary of my expenses for Q1 2024."
            Response: {{"intent": "RetrieveExpenditureSummary"}}

      2. RetrieveCategoryTransactionTotal
          - Example 1: "How much have I spent on dining?"
            Response: {{"intent": "RetrieveCategoryTransactionTotal", "category": "dining", "transaction_type": "expense"}}
          - Example 2: "Total amount spent at Starbucks."
            Response: {{"intent": "RetrieveCategoryTransactionTotal", "category": "Starbucks", "transaction_type": "expense"}}
          - Example 3: "How much did I receive through PayPal this month?"
            Response: {{"intent": "RetrieveCategoryTransactionTotal", "category": "PayPal", "transaction_type": "income",}}

      3. RetrieveCategoryTransactionList
          - Example 1: "List my transactions for groceries."
            Response: {{"intent": "RetrieveCategoryTransactionList", "category": "groceries"}}
          - Example 2: "Show me all transactions from Amazon."
            Response: {{"intent": "RetrieveCategoryTransactionList", "category": "Amazon"}}

      4. RetrieveTransactionTotal
          - Example 1: "What's the total amount I've spent today?"
            Response: {{"intent": "RetrieveTransactionTotal", "transaction_type": "expense"}}
          - Example 2: "How much did I spend in the last year?"
            Response: {{"intent": "RetrieveTransactionTotal", "transaction_type": "expense"}}
          - Example 3: "How much money did I deposit last December?"
            Response: {{"intent": "RetrieveTransactionTotal", "transaction_type": "income"}}

      5. RetrieveTransactionList
          - Example 1: "Show me my transactions for this week."
            Response: {{"intent": "RetrieveTransactionList"}}
          - Example 2: "What transactions did I make in March?"
            Response: {{"intent": "RetrieveTransactionList"}}

      Note : Deposits or other forms of income are categorized as "income" while expenses are categorized as "expense."
      
      Identify the intent for the following query. Provide the result in JSON format as shown in the examples.

      Query: 
      """

system_instruction_date = f"""
  Your task is to accurately identify and extract date information from user queries. Generate a JSON response based on the details provided in the query.

  You have the transaction data with the date interval between {first_date} and {last_date}

  Today is {today_date} and the corresponding Day is {today_day}

  Examples of queries and their corresponding responses:

  Example queries and responses:

  1. Query: How much did I spend this month.
    Response: "start_date:2024-07-01, end_date:{today_date}"

  2. Query: How much did I spend last year.
    Response: "start_date:2023-01-01, end_date: 2023-12-31"

  3. Query: Show me transactions from the first week of June 2023.
    Response: "start_date:2023-06-01, end_date: 2023-06-04"

  4. Query: What were my expenses in Q3 2022?
    Response: "start_date:2022-07-01, end_date:2022-09-30"

  5. Query: List transactions from last 2 years.
    Response: "start_date:2022-01-01, end_date:{today_date}"

  6. Query: List transactions I have done during last week.
    Response: "start_date:2024-07-01, end_date:2024-07-07"

  7. Query : How much did I spend on MoneyLion yesterday.
    Response: "date:2024-07-13"

  8. Query: How much did I spend this month.
    Response: "start_date:2024-07-01, end_date:{today_date}"

  9. Query: How much did I spend last year
    Response: "start_date:2023-01-01, end_date : 2023-12-30"

  10. What did I spend last week Tuesday.
      Response : "date:2024-07-09"
  Additional guidelines to consider :

  - "Last 7 days" refers to the seven days before today, excluding today.
  - "Last 30 days" refers to the thirty days before today, excluding today.
  - "Last year" refers to the previous calendar year.
  - "Last 2 years" refers to the two calendar years before the current year.
  - "Last month" excludes the current month.
  - "Last week" excludes the current week, defined as Monday to Sunday.
  - If the month starts on a Wednesday, the first week is from Wednesday to Sunday.
  - "Yesterday" refers to the previous calendar day.
  - "First quarter" refers to the months January, February, and March.
  - If a specific weekday is mentioned (e.g., "last week Tuesday"), it refers to the last occurrence of that weekday in the previous week.

  Now, generate a JSON response with keys 'start_date' and 'end_date' if there is an interval, otherwise with a single 'date' key. Omit any fields if there is no applicable date for the query.

  Query: 
  """

