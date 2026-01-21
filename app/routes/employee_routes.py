from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.employee_schema import EmployeeCreate
from app.crud import employee_crud

router = APIRouter(prefix="/employees", tags=["Employees"])

# Provides database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creates new employee
@router.post("/")
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    
    if employee_crud.find_employee_by_id(db, data.employee_id):
        raise HTTPException(status_code=409, detail="Employee ID already exists")

    if employee_crud.find_employee_by_email(db, data.email):
        raise HTTPException(status_code=409, detail="Email already exists")

    employee = employee_crud.save_employee(db, data.dict())

    return {
        "message": "Employee added successfully",
        "data": employee
    }

# Returns list of employees
@router.get("/")
def list_employees(db: Session = Depends(get_db)):
    employees = employee_crud.get_all_employees(db)

    if not employees:
        return {"message": "No employees found", "data": []}

    return {"data": employees}

# Deletes employee
@router.delete("/{employee_id}")
def remove_employee(employee_id: str, db: Session = Depends(get_db)):

    employee = employee_crud.find_employee_by_id(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee_crud.delete_employee(db, employee)

    return {"message": "Employee deleted successfully"}
