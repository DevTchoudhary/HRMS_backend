from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_tables
from app.routes.employee_routes import router as employee_router
from app.routes.attendance_routes import router as attendance_router
from app.routes.dashboard_routes import router as dashboard_router


app = FastAPI(title="HRMS Lite API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow Vercel + local frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    """
    Runs once per server startup.
    Serverless-safe way to initialize DB tables.
    """
    create_tables()


# Register routes
app.include_router(employee_router)
app.include_router(attendance_router)
app.include_router(dashboard_router)


# Health check endpoint
@app.get("/")
def home():
    return {"message": "HRMS Backend Running Successfully"}
