from sklearn.linear_model import LinearRegression
import joblib
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = [10, 20, 30, 40, 50]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model saved successfully")