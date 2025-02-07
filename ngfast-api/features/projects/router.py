"""Project management routes"""
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from datetime import datetime
import json
from .models import Project, ProjectVersion  # Assuming these exist
from config.database import get_db  # Updated import path
from .queries import INSERT_PROJECT, INSERT_PROJECT_VERSION  # Assuming we'll create these

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=List[Project])
def get_projects():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return projects

@router.get("/{project_id}", response_model=Project)
def get_project(project_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
    project = cursor.fetchone()
    conn.close()
    
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return project 