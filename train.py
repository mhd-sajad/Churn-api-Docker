# train.py — Run this once to generate the model file
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import numpy as np
import os

# ─── Synthetic training data ───────────────────────────────────────────────────
# Features: [age, tenure, monthly_charges, num_products, has_internet]
X = np.array([
    [22,  2, 75.5, 1, 1],   # Young, new, high bill, single product → likely churn
    [30,  6, 50.0, 2, 1],
    [45, 24, 40.0, 3, 1],   # Established customer → likely stay
    [52, 36, 30.0, 4, 0],
    [27,  1, 90.0, 1, 1],   # Brand new, very high bill → likely churn
    [60, 48, 25.0, 5, 0],   # Long tenure, low charges → very likely stay
    [35, 12, 60.0, 2, 1],
    [29,  3, 85.0, 1, 1],
])

# Labels: 1 = Churned, 0 = Stayed
y = np.array([1, 1, 0, 0, 1, 0, 0, 1])

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(random_state=42))
])

pipeline.fit(X, y)

os.makedirs('models', exist_ok=True)

joblib.dump(pipeline, 'models/churn_model.pkl')
print("✅ Churn model pipeline saved to models/churn_model.pkl!")
