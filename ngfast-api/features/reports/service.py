"""Report service layer"""
from datetime import datetime
from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException

from .models import MembershipReport, GroupSnapshot, UserSnapshot
from .schemas import ReportRequest
from shared.exceptions import EntityNotFoundError
from features.memberships.models import (
    Membership,
    UserMembership,
    GroupMembership
)
from features.users.models import UserDB
from features.groups.models import GroupDB

class ReportService:
    def __init__(self, db: Session):
        self.db = db

    def generate_report(self, request: ReportRequest) -> MembershipReport:
        """Generate a new membership report"""
        try:
            report = MembershipReport(
                report_type=request.report_type,
                target_id=request.target_id,
                created_at=datetime.utcnow(),
                status="pending",
                properties=request.properties or {}
            )
            self.db.add(report)
            self.db.flush()

            if request.report_type == "full":
                self._generate_full_report(report)
            elif request.report_type == "group_specific":
                self._generate_group_report(report)
            elif request.report_type == "user_specific":
                self._generate_user_report(report)
            elif request.report_type == "membership_specific":
                self._generate_membership_report(report)

            report.status = "completed"
            report.completed_at = datetime.utcnow()
            
            self.db.commit()
            return report
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def _generate_membership_report(self, report: MembershipReport) -> None:
        """Generate membership-specific report"""
        membership_id = report.target_id
        membership = self.db.query(Membership).filter_by(membership_id=membership_id).first()
        if not membership:
            raise EntityNotFoundError("Membership", membership_id)

        snapshot = MembershipSnapshot(
            report_id=report.id,
            membership_id=membership_id,
            user_count=self._get_membership_user_count(membership_id),
            group_count=self._get_membership_group_count(membership_id),
            active_since=membership.created_at,
            properties=report.properties
        )
        self.db.add(snapshot)

    def _generate_user_report(self, report: MembershipReport) -> None:
        """Generate user-specific report"""
        user_id = report.target_id
        user = self.db.query(UserDB).filter_by(user_id=user_id).first()
        if not user:
            raise EntityNotFoundError("User", user_id)

        snapshot = UserSnapshot(
            report_id=report.id,
            user_id=user_id,
            membership_history=self._get_user_membership_history(user_id),
            current_memberships=self._get_user_current_memberships(user_id),
            properties=report.properties
        )
        self.db.add(snapshot)

    def _generate_group_report(self, report: MembershipReport) -> None:
        """Generate group-specific report"""
        group_id = report.target_id
        group = self.db.query(GroupDB).filter_by(group_id=group_id).first()
        if not group:
            raise EntityNotFoundError("Group", group_id)

        snapshot = GroupSnapshot(
            report_id=report.id,
            group_id=group_id,
            direct_members=self._get_group_direct_members(group_id),
            nested_members=self._get_group_nested_members(group_id),
            member_of=self._get_group_memberships(group_id),
            properties=report.properties
        )
        self.db.add(snapshot)

    def _generate_full_report(self, report: MembershipReport) -> None:
        """Generate a full system report"""
        # Implementation here

    def _get_membership_user_count(self, membership_id: int) -> int:
        """Get active user count for membership"""
        return self.db.query(UserMembership)\
            .filter_by(membership_id=membership_id)\
            .filter(UserMembership.end_date.is_(None))\
            .count()

    def _get_membership_group_count(self, membership_id: int) -> int:
        """Get active group count for membership"""
        return self.db.query(GroupMembership)\
            .filter_by(membership_id=membership_id)\
            .filter(GroupMembership.end_date.is_(None))\
            .count()

    def get_report(self, report_id: int) -> Optional[MembershipReport]:
        """Get a specific report"""
        return self.db.query(MembershipReport).filter_by(id=report_id).first()

    def compare_reports(self, report_id1: int, report_id2: int) -> Dict[str, Any]:
        """Compare two reports"""
        # Implementation here 