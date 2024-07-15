import pandas as pd
class IntentHandler:
    """
    IntentHandler class handles retrieving and processing transaction data for a specific client.
    It includes methods to fetch transactions, transaction amounts, and transactions by category or merchant.
    """
    def __init__(self):

        #read the file
        data = pd.read_csv("data.csv")

        
        data['txn_date'] = pd.to_datetime(data["txn_date"])
        self.data = data

    """
    Helper Functions
    ------------------------------
    """
    def PreprocessData(self, data):
        """
        Cleans the transaction listing by dropping unnecessary columns and renaming others.
        Args:
            listing (pd.DataFrame): The transaction listing to be cleaned.
        Returns:
            pd.DataFrame: The cleaned transaction listing.
        """
         # Drop specified columns
        data = data.drop(['clnt_id', 'bank_id', 'acc_id', 'txn_id'], axis=1)
        
        # Rename remaining columns
        data.rename(columns={'txn_date': 'Transaction Date', 'desc': 'Description', 'amt': 'Amount', 'cat': 'Category', 'merchant': 'Merchant'}, inplace=True)
        
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
            filtered_data = data[(data['Transaction Date'] >= start_date) & (data['Transaction Date'] <= end_date)]
        else:
            filtered_data = data[data['Transaction Date'] == dates[0]]
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

        for date in dates:
            if date:
                return True

        return False

    def CalculateExpenseSum(self, data, date_range):
        """
        Calculates the total sum of expenses for the given date or date range.
        
        Parameters:
            data (DataFrame): The dataset to filter and analyze.
            date_range (list): List of dates to filter. One date filters for that specific date. 
                            Two dates filter for the inclusive range between them.
                            
        Returns:
            str: A message stating the total expense amount for the specified dates.
        """
        if len(date_range) == 1:
            filtered_data = data[data["txn_date"] == pd.to_datetime(date_range[0])]
            total_expenses = round(filtered_data[filtered_data['amt'] < 0]['amt'].sum())
            return f"Total expenses incurred on {date_range[0]}: {str(total_expenses).lstrip('-')}\n"
        else:
            filtered_data = data[(data["txn_date"] >= pd.to_datetime(date_range[0])) & 
                                (data["txn_date"] <= pd.to_datetime(date_range[1]))]
            total_expenses = round(filtered_data[filtered_data['amt'] < 0]['amt'].sum())
            return f"Total expenses incurred between {date_range[0]} and {date_range[1]}: {str(total_expenses).lstrip('-')}\n"

    def CalculateIncomeSum(self, data, date_range):
        """
        Calculates the total sum of income for the given date or date range.
        
        Parameters:
            data (DataFrame): The dataset to filter and analyze.
            date_range (list): List of dates to filter. One date filters for that specific date. 
                            Two dates filter for the inclusive range between them.
                            
        Returns:
            str: A message stating the total income amount for the specified dates.
        """
        if len(date_range) == 1:
            filtered_data = data[data["txn_date"] == pd.to_datetime(date_range[0])]
            total_income = round(filtered_data[filtered_data['amt'] > 0]['amt'].sum())
            return f"Total income received on {date_range[0]}: {total_income}\n"
        else:
            filtered_data = data[(data["txn_date"] >= pd.to_datetime(date_range[0])) & 
                                (data["txn_date"] <= pd.to_datetime(date_range[1]))]
            total_income = round(filtered_data[filtered_data['amt'] > 0]['amt'].sum())
            return f"Total income received between {date_range[0]} and {date_range[1]}: {total_income}\n"
    
    def determine_filter_type(self, filter_criteria):
        """
        Determines whether the filter criteria is based on category or merchant.
        
        Parameters:
            filter_criteria (str): The filter criteria to check.

        Returns:
            str or None: Returns "merchant_filter" if the criteria is a merchant, 
                         "category_filter" if it is a category, or None if it doesn't match either.
        """
        self.merchants = self.data["merchant"].unique()
        
        self.categories = self.data["cat"].unique()
        print(self.categories)
        if filter_criteria in self.merchants:
            return "merchant_filter"
        elif filter_criteria in self.categories:
            return "category_filter"
        else:
            return None
    
    def CalculateAmount(self, transactions, transaction_type):
        if transaction_type == "expense":
            return transactions[transactions["amt"] < 0]["amt"].sum() * -1
        elif transaction_type == "income":
            return transactions[transactions["amt"] > 0]["amt"].sum()
        else:
            return 0    
    """
    Transaction Functions
    ---------------------------------------
    """
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
            return(f"Following are the Transactions from {start_date} to {end_date} : \n{filtered_transactions}\n")
        else:
            date = dates[0]
            return(f"Following Transactions for date: {date} : \n{filtered_transactions}\n")
    
    def retrieve_category_transactions_list(self, category, dates):
        """
        Filters transactions based on a given merchant and optionally within a specified date range.

        Parameters:
            merchant (str): The name of the merchant to filter transactions for.
            dates (list, optional): List of one or two dates to filter the transactions. Defaults to None.

        Returns:
            str: A message detailing the transactions found or indicating that none were found.
        """
        
        filtered_data = self.data
        
        if self.CheckValidDates(dates):
            filtered_data = self.FilterDataByDates(dates)
        
        # category_lower = str(category).lower()
        
        column = self.determine_filter_type(category)
        
        if column == 'merchant_filter':
            column = "merchant"
        else:
            column = "cat"
        if column is None:
            return f"Sorry, Transactions on {category} not found"
        
        matching_transactions = filtered_data[filtered_data[column] == category]
        
        if not matching_transactions.empty:
            cleaned_transactions = self.PreprocessData(matching_transactions)
            return f"Following are your transactions for {category}:\n{cleaned_transactions}"
        else:
            return "Transactions not found"
      
    def retrieve_category_transaction_total(self, category, transaction_type, dates = None):
        
        """
        Retrieves the total transaction amount for a specific merchant and transaction type (expense or income),
        optionally within a specified date range.

        Parameters:
            trn_type (str): The type of transaction ("expense" or "income").
            merchant (str): The name of the merchant to filter transactions for.
            dates (list, optional): List of dates to filter transactions. Defaults to None.

        Returns:
            str: A formatted message indicating the total amount spent or deposited for the specified merchant.
        """
        
        filtered_data = self.data
        
        if self.CheckValidDates(dates):
            filtered_data = self.FilterDataByDates(dates)
        
        # category_lower = str(category).lower()
        
        column = self.determine_filter_type(category)
        
        if column == 'merchant_filter':
            column = "merchant"
        else:
            column = "cat"
        if column is None:
            return f"Sorry, Transactions on {category} not found"
        
        matching_transactions = filtered_data[filtered_data[column] == category]
        if not matching_transactions.empty:
            amount = self.CalculateAmount(matching_transactions, transaction_type)
            return f"You have spent {round(amount)} for {category.capitalize()}"
        else:
            return f"No transactions found for {category.capitalize()}"
    def retrieve_transaction_total(self, dates, transaction_type):
        """
        Retrieves the total transaction amount based on the type (expense or income) and date parameters.
        
        Parameters:
            transaction_type (str): The type of transaction ("expense" or "income").
            date_parameters (dict): Dictionary of dates to filter the transactions.

        Returns:
            str: A message indicating the total transaction amount for the specified type and dates.
        """
     
        date_list = dates
        if transaction_type.lower() == "expense":
            return self.CalculateExpenseSum(self.data, date_list)
        else:
            return self.CalculateIncomeSum(self.data, date_list)

