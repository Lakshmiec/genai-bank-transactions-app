import csv
from datetime import datetime

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
