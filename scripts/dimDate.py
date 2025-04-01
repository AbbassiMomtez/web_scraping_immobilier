import pandas as pd
from datetime import datetime, timedelta

# Define start and end date
start_date = datetime(2000, 1, 1)
end_date = datetime(2030, 12, 31)

# Generate date range
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Create dataframe
df = pd.DataFrame({'date': date_range})
df['date_key'] = df['date'].dt.strftime('%Y%m%d')  # Primary key
df['year'] = df['date'].dt.year
df['quarter'] = df['date'].dt.quarter
df['month'] = df['date'].dt.month
df['month_name'] = df['date'].dt.strftime('%B')
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday + 1  # Monday = 1, Sunday = 7
df['weekday_name'] = df['date'].dt.strftime('%A')
df['is_weekend'] = df['weekday'].isin([6, 7])
df['is_holiday'] = False  # You can add holiday logic here

df.to_csv('../data/dim_date.csv', index=False)

print("Date dimension CSV generated successfully!")