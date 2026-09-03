from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('model.pkl')

class Model(BaseModel):
    no : int

@app.get('/')
def home():
    return{
        "message": "Model is Healthy and Working"
    }

@app.post('/predict')
def pred(data:Model):
    input = np.array([[data.no]])
    res = int(model.predict(input)[0])
    return {
        "Result": int(res)
    } 