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

# Visualize the distribution of events by hour of the day
plt.figure(figsize=(12, 6))
sns.countplot(x='hourOfDay', data=df)
plt.title('Distribution of Events by Hour of the Day')
plt.show()

# Explore specific event types by day of the week
plt.figure(figsize=(14, 8))
sns.countplot(x='dayOfWeek', hue='type', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Distribution of Event Types by Day of the Week')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()

# Explore specific event types by hour of the day
plt.figure(figsize=(14, 8))
sns.countplot(x='hourOfDay', hue='type', data=df)
plt.title('Distribution of Event Types by Hour of the Day')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()
