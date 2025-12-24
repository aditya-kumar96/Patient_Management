from fastapi import FastAPI,Path,HTTPException,Query
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
@app.get("/patient/{patient_id}")
def viewByPatient(patient_id:str = Path(...,title="Patient_Id",description="Patient Id is required",    )) :
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient Id not found')

@app.get('/sort')
def sort_patients( sort_by:str=Query(...,description="sort on the basis of height weight bmi"), order:str = Query('asc',description="sort in asc or desc order") ):
    validfields=['height','wieght','bmi']
    if sort_by not in validfields :
        raise HTTPException(status_code=400,detail="Invalid fields, select from valid fields")
    if order not in ['asc','desc'] :
        raise HTTPException(status_code=400,detail="Invalid order select between asc or desc")
    
    data = load_data()
    
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=True)
    return sorted_data
    