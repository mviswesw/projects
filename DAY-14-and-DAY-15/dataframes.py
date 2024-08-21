import pandas as pd
from decimal import Decimal
# read
df = pd.read_csv("/Users/meenu/SPHARK/Training/DAY-14-and-DAY-15/data/equity_data.csv")


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
print(f"\n1.i. Average user balance in entire data ${avg}")
print(f"1.ii. total {len(df)}")
"""
2. find avg of each individual user
"""
# users = df['user_id'].unique()
# print(len(users))

# df.groupby('user_id')['balance'].mean().reset_index()
# df_avg_each = df.groupby('user_id')['balance'].mean().reset_index()
# Calculate the average balance for each user
df_avg_balance = df.groupby('user_id')['balance'].mean().reset_index()
df_avg_balance.rename(columns={'balance': 'avg_balance'}, inplace=True)
# Merge the average balance back with the original DataFrame
df_avg_each = pd.merge(df, df_avg_balance, on='user_id')
print(f"\n2.find avg balance of each individual user \n{df_avg_each}")
# print(df_avg_each.head())

"""
3. splitting the data where the threshold is avg value for all users
"""
# Filter the DataFrame where the balance is above or equal to the threshold
unique_users_with_balance_above_threshold = df_avg_each[df_avg_each['balance'] >= 1000].reset_index(drop=True)

print(unique_users_with_balance_above_threshold)

# unique_users_with_balance_above_threshold = df_avg_each[df_avg_each['balance'] >= avg].reset_index()
print(f"3.i. Splitting data where the threshold is avg value for all users {unique_users_with_balance_above_threshold}")

users_with_balance_above_threshold_at_all_times  = df[df['balance'] >= avg ].reset_index()
users_with_balance_above_threshold_at_all_times_u = users_with_balance_above_threshold_at_all_times['user_id'].unique()
print(type(users_with_balance_above_threshold_at_all_times_u))
print(f"3.ii. Splitting data where the threshold is avg value for all users at all times {len(users_with_balance_above_threshold_at_all_times_u)}")

"""
3.a Create mock data using 10 -15 rows
"""
# mockdata_df = df.head(100000)
# print(mockdata_df)
# print(f"unique users {len(mockdata_df['user_id'].unique())}")
# df_avg_each_mock = mockdata_df.groupby('user_id')['balance'].mean().reset_index()
# print(f"\n2.find avg balance of each individual user \n{df_avg_each_mock}")
# filer_mock = df_avg_each_mock[df_avg_each_mock['balance'] > avg]
# print(f"Folter beyond $100 {filer_mock}")

"""
4. balance - see if balance of the filtered users have increased atleast by 3-4 datapoints (data is collected every 6 hrs) - 'equity'

"""
# print thser IDs who have been consistently inproving in profits 

set1 = set(unique_users_with_balance_above_threshold['user_id'])
set2 = set(users_with_balance_above_threshold_at_all_times_u)

# Find the intersection
common_data = set1.intersection(set2)

print("4. \nCount Common data:", len(common_data))

# for users in users_with_balance_above_threshold_at_all_times_u filter user_id whose equity is incremental for next 3 timestamps
# find unique_users_with_balance_above_threshold subtract users_with_balance_above_threshold_at_all_times_u
# df[unique_users_with_balance_above_threshold['user_id'] == users_with_balance_above_threshold_at_all_times_u['user_id']]
# Convert created_at to datetime if it's not already
# df['created_at'] = pd.to_datetime(df['created_at'])
# Function to find users with increasing balance for 3 consecutive timestamps
"""def find_increasing_balances(df):
    results = []
    grouped = df.groupby('user_id')

    for user_id, group in grouped:
        # Check if the balance is increasing for 3 consecutive timestamps
        for i in range(len(group) - 2):
            if (group.iloc[i + 1]['balance'] > group.iloc[i]['balance'] and
                group.iloc[i + 2]['balance'] > group.iloc[i + 1]['balance']):
                results.append(group.iloc[i:i + 3])
                
    return pd.concat(results) if results else pd.DataFrame()"""
def find_increasing_balances(df, consecutive_points=20):
    """
    Find all instances where the balance increases for a specified number of consecutive timestamps.

    Parameters:
    - df: DataFrame with columns 'user_id', 'created_at', and 'balance'.
    - consecutive_points: Number of consecutive timestamps to check for increasing balances.

    Returns:
    - DataFrame with all rows where balance increased for the specified number of consecutive timestamps.
    """
    results = []
    grouped = df.groupby('user_id')

    for user_id, group in grouped:
        # Ensure the DataFrame is sorted by 'created_at'
        group = group.sort_values(by='created_at')
        
        # Check if the balance is increasing for 'consecutive_points' timestamps
        for i in range(len(group) - consecutive_points + 1):
            # Check if the balance increases for consecutive_points timestamps
            increasing = True
            for j in range(consecutive_points - 1):
                if group.iloc[i + j + 1]['balance'] <= group.iloc[i + j]['balance']:
                    increasing = False
                    break
            if increasing:
                results.append(group.iloc[i:i + consecutive_points])
                
    return pd.concat(results) if results else pd.DataFrame()


# Apply the function
increasing_balances_df = find_increasing_balances(unique_users_with_balance_above_threshold)
print(f"\n Increaasin balances {increasing_balances_df.head()}")
unique_users_df = increasing_balances_df.drop_duplicates(subset='user_id')
unique_users_df.to_csv("WORTH_USERS.csv")

"""
5. Find users that have maximum balance (example - collect top 10 users)
"""
top_10 = df.groupby('user_id')['balance'].max().reset_index()
# top_10_dataframe = top_10.to_frame(name='balance')
print(f"5. top 10 users \n{top_10['balance'].max()}")
top_sorted = top_10.sort_values(by='balance',ascending=False)
top_sorted['balance'].dtype

top_sorted['balance'] = top_sorted['balance'].apply(Decimal)
print(f"sorted {top_sorted.head(2500)}")
top_sorted.head(2500).to_csv("sorted_to_100_users.csv")