import joblib
import pandas as pd
import datetime

# Load the trained model
model = joblib.load('trained_model.joblib')
type_encoder = joblib.load('type_encoder.joblib')
dayOfWeek_encoder = joblib.load('dayOfWeek_encoder.joblib')

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

event_df['typeEncoded'] = 0  # Replace 0 with a placeholder value if needed

# event_df['timeBetweenEvents'] = time_between_events



# Select relevant features for prediction
# prediction_features = ['dayOfMonth', 'dayOfWeekEncoded', 'typeEncoded', 'timeBetweenEvents']
prediction_features = ['dayOfMonth', 'dayOfWeekEncoded', 'typeEncoded']

print(event_df[prediction_features])

event_features = event_df[prediction_features]

# Make predictions
predicted_event_type = model.predict(event_features)

# Decode the predicted label if necessary
predicted_event_type_decoded = type_encoder.inverse_transform(predicted_event_type)[0]

# Display the prediction
print(f"The predicted event type for March 7, 2024, at 17:00 is: {predicted_event_type_decoded}")