from fastapi import APIRouter
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal
import csv

router = APIRouter()


@router.get('/status')
async def get_status():
    try:
        return {"Health OK"}

    except Exception as e:
        return {'Error: ' + str(e)}
    


@router.post("/import-csv/")
async def import_csv():
    try:
        csv_file_path = "app/data/business_symptom_data.csv"
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
    
    except Exception as e:
        return {'Error: ' + str(e)}
