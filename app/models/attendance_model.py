from sqlalchemy import Column, String, Date, ForeignKey, Integer
from app.database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(String, ForeignKey("employees.employee_id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
