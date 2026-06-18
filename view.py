from fastapi import FastAPI
import json

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Patient Management System"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()
    return data