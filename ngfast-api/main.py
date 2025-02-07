"""Application entry point"""
from fastapi import FastAPI
from config import initialize_database
import logging
from features.users.router import router as users_router
from features.groups.router import router as groups_router
from features.projects.router import router as projects_router
from features.admin.router import router as admin_router
from features.reports.router import router as reports_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Portfolio API",
    description="User and group management with version history",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    """Initialize database on application startup"""
    initialize_database()

# Include routers
app.include_router(users_router)
app.include_router(groups_router)
# app.include_router(projects_router)
app.include_router(admin_router)
app.include_router(reports_router)

@app.get("/", tags=["root"])
def read_root():
    """Welcome endpoint returning API status"""
    return {"message": "Welcome to the Portfolio API"}
