import datetime
import pandas as pd
import json
import os

# Path to the JSON file
file_path = os.path.join('data', 'events.json')

# Read the JSON file
with open(file_path, 'r') as file:
    raw_data = json.load(file)

# Convert timestamps to datetime objects and extract day of the week
for event in raw_data:
    event['endTimestamp'] = round(event['endTimestamp']) # Round to the nearest second
    event['startDatetime'] = datetime.datetime.fromtimestamp(event['startTimestamp'])
    event['endDatetime'] = datetime.datetime.fromtimestamp(event['endTimestamp'])
    event['dayOfWeek'] = event['startDatetime'].strftime('%A')  # Full day name (Monday, Tuesday, etc.)
    event['dayOfMonth'] = event['startDatetime'].day
    event['type'] = event['type'].lower()
    event['weekOfYear'] = event['startDatetime'].isocalendar().week


# Sort the data by type and startDatetime
df = pd.DataFrame(raw_data).sort_values(by=['type', 'startDatetime'])

df = df[df['ultra'] != True]

# Calculate the time between events of the same type
df['timeBetweenEvents'] = df.groupby('type')['startDatetime'].diff().dt.total_seconds()


# Save the DataFrame to a CSV file
df.to_csv('events_data.csv', index=False)