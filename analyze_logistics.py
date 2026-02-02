import pandas as pd

# Load the data
df = pd.read_csv('shipments.csv')

# 1. Convert columns to datetime objects
df['planned_ship_date'] = pd.to_datetime(df['planned_ship_date'])
df['actual_ship_date'] = pd.to_datetime(df['actual_ship_date'])

# 2. Calculate the Delay (Actual - Planned)
df['delay_days'] = (df['actual_ship_date'] - df['planned_ship_date']).dt.days

# 3. Categorize the performance using a Lambda function (Bonus Skill!)
df['status'] = df['delay_days'].apply(lambda x: 'Late' if x > 0 else 'On-Time')

print("--- Logistics Analysis Report ---")
print(df)

# Save for our SQL Join later
df.to_csv('logistics_results.csv', index=False)
