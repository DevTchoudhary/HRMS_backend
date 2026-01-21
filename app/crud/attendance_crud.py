from app.models.attendance_model import Attendance

# Saves attendance
def save_attendance(db, attendance_data):
    attendance = Attendance(**attendance_data)
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

# Returns all attendance
def get_all_attendance(db):
    return db.query(Attendance).all()

# Checks duplicate attendance
def find_duplicate_attendance(db, employee_id, date):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        Attendance.date == date
    ).first()

# Returns attendance for specific employee
def get_employee_attendance(db, employee_id):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()

# Returns attendance by date
def filter_by_date(db, date):
    return db.query(Attendance).filter(
        Attendance.date == date
    ).all()

# Counts present days for employee (BONUS)
def count_present_days(db, employee_id):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        Attendance.status == "Present"
    ).count()
