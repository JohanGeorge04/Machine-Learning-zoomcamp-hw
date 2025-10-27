import pickle
from fastapi import FastAPI
from typing import Dict, Any
import uvicorn

app = FastAPI()

with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

client={
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

def predict_single(client):
    result = pipeline.predict_proba(client)[0, 1]
    return float(result)


@app.post("/predict")
def predict(customer: Dict[str, Any]):
    prob = predict_single(customer)
    return {
        "conversion_probability": prob
    }

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)