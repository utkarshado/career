from fastapi import FastAPI
import joblib

app = FastAPI(docs_url="/firstapi")
model = joblib.load(BASE_DIR / "model" / "model.pkl")

@app.get("/")
def home():
    return {"message": "Career Predictor API"}

@app.post("/predict")
def predict(data: dict):
    features = [[
        data["prog"], data["math"], data["comm"],
        data["creative"], data["logic"],
        data["tech"], data["business"], data["cgpa"]
        
    ]]
    
    prediction = model.predict(features)
    
    return {"career": prediction[0]}
