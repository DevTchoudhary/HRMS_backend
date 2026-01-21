"""
Vercel entrypoint for FastAPI

IMPORTANT:
- Do NOT create FastAPI app here
- Do NOT add routes here
- Do NOT add uvicorn.run()

This file only exposes the existing FastAPI app
"""

from app.main import app  # imports your already-configured FastAPI app