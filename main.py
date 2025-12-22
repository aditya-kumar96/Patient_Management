from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f) 
    return data

@app.get('/')
def hello():
    return {'print':'hello'}

@app.get("/view")
def viewPatients():
    data = load_data()
    return data

