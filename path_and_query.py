from fastapi import FastAPI,Path,Query
import json
app = FastAPI()
def load_data():
    with open("patient.json",'r') as f:
        data = json.load(f)
    return data
@app.get("/view")
def view():
    data = load_data()
    return data
#Path Parameters
#We can path function to
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(...,description="ID of the Patient",example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error" : "patient not found"}
#Query Parameters
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of weight_kg, height_cm, bmi"
    ),
    order: str = Query(
        "asc",
        description="Sort in ascending or descending order"
    )
):
    valid_fields = ["weight_kg", "height_cm", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Choose from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be either 'asc' or 'desc'"
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data