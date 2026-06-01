import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    data = pd.read_csv("data/cost_data.csv")

    X = data[['area']]
    y = data['cost']

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_cost(model, area):
    prediction = model.predict([[area]])
    return prediction[0]