from app.models.employee_model import Employee

# Saves new employee in database
def save_employee(db, employee_data):
    employee = Employee(**employee_data)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

# Returns list of all employees
def get_all_employees(db):
    return db.query(Employee).all()

# Finds employee by id
def find_employee_by_id(db, employee_id):
    return db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

# Finds employee by email
def find_employee_by_email(db, email):
    return db.query(Employee).filter(
        Employee.email == email
    ).first()

# Deletes employee from database
def delete_employee(db, employee):
    db.delete(employee)
    db.commit()
