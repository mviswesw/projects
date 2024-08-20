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
