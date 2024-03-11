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
    event['startTimestamp'] = round(event['startTimestamp']) # Round to the nearest second
    event['endTimestamp'] = round(event['endTimestamp']) # Round to the nearest second
    event['startDatetime'] = datetime.datetime.fromtimestamp(event['startTimestamp'])
    event['endDatetime'] = datetime.datetime.fromtimestamp(event['endTimestamp'])
    event['dayOfWeek'] = event['startDatetime'].strftime('%A')  # Full day name (Monday, Tuesday, etc.)
    event['dayOfMonth'] = event['startDatetime'].day
    event['type'] = event['type'].lower()
    event['weekOfYear'] = event['startDatetime'].isocalendar().week


# Sort the data by type and startDatetime
df = pd.DataFrame(raw_data).sort_values(by=['type', 'startTimestamp'])

df = df[df['ultra'] != True]

# Calculate the time between events of the same type (in days)
df['timeBetweenEvents'] = df.groupby('type')['startDatetime'].diff().dt.total_seconds() / 86400


# Sort by startDatetime and reset the index
df = df.sort_values(by='startTimestamp').reset_index(drop=True)


# Calculate the preceding event type when sorted by startDatetime
df['precedingEventType'] = df['type'].shift(1)



# Save the DataFrame to a CSV file
df.to_csv('events_data.csv', index=False)