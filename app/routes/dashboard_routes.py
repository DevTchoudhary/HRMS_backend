from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import dashboard_crud

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

# Creates db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Returns dashboard summary
@router.get("/")
def get_dashboard_data(db: Session = Depends(get_db)):

    total_employees = dashboard_crud.get_total_employees(db)
    total_attendance = dashboard_crud.get_total_attendance(db)
    today_present = dashboard_crud.get_today_present(db)

    return {
        "total_employees": total_employees,
        "total_attendance_records": total_attendance,
        "today_present": today_present
    }
