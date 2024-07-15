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