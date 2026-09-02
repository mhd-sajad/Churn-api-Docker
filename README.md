
```markdown
# 🔮 Customer Churn Prediction API

A production-ready inference microservice developed by Muhammed Sajad, predicting the probability of customer churn in real-time. This project is a core implementation within the broader MACHINE LEARNING JOURNEY[cite: 2], demonstrating the transition from local model development to a fully containerized, cloud-hosted architecture[cite: 14].

---

## 🌐 Live Service & Interactive Documentation

The service is continuously deployed and hosted on Render:

* **Live Base URL:** [https://churn-prediction-api-edu0.onrender.com/](https://churn-prediction-api-edu0.onrender.com/)
* **Interactive Swagger UI:** [https://churn-prediction-api-edu0.onrender.com/docs](https://churn-prediction-api-edu0.onrender.com/docs)
* **ReDoc Documentation:** [https://churn-prediction-api-edu0.onrender.com/redoc](https://churn-prediction-api-edu0.onrender.com/redoc)

---

## 🏗️ Architecture & Tech Stack

* **Framework:** FastAPI (ASGI) for asynchronous, high-throughput request handling[cite: 14].
* **Machine Learning:** `scikit-learn` Pipeline (StandardScaler + Logistic Regression), explicitly chosen for its high interpretability and transparent probability scoring in critical decision-making. 
* **Data Validation:** Pydantic models for strict runtime type enforcement and bounds checking[cite: 14].
* **Containerization:** Docker multi-stage configuration using a minimal `python:3.10-slim` base image.
* **Hosting:** Cloud deployment via Render, executing automated builds from the GitHub repository.

---

## 📁 Project Structure

```text
churn-prediction-api/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI entry point, lifespan events & routing[cite: 14]
│   └── schemas.py         # Pydantic input/output validation models[cite: 14]
├── models/
│   └── churn_model.pkl    # Serialized scikit-learn pipeline (auto-generated during build)
├── Dockerfile             # Container build blueprint
├── .dockerignore          # Docker build exclusion rules
├── requirements.txt       # Locked project dependencies
├── train.py               # Automated pipeline training & serialization script
├── .gitignore
└── README.md

```

---

## 📊 Input Features & Validation Rules

| Feature | Type | Constraints | Description |
| --- | --- | --- | --- |
| `age` | `int` | `> 17` | Customer age in years |
| `tenure` | `int` | `≥ 0` | Months subscribed with the service |
| `monthly_charges` | `float` | `> 0.0` | Monthly billing amount (USD) |
| `num_products` | `int` | `1 – 10` | Total number of subscribed services |
| `has_internet` | `int` | `0 or 1` | Internet service access flag |

---

## 🔌 API Endpoints & Contracts

### 1. Health Check

* **Route:** `GET /`
* **Response:**
```json
{
  "status": "200 OK",
  "message": "Churn Prediction API is healthy and model is loaded."
}

```



### 2. Churn Prediction

* **Route:** `POST /predict`
* **Request Payload:**
```json
{
  "age": 27,
  "tenure": 2,
  "monthly_charges": 89.5,
  "num_products": 1,
  "has_internet": 1
}

```


* **Success Response (`200 OK`):**
```json
{
  "status": "success",
  "churn_prediction": true,
  "verdict": "Will Churn",
  "churn_probability": 0.8321
}

```



---

## 🚀 Local Deployment Options

### Option A: Run via Docker (Recommended)

1. **Build the Docker Image:**
```bash
docker build -t churn-prediction-api:v1 .

```


2. **Run the Container:**
```bash
docker run -d -p 8000:8000 --name churn_api churn-prediction-api:v1

```


3. **Access the API:**
Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

---

### Option B: Run Locally with Python Virtual Environment

1. **Create and Activate Environment:**
```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

```


2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Train the Pipeline:**
```bash
python train.py

```


4. **Start the ASGI Server:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

```



---

## 🛡️ Error Handling & Status Codes

| Status Code | Reason | Cause |
| --- | --- | --- |
| `200 OK` | Success | Valid input processed through the inference pipeline. |
| `422 Unprocessable Entity` | Validation Error | Malformed JSON, incorrect data types, or out-of-bounds input values.

 |
| `500 Internal Server Error` | Execution Failure | Missing `.pkl` artifact or runtime inference exception.

 |

```

Would you like to run through a quick mock interview scenario to practice explaining this specific API architecture to your industry reviewer?

```
