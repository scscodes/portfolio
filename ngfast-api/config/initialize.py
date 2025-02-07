"""
Database initialization and seeding functionality
"""
from sqlalchemy.orm import Session
import logging
from .database import engine, Base, SessionLocal
from datetime import datetime
import sys
import os

# Add the parent directory to system path to import mock_data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data import mock_data
from features.groups.models import GroupDB, GroupHistory
from features.users.models import UserDB, UserHistory
from features.memberships.models import (
    Membership, MembershipHistory,
    UserMembership, UserMembershipHistory,
    GroupMembership, GroupMembershipHistory
)
from features.reports.models import MembershipReport, GroupSnapshot, UserSnapshot

logger = logging.getLogger(__name__)

def initialize_database():
    """
    Initialize the database, create all tables, and seed with mock data
    """
    try:
        # Drop existing tables
        logger.info("Dropping existing tables...")
        Base.metadata.drop_all(bind=engine)
        
        # Create all tables
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        
        # Seed mock data using a session
        logger.info("Seeding mock data...")
        db = SessionLocal()
        try:
            seed_mock_data(db)
            db.commit()
            logger.info("Database initialization completed successfully")
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise

def seed_mock_data(db: Session):
    """
    Seed the database with mock data, maintaining AD-like relationships
    """
    try:
        now = datetime.utcnow()
        
        # First, create all groups
        logger.info("Seeding groups...")
        group_mapping = {}  # Store group_name -> GroupDB mapping
        for group_data in mock_data.GROUPS:
            group = GroupDB(
                group_name=group_data['name'],
                description=group_data.get('description'),
                properties=group_data.get('properties', {})
            )
            db.add(group)
            db.flush()
            
            # Create initial history record
            history = GroupHistory(
                group_id=group.group_id,
                group_name=group.group_name,
                start_date=now,
                end_date=None
            )
            db.add(history)
            group_mapping[group.group_name] = group

        # Create users
        logger.info("Seeding users...")
        user_mapping = {}  # Store username -> UserDB mapping
        for user_data in mock_data.USERS:
            user = UserDB(
                user_name=user_data['username'],
                email=user_data['email'],
                full_name=user_data['full_name'],
                principal_name=user_data['principal_name'],
                properties=user_data.get('properties', {})
            )
            db.add(user)
            db.flush()
            
            # Create initial history record
            history = UserHistory(
                user_id=user.user_id,
                user_name=user.user_name,
                start_date=now,
                end_date=None
            )
            db.add(history)
            user_mapping[user.user_name] = user

        # Create memberships
        logger.info("Seeding memberships...")
        membership_mapping = {}  # Store membership_name -> Membership mapping
        
        # Create a default membership for each group
        for group_name, group in group_mapping.items():
            membership = Membership(
                membership_name=f"{group_name}_membership"
            )
            db.add(membership)
            db.flush()
            
            # Create membership history
            history = MembershipHistory(
                membership_id=membership.membership_id,
                membership_name=membership.membership_name,
                start_date=now,
                end_date=None
            )
            db.add(history)
            membership_mapping[group_name] = membership

            # Create group membership with explicit flush
            group_membership = GroupMembership(
                group_id=group.group_id,
                membership_id=membership.membership_id
            )
            db.add(group_membership)
            db.flush()  # Ensure we get the ID
            
            # Now create group membership history with the ID
            group_membership_history = GroupMembershipHistory(
                group_membership_id=group_membership.group_membership_id,
                group_id=group.group_id,
                membership_id=membership.membership_id,
                start_date=now,
                end_date=None
            )
            db.add(group_membership_history)

        # Create user memberships
        logger.info("Creating user memberships...")
        for user_data in mock_data.USERS:
            user = user_mapping[user_data['username']]
            for group_name in user_data['direct_memberships']:
                if group_name in membership_mapping:
                    membership = membership_mapping[group_name]
                    
                    # Create user membership with explicit flush
                    user_membership = UserMembership(
                        user_id=user.user_id,
                        membership_id=membership.membership_id
                    )
                    db.add(user_membership)
                    db.flush()  # Get the ID
                    
                    # Create user membership history with the ID
                    user_membership_history = UserMembershipHistory(
                        user_membership_id=user_membership.user_membership_id,
                        user_id=user.user_id,
                        membership_id=membership.membership_id,
                        start_date=now,
                        end_date=None
                    )
                    db.add(user_membership_history)

        # Seed reports
        logger.info("Seeding reports...")
        for report_data in mock_data.REPORTS:
            report = MembershipReport(
                report_type=report_data["report_type"],
                target_id=report_data.get("target_id"),
                created_at=report_data["created_at"],
                completed_at=report_data["completed_at"],
                status=report_data["status"],
                properties=report_data["properties"]
            )
            db.add(report)
            db.flush()

            # Add group snapshots
            for group_snap in report_data["snapshots"].get("groups", []):
                snapshot = GroupSnapshot(
                    report_id=report.id,
                    group_name=group_snap["group_name"],
                    description=group_snap["description"],
                    direct_members=group_snap["direct_members"],
                    nested_members=group_snap["nested_members"],
                    member_of=group_snap["member_of"],
                    all_parent_groups=group_snap["all_parent_groups"],
                    properties=group_snap["properties"],
                    snapshot_time=group_snap["snapshot_time"],
                    original_created_at=datetime.utcnow(),
                    original_modified_at=datetime.utcnow()
                )
                db.add(snapshot)

            # Add user snapshots
            for user_snap in report_data["snapshots"].get("users", []):
                snapshot = UserSnapshot(
                    report_id=report.id,
                    username=user_snap["username"],
                    email=user_snap["email"],
                    full_name=user_snap["full_name"],
                    principal_name=user_snap["principal_name"],
                    direct_memberships=user_snap["direct_memberships"],
                    effective_memberships=user_snap["effective_memberships"],
                    properties=user_snap["properties"],
                    snapshot_time=user_snap["snapshot_time"],
                    original_created_at=datetime.utcnow(),
                    original_modified_at=datetime.utcnow()
                )
                db.add(snapshot)

        # Final commit
        db.commit()
        logger.info("Successfully seeded all data")
        
    except Exception as e:
        logger.error(f"Error seeding mock data: {str(e)}")
        db.rollback()
        raise 