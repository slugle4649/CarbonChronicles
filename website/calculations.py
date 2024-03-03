import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

class stats():
    # Getting datasets
    def __init__(self, filename):
        self.data = pd.read_csv(os.path.join('website', 'data', filename))
        self.CO2 = {}
        self.rank = {}
        for j in range(len(self.data)):
            self.CO2[self.data['name'][j]] = self.data[' metric tonnes of CO2'][j]
            self.rank[self.data['name'][j]] = self.data['ranking'][j]

    # Calculating statistics
    def calc(self, country):
        calcs = {}
        CO2 = self.CO2[country].replace(',', '')
        # Carbon emissions equivalent to 
        calcs['calgasoline_gallons'] = int(CO2) * 113.0
        calcs['passenger_miles'] = int(CO2) * 2564.0
        calcs['smartphones_charged'] = int(CO2) * 121643.0

        # Amount needed to sequest carbon emissions
        calcs['USforest_acres'] = int(CO2) * 1.2

        # Counteracting emissions 
        calcs['trashbags_recycled'] = int(CO2) * 43.3
        calcs['windturbines_running'] = int(CO2) * 0.0003

        return calcs


class ai():
    # Defining model and data
    def __init__(self, filename):
        self.data = pd.read_csv(os.path.join('website', 'data', filename))

        self.X = (self.data['year'].values).reshape(-1, 1)
        self.y = (self.data['trend'].values).reshape(-1, 1)
        self.model = LinearRegression()
    
    # Converts figure to png to send to html
    def fig_to_png(self, fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        return base64.b64encode(buf.getvalue()).decode('utf-8')

    def train(self):
        # Splits the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Trains the linear regression model
        self.model.fit(X_train, y_train)

        # Making predictions
        y_pred_test = self.model.predict(X_test)

        # Visualizes the results
        fig, ax = plt.subplots(figsize=(5, 4), dpi=200)  # Adjust the figure size as needed
        ax.scatter(X_test, y_test, color='blue', label='Actual CO2 Emissions Per Year')  # Label for actual data points
        ax.plot(X_test, y_pred_test, color='red', label='Predicted CO2 Emissions Over Time')  # Label for predicted trend line
        ax.set_title('CO2 Trends Prediction')
        ax.set_xlabel('Year')
        ax.set_ylabel('CO2 Emissions')

        # Setting appropriate axis limits
        ax.set_xlim(min(self.X), max(self.X))
        ax.set_ylim(min(self.y), max(self.y))

        # Rotating x-axis labels for better readability if needed
        plt.xticks(rotation=45)
        ax.legend()

        plt.tight_layout()
        img_data = self.fig_to_png(fig)
        plt.close(fig)

        # Returns image as png represented by base64 value
        return img_data


    def predict(self, year):
        # Time range for future predictions
        future_years = np.arange(2025, year)
        future_years = future_years.reshape(-1,1)
            
        # Fits a linear regression model
        self.model.fit(self.X, self.y)

        # Making predictions for future years
        future_predictions = self.model.predict(future_years)

        # Plots the future predictions
        fig, ax = plt.subplots(figsize=(5, 4), dpi=200)
        ax.plot(self.X, self.y, color='blue', label='Historical CO2 Emissions')
        ax.scatter(future_years, future_predictions, color='red', label='Predicted CO2 Emissions Per Year')
        ax.set_title('Future CO2 Emissions Predictions')
        ax.set_xlabel('Year')
        ax.set_ylabel('CO2 Emissions')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        img_data = self.fig_to_png(fig)
        plt.close(fig)

        # Returns image as png represented by base64 value
        return img_data
