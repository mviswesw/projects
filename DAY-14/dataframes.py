import pandas as pd
# read
df = pd.read_csv("/Users/meenu/SPHARK/Training/DAY-13/data/equity_data.csv")


"""
HW
1. find avg user balance in the entire data
2. find avg of each individual user
3. splitting the data where the threshold is avg value for all users
4. balance - see if balance of the filtered users have increased atleast by 3-4 datapoints (data is collected every 6 hrs) - 'equity'
5. Find users that have maximum balance (example - collect top 10 users)
"""

"""
1.find avg user balance in the entire data
"""
avg = df['balance'].mean()
print(f"\n1.Average user balance in entire data ${avg}")

"""
2. find avg of each individual user
"""
# users = df['user_id'].unique()
# print(len(users))

# df.groupby('user_id')['balance'].mean().reset_index()
df_avg_each = df.groupby('user_id')['balance'].mean().reset_index()
print(f"\n2.find avg balance of each individual user \n{df_avg_each.head()}")
# print(df_avg_each.head())

"""
3. splitting the data where the threshold is avg value for all users
"""
split_df_by_threshold = df[df['balance'] >= avg].reset_index()
print(split_df_by_threshold.head())

