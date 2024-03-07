import joblib
import pandas as pd
import datetime
import numpy as np

# Load the trained model
model = joblib.load('trained_model.joblib')
type_encoder = joblib.load('type_encoder.joblib')
dayOfWeek_encoder = joblib.load('dayOfWeek_encoder.joblib')

# Load the historical data
historical_data = pd.read_csv('events_data.csv')

# Calculate the average time between events for each type
average_time_between_events = historical_data.groupby('type')['timeBetweenEvents'].mean()
print(average_time_between_events)

event_data = {
    "startDatetime": datetime.datetime(2024, 3, 7, 17, 0),  # Replace with the actual start time
    # Add other relevant information for the event
}


# Convert event data to DataFrame
event_df = pd.DataFrame([event_data])

# print(event_df['startDatetime'])


# Extract day of the week, day within the month, and hour of the day
event_df['dayOfWeek'] = event_df['startDatetime'].dt.day_name()
event_df['dayOfMonth'] = event_df['startDatetime'].dt.day

# Encode categorical features
event_df['dayOfWeekEncoded'] = dayOfWeek_encoder.transform(event_df['dayOfWeek'])

# Initialize a variable to store the best prediction and its probability
best_prediction = None
best_probability = -np.inf

# Iterate over each event type
for type_encoded in range(len(type_encoder.classes_)):
    # Set the typeEncoded and timeBetweenEvents for the current event type
    event_df['typeEncoded'] = type_encoded
    event_df['timeBetweenEvents'] = average_time_between_events[type_encoded]

    # Select relevant features for prediction
    prediction_features = ['dayOfMonth', 'dayOfWeekEncoded', 'typeEncoded', 'timeBetweenEvents']

    event_features = event_df[prediction_features]

    # Make predictions
    predicted_event_type = model.predict(event_features)
    predicted_probability = model.predict_proba(event_features).max()

    print(type_encoder.inverse_transform(predicted_event_type), predicted_probability)

    # If this prediction has a higher probability than the current best, update the best prediction
    if predicted_probability > best_probability:
        best_prediction = predicted_event_type
        best_probability = predicted_probability

# Decode the best predicted label
best_predicted_event_type_decoded = type_encoder.inverse_transform(best_prediction)[0]

# Display the prediction
print(f"The predicted event type for March 7, 2024, at 17:00 is: {predicted_event_type_decoded}")