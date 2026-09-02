from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
import pandas as pd
from app.schemas import CustomerInput

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts whether a customer is likely to churn based on their profile.",
    version="1.0.0"
)

try:
    model = joblib.load('models/churn_model.pkl')
    print("Churn model loaded successfully.")
except Exception as e:
    model = None
    print(f"Warning: Model failed to load: {e}")


@app.get("/", tags=["Health"])
def health_check():
    """Basic health check to confirm the API is alive and the model is loaded."""
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="API is running, but churn model is missing. Run train.py first."
        )
    return {
        "status": "200 OK",
        "message": "Churn Prediction API is healthy and model is loaded."
    }


@app.post("/predict", tags=["Prediction"])
def predict_churn(customer: CustomerInput):
    """
    Predicts customer churn probability.

    - **age**: Customer's age
    - **tenure**: Months with the company
    - **monthly_charges**: Monthly billing amount (USD)
    - **num_products**: Number of subscribed products
    - **has_internet**: Internet service flag (0 or 1)
    """
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Server Error: Churn model is not loaded."
        )

    try:
        # input_data = np.array([[
        #     customer.age,
        #     customer.tenure,
        #     customer.monthly_charges,
        #     customer.num_products,
        #     customer.has_internet
        # ]])

        input_data = pd.DataFrame([customer.model_dump()])

        prediction = int(model.predict(input_data)[0])
        probability = float(model.predict_proba(input_data)[0][1])

        verdict = "Will Churn" if prediction == 1 else "Will Stay"

        return {
            "status": "success",
            "churn_prediction": bool(prediction),
            "verdict": verdict,
            "churn_probability": round(probability, 4)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )