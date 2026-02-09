from fastapi import FastAPI 
import json
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data =json.load(f)
    return data


@app.get("/")
def hello():
    return {"message": "patient management system"}


@app.get("/about")
def about():
    return {"message": "i am a fastapi application"}


@app.get("/view")
def view():
    data = load_data()
    return data

#using specific path/specific user
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    # load all patients
    data = load_data()

    for patient in data["patients"]:
        if patient["id"] == patient_id:
            return patient

    return {"error": "Patient not found"}
