import quixstreams as qx
import pandas as pd
import numpy as np
import os


class QuixFunction:
    def __init__(self, consumer_stream: qx.StreamConsumer, producer_stream: qx.StreamProducer, model):
        self.consumer_stream = consumer_stream
        self.producer_stream = producer_stream
        # Load the autoencoder model from the file
        self.model = model
    # Callback triggered for each new event
    def on_event_data_handler(self, stream_consumer: qx.StreamConsumer, data: qx.EventData):
        print(data.value)
        # Transform your data here.
        self.producer_stream.events.publish(data)

    # Callback triggered for each new parameter data.
    def on_dataframe_handler(self, stream_consumer: qx.StreamConsumer, df: pd.DataFrame):
        # Normalize the anomalous data
        print(df)
        df = df.set_index('timestamp')
        anom_data = df.drop(columns=['machineID'])


        # Use the Autoencoder to predict on the anomalous data
        predictions = self.model.predict(anom_data)

        # Calculate reconstruction error for each sequence
        mse = np.mean(np.power(anom_data.values[-predictions.shape[0]:] - predictions[:, -1, :], 2), axis=1)

        # Scale the MSE to a percentage
        min_mse = np.min(mse)
        max_mse = np.max(mse)
        mse_percentage = ((mse - min_mse) / (max_mse - min_mse)) * 100


        # Detect anomalies by comparing the scaled reconstruction error to some threshold
        threshold = float(os.environ["threshold"])  # Define a threshold value (in percentage)

        # Add 'is_anomalous' column to the DataFrame
        df['is_anomalous'] = mse_percentage > threshold
        df['mse_percentage'] = mse_percentage


        df = df.reset_index().rename(columns={'timestamp': 'time'})
        print(df)


        self.producer_stream.timeseries.buffer.publish(df)  # Send filtered data to output topic›
