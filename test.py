from datetime import datetime
import pandas as pd

new_transaction_df = pd.DataFrame([[1,2,3,4,5,6,7,8,9]],columns=["Date","Time","Item","Currency","Amount","Paid by","For","Split","to HKD"])
print(new_transaction_df.head())
#print(type(tuple(currencies_dict.keys())))