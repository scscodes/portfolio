"""Router for membership report endpoints"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime

from config.database import get_db
from .service import ReportService
from .models import MembershipReport
from .schemas import (
    ReportRequest,
    ReportResponse,
    DetailedReportResponse,
    GroupSnapshotResponse,
    UserSnapshotResponse
)

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.post("/", response_model=ReportResponse)
def generate_report(request: ReportRequest, db: Session = Depends(get_db)):
    """Generate a new report"""
    service = ReportService(db)
    return service.generate_report(request)

@router.get("/{report_id}", response_model=DetailedReportResponse)
def get_report(report_id: int, db: Session = Depends(get_db)):
    """Get a specific report"""
    service = ReportService(db)
    report = service.get_report(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.get("/", response_model=List[ReportResponse])
async def list_reports(
    report_type: Optional[str] = Query(None),
    target_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    from_date: Optional[datetime] = Query(None),
    to_date: Optional[datetime] = Query(None),
    limit: int = Query(default=50, le=100),
    offset: int = Query(default=0),
    db: Session = Depends(get_db)
) -> List[ReportResponse]:
    """
    List reports with optional filtering
    """
    query = db.query(MembershipReport)
    
    if report_type:
        query = query.filter(MembershipReport.report_type == report_type)
    if target_id:
        query = query.filter(MembershipReport.target_id == target_id)
    if status:
        query = query.filter(MembershipReport.status == status)
    if from_date:
        query = query.filter(MembershipReport.created_at >= from_date)
    if to_date:
        query = query.filter(MembershipReport.created_at <= to_date)
    
    return query.order_by(MembershipReport.created_at.desc()).offset(offset).limit(limit).all()

@router.get("/{report_id}/groups", response_model=List[GroupSnapshotResponse])
async def get_report_groups(
    report_id: int,
    group_name: Optional[str] = Query(None),
    db: Session = Depends(get_db)
) -> List[GroupSnapshotResponse]:
    """
    Get group snapshots for a specific report
    """
    report = db.query(MembershipReport).filter_by(id=report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    if group_name:
        return [snapshot for snapshot in report.group_snapshots if snapshot.group_name == group_name]
    return report.group_snapshots

@router.get("/{report_id}/users", response_model=List[UserSnapshotResponse])
async def get_report_users(
    report_id: int,
    username: Optional[str] = Query(None),
    db: Session = Depends(get_db)
) -> List[UserSnapshotResponse]:
    """
    Get user snapshots for a specific report
    """
    report = db.query(MembershipReport).filter_by(id=report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    if username:
        return [snapshot for snapshot in report.user_snapshots if snapshot.username == username]
    return report.user_snapshots

@router.get("/compare/{report_id1}/{report_id2}")
def compare_reports(
    report_id1: int,
    report_id2: int,
    db: Session = Depends(get_db)
):
    """Compare two reports"""
    service = ReportService(db)
    return service.compare_reports(report_id1, report_id2) 