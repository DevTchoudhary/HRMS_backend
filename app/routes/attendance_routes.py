from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.attendance_schema import AttendanceCreate
from app.crud import attendance_crud, employee_crud

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

# Creates and returns database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Marks attendance for employee
@router.post("/")
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):

    employee = employee_crud.find_employee_by_id(db, data.employee_id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee does not exist"
        )

    duplicate = attendance_crud.find_duplicate_attendance(
        db, data.employee_id, data.date
    )
    if duplicate:
        raise HTTPException(
            status_code=409,
            detail="Attendance already marked for this date"
        )

    attendance_record = attendance_crud.save_attendance(
        db, data.dict()
    )

    return {
        "message": "Attendance marked successfully",
        "data": attendance_record
    }

# Returns attendance by date
@router.get("/date/{attendance_date}")
def get_attendance_by_date(
    attendance_date: str,
    db: Session = Depends(get_db)
):

    records = attendance_crud.filter_by_date(
        db, attendance_date
    )

    if not records:
        return {
            "message": "No attendance found for this date",
            "data": []
        }

    return {"data": records}

# Returns all attendance records
@router.get("/")
def get_all_attendance(db: Session = Depends(get_db)):

    records = attendance_crud.get_all_attendance(db)

    if not records:
        return {
            "message": "No attendance records found",
            "data": []
        }

    return {"data": records}

# Returns attendance for specific employee
@router.get("/{employee_id}")
def get_employee_attendance(
    employee_id: str,
    db: Session = Depends(get_db)
):

    records = attendance_crud.get_employee_attendance(
        db, employee_id
    )

    if not records:
        raise HTTPException(
            status_code=404,
            detail="No attendance found for this employee"
        )

    return {"data": records}

# Returns total present days (BONUS)
@router.get("/present/{employee_id}")
def get_total_present_days(
    employee_id: str,
    db: Session = Depends(get_db)
):

    count = attendance_crud.count_present_days(
        db, employee_id
    )

    return {
        "employee_id": employee_id,
        "total_present_days": count
    }
