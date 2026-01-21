from sqlalchemy import Column, String
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)
