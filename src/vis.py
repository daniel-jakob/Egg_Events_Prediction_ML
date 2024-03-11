import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the DataFrame from the CSV file
df = pd.read_csv('events_data.csv')

# Explore the DataFrame
print(df.head())


# Visualize event types distribution
plt.figure(figsize=(12, 6))
sns.countplot(x='type', data=df)
plt.title('Distribution of Event Types')
plt.xticks(rotation=45)
plt.show()

# Visualize day of the week distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='dayOfWeek', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Distribution of Events by Day of the Week')
plt.show()

# Explore specific event types by day of the week
plt.figure(figsize=(14, 8))
sns.countplot(x='dayOfWeek', hue='type', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Distribution of Event Types by Day of the Week')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()

# Filter the DataFrame to only include 'prestige-boost' events
prestige_boost_events = df[df['type'] == 'prestige-boost']

# Plot a histogram of the time between events
plt.figure(figsize=(10, 6))
sns.histplot(prestige_boost_events['timeBetweenEvents'], bins=30, kde=True)
plt.title('Distribution of Time Between "prestige-boost" Events')
plt.xlabel('Time Between Events (days)')
plt.ylabel('Frequency')
plt.show()