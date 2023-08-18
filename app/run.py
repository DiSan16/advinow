import uvicorn
from fastapi import FastAPI, Query # need python-multipart
from app.views import router
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal
import csv


app = FastAPI(title="AdviNow Interview Challenge", version="1.6")

app.include_router(router)

@app.post("/import-csv/")
async def import_csv():
    csv_file_path = "app/data/business_symptom_data.csv"
    print("Yes1")
    db = SessionLocal()

    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:

        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Read the header line

        for row in csv_reader:
            # Process each row of data here
            fields = row.split(",")
            business_id, business_name, symptom_code, symptom_name, symptom_diagnostic = fields
    
            symptom = Symptom(business_id=business_id,
                              business_name=business_name,
                              code=symptom_code,
                              name=symptom_name,
                              diagnostic=symptom_diagnostic)

            db.add(symptom)
        db.commit()
        db.close()

    return {"message": "CSV file processed successfully"}

@app.get("/symptoms/")
async def get_symptoms(
    business_id: int = Query(None, title="Business ID"),
    diagnostic: str = Query(None, title="Diagnostic")
):
    db = SessionLocal()
    query = db.query(models.Symptom)
    
    if business_id is not None:
        query = query.filter(models.Symptom.business_id == business_id)
    if diagnostic is not None:
        query = query.filter(models.Symptom.diagnostic == diagnostic)
    
    symptoms = query.all()
    return symptoms


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8013)
