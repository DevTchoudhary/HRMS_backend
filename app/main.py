from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_tables
from app.routes.employee_routes import router as employee_router
from app.routes.attendance_routes import router as attendance_router
from app.routes.dashboard_routes import router as dashboard_router


app = FastAPI(title="HRMS Lite API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, DELETE, OPTIONS etc)
    allow_headers=["*"],  # Allow all headers
)

# Creates tables on server start
create_tables()

# Register routes
app.include_router(employee_router)
app.include_router(attendance_router)
app.include_router(dashboard_router)


# Health check endpoint
@app.get("/")
def home():
    return {"message": "HRMS Backend Running Successfully"}
