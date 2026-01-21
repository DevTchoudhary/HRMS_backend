from app.models.employee_model import Employee
from app.models.attendance_model import Attendance
from datetime import date

# Returns total employees
def get_total_employees(db):
    return db.query(Employee).count()

# Returns total attendance records
def get_total_attendance(db):
    return db.query(Attendance).count()

# Returns today's present employees
def get_today_present(db):
    today = str(date.today())

    return db.query(Attendance).filter(
        Attendance.date == today,
        Attendance.status == "Present"
    ).count()
