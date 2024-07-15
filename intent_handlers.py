class IntentHandler:
    """
    IntentHandler class handles retrieving and processing transaction data for a specific client.
    It includes methods to fetch transactions, transaction amounts, and transactions by category or merchant.
    """
    def __init__(self):

        #read the file
        data = pd.read_csv("data.csv")

        
        data['txn_date'] = pd.to_datetime(data["txn_date"])
        
    def PreprocessData(self, data):
        """
        Cleans the transaction listing by dropping unnecessary columns and renaming others.
        Args:
            listing (pd.DataFrame): The transaction listing to be cleaned.
        Returns:
            pd.DataFrame: The cleaned transaction listing.
        """
       # Renaming columns for clarity
        data.rename(columns={
            'txn_date': 'Transaction Date',
            'desc': 'Description',
            'amt': 'Amount',
            'cat': 'Category',
            'merchant': 'Merchant'
        }, inplace=True)
        # dropping unnecessary columns 
        data = data.drop(['clnt_id', 'bank_id', 'acc_id', 'txn_id'], axis=1)
        data = data.reset_index(drop=True)
        return data
    
    def FilterDataByDates(self, data, dates):
    """
    Filters the given data based on the provided date or date range.
    
    Args:
        data (pd.DataFrame): The DataFrame containing transaction data.
        dates (list or tuple): Either a single datetime value or a tuple containing start and end dates.
        
    Returns:
        pd.DataFrame: The filtered data that falls within the specified date or date range.
    """
        if len(dates) == 2:
            start_date, end_date = dates[0], dates[1]
            filtered_data = data[(data['txn_date'] >= start_date) & (data['txn_date'] <= end_date)]
        else:
            filtered_data = data[data['txn_date'] == dates]
        return filtered_data
    
    def CheckValidDates(self, dates):
        """
        Check if the provided dictionary contains any valid, non-empty date values.

        Args:
            dates (dict): A dictionary where the values are date strings.

        Returns:
            bool: True if there is at least one non-empty date value, otherwise False.
        """
        if not dates:
            return False

        for date in dates.values():
            if date:
                return True

        return False

        
    def retrieve_transaction_list(self, dates):
         """
        Retrieves the transaction list based on the specified dates.
        If dates are provided, filters transactions within that date range.
        Args:
            dates (list or tuple, optional): Either a single datetime value or a tuple containing start and end dates.
        Returns:
            pd.DataFrame: The filtered transaction data.
        """
        preprocessed_data = self.PreprocessData(self.data)
        filtered_transactions = self.FilterDataByDates(preprocessed_data, dates)

        if len(dates) == 2:
            start_date, end_date = dates
            # Simulate fetching transactions within the date range and category
            print(f"Following are the Transactions from {start_date} to {end_date} for category: {category}: {filtered_transactions}")
        else:
            date = dates[0]
            print(f"Following Transactions for date: {date} : {filtered_transactions}")
    