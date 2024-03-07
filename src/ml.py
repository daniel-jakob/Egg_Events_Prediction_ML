import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Read the DataFrame from the CSV file
df = pd.read_csv('events_data.csv')



# Feature Engineering: Encode categorical features
type_encoder = LabelEncoder()
df['typeEncoded'] = type_encoder.fit_transform(df['type'])

dayOfWeek_encoder = LabelEncoder()
df['dayOfWeekEncoded'] = dayOfWeek_encoder.fit_transform(df['dayOfWeek'])


# Select relevant features for the model
features = ['dayOfMonth', 'dayOfWeekEncoded', 'typeEncoded', 'timeBetweenEvents', 'weekOfYear']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df['typeEncoded'], test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Display results
print(f"Accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(classification_rep)

# Save the model to a file
joblib.dump(model, 'trained_model.joblib')
joblib.dump(type_encoder, 'type_encoder.joblib')
joblib.dump(dayOfWeek_encoder, 'dayOfWeek_encoder.joblib')

