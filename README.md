# Egg Events Prediction

This project is a machine learning model that predicts the type of events in the game Egg, Inc. based on historical event data.

## Project Structure

```- README.md
- src/
    |--- data/
    |       |--- events.json
    |--- feature_extraction.py
    |--- ml.py
    |--- predict.py
    |--- vis.py
```

## Files

-   `events.json`: This file contains the raw event data.
-   `events_data.csv`: This file contains the processed event data used for training the model.
-   `feature_extraction.py`: This script reads the raw event data, extracts relevant features, and saves the processed data to a CSV file.
-   `ml.py`: This script reads the processed event data, trains a Random Forest Classifier, and evaluates its performance.
-   `predict.py`: This script uses the trained model to make predictions on new data.
-   `vis.py`: This script is used for visualizing the data and the results.

## How to Run

1. Run `feature_extraction.py` to process the raw event data.
2. Run `ml.py` to train and evaluate the model.
3. Use `predict.py` to make predictions on new data.

## Features

The model uses the following features for prediction:

-   `dayOfMonth`: Day of the month when the event starts.
-   `dayOfWeekEncoded`: Day of the week when the event starts, encoded as an integer.
-   `typeEncoded`: Type of the event, encoded as an integer.
-   `timeBetweenEvents`: Time between this event and the previous event of the same type, in seconds.
-   `weekOfYear`: Week of the year of the event start (attempting to capture holidays)
-   `eventFrequency`: How often different event types occur

## Model

The model is a Random Forest Classifier trained on 80% of the data, with the remaining 20% used for testing. The model's performance is evaluated based on its accuracy, confusion matrix, and classification report.
