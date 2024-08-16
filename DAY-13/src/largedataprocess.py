import pandas as pd

# read
df = pd.read_csv("/Users/meenu/SPHARK/Training/DAY-13/data/equity_data.csv")


print(f"\n=======1. df.head() ======= \n{df.head()} TAIL \n{df.tail()} ")
print(f"\n=======2. df.dtypes =======\n{df.dtypes}") # metadata of the data set is stored which automatically populates the datatype
print(f"\n=======3. df.columns =======\n{df.columns}")
dtype_dict = {
    'created_at': 'datetime',
    'user_id': 'int',
    'asset_symbol': 'str',
    'spot_price': 'float',
    'balance': 'float',
    'robo_balance': 'float',
    'upl': 'float',
    'equity': 'float',
    'amount_usd': 'float'
}

# print(df['equity'].max())
print(f'\n=======4. df.describe() =======- \n{df.describe()}')
print(f'\n=======5. df.info() =======-\n{df.info()}') 

print(f"\n {df['asset_symbol'].unique()}")

"""
HW
1. find avg user balance in the entire data
2. find avg of each individual user
3. splitting he data where the threshold is avg value for all users
4. balance - see if balance of the filtered users have increased atleast by 3-4 datapoints (data is collected every 6 hrs) - 'equity'
5. Find users that have maximum balance (example - collect top 10 users)
"""