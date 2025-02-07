"""
Mock data for development and testing, structured to mimic Active Directory relationships
"""
from datetime import datetime, timedelta
from typing import List, Dict, Any

# Test scenarios:
# 1. Nested group hierarchies
# 2. Multiple group memberships
# 3. Time-based memberships (some expired)
# 4. Special access patterns
# 5. Edge cases (empty groups, disabled users)

GROUPS = [
    # Root level
    {
        "name": "Organization",
        "description": "Root organizational group",
        "direct_members": [],
        "properties": {
            "scope": "global",
            "type": "organizational",
            "auto_subscribe": False
        }
    },
    
    # Department level
    {
        "name": "IT",
        "description": "Information Technology",
        "direct_members": ["IT_Security", "IT_Development", "IT_Operations"],
        "properties": {
            "scope": "department",
            "cost_center": "CC001",
            "manager": "cto@company.com"
        }
    },
    
    # IT Sub-departments
    {
        "name": "IT_Security",
        "description": "Security team",
        "direct_members": ["Security_Admins", "Security_Analysts"],
        "properties": {
            "scope": "team",
            "requires_clearance": True,
            "on_call_rotation": True
        }
    },
    {
        "name": "IT_Development",
        "description": "Development teams",
        "direct_members": ["Senior_Developers", "Junior_Developers", "QA_Team"],
        "properties": {
            "scope": "team",
            "github_access": True
        }
    },
    {
        "name": "IT_Operations",
        "description": "Operations team",
        "direct_members": ["SRE_Team", "Support_Team"],
        "properties": {
            "scope": "team",
            "aws_access": True
        }
    },
    
    # Special purpose groups
    {
        "name": "Emergency_Access",
        "description": "Break-glass emergency access",
        "direct_members": [],
        "properties": {
            "scope": "special",
            "requires_approval": True,
            "auto_expire": True,
            "max_duration": "24h"
        }
    },
    {
        "name": "Contractors",
        "description": "External contractors",
        "direct_members": [],
        "properties": {
            "scope": "external",
            "requires_nda": True,
            "auto_expire": True
        }
    }
]

USERS = [
    # IT Security
    {
        "username": "security_lead",
        "email": "security.lead@company.com",
        "full_name": "Security Lead",
        "principal_name": "security_lead@company.com",
        "direct_memberships": ["IT_Security", "Security_Admins", "Emergency_Access"],
        "properties": {
            "employee_type": "FTE",
            "clearance_level": "high",
            "start_date": "2020-01-01",
            "manager": "cto@company.com"
        }
    },
    {
        "username": "security_analyst",
        "email": "analyst@company.com",
        "full_name": "Security Analyst",
        "principal_name": "analyst@company.com",
        "direct_memberships": ["Security_Analysts"],
        "properties": {
            "employee_type": "FTE",
            "clearance_level": "medium",
            "start_date": "2022-03-15"
        }
    },
    
    # Development
    {
        "username": "lead_dev",
        "email": "lead.dev@company.com",
        "full_name": "Lead Developer",
        "principal_name": "lead_dev@company.com",
        "direct_memberships": ["IT_Development", "Senior_Developers"],
        "properties": {
            "employee_type": "FTE",
            "github_admin": True,
            "start_date": "2019-06-01"
        }
    },
    {
        "username": "junior_dev",
        "email": "junior.dev@company.com",
        "full_name": "Junior Developer",
        "principal_name": "junior_dev@company.com",
        "direct_memberships": ["Junior_Developers"],
        "properties": {
            "employee_type": "FTE",
            "github_access": True,
            "start_date": "2023-09-01",
            "probation_end": "2024-03-01"
        }
    },
    
    # Operations
    {
        "username": "sre_lead",
        "email": "sre.lead@company.com",
        "full_name": "SRE Lead",
        "principal_name": "sre_lead@company.com",
        "direct_memberships": ["IT_Operations", "SRE_Team", "Emergency_Access"],
        "properties": {
            "employee_type": "FTE",
            "aws_admin": True,
            "start_date": "2021-01-15",
            "on_call": True
        }
    },
    
    # Contractors
    {
        "username": "contractor1",
        "email": "contractor1@external.com",
        "full_name": "Contractor One",
        "principal_name": "contractor1@company.com",
        "direct_memberships": ["Contractors", "Junior_Developers"],
        "properties": {
            "employee_type": "Contractor",
            "contract_end": "2024-12-31",
            "github_access": True,
            "requires_supervision": True
        }
    },
    
    # Special cases
    {
        "username": "disabled_user",
        "email": "disabled@company.com",
        "full_name": "Disabled User",
        "principal_name": "disabled@company.com",
        "direct_memberships": [],
        "properties": {
            "employee_type": "FTE",
            "enabled": False,
            "disable_reason": "Extended Leave",
            "disable_date": "2024-01-01"
        }
    },
    {
        "username": "temp_admin",
        "email": "temp.admin@company.com",
        "full_name": "Temporary Admin",
        "principal_name": "temp_admin@company.com",
        "direct_memberships": ["Emergency_Access"],
        "properties": {
            "employee_type": "FTE",
            "temp_access_start": "2024-03-15",
            "temp_access_end": "2024-03-16",
            "approval_ticket": "INC123456"
        }
    }
]

# Test scenarios for membership relationships
MEMBERSHIP_SCENARIOS = {
    "nested_groups": {
        "path": ["Organization", "IT", "IT_Development", "Senior_Developers"],
        "expected_users": ["lead_dev"]
    },
    "multiple_memberships": {
        "user": "security_lead",
        "expected_groups": ["IT_Security", "Security_Admins", "Emergency_Access"]
    },
    "contractor_access": {
        "user": "contractor1",
        "restricted_groups": ["Security_Admins", "Emergency_Access"]
    },
    "temporary_access": {
        "user": "temp_admin",
        "duration": timedelta(days=1),
        "requires_approval": True
    }
}

# Additional test data
AUDIT_SCENARIOS = {
    "group_changes": [
        {
            "group": "IT_Development",
            "change_type": "add_member",
            "user": "contractor1",
            "timestamp": "2024-01-15T10:00:00Z"
        },
        {
            "group": "Emergency_Access",
            "change_type": "add_member",
            "user": "temp_admin",
            "timestamp": "2024-03-15T09:00:00Z"
        }
    ],
    "access_patterns": [
        {
            "pattern": "emergency_access",
            "frequency": "rare",
            "duration": "24h",
            "approval_required": True
        },
        {
            "pattern": "contractor_access",
            "frequency": "workdays",
            "duration": "contract_period",
            "approval_required": False
        }
    ]
}

# Add mock reports data
REPORTS = [
    {
        "report_type": "full",
        "created_at": datetime.utcnow() - timedelta(days=1),
        "completed_at": datetime.utcnow() - timedelta(days=1, minutes=30),
        "status": "completed",
        "properties": {
            "include_disabled": True,
            "include_historical": True
        },
        "snapshots": {
            "groups": [
                {
                    "group_name": "IT_Department",
                    "description": "IT Department Group",
                    "direct_members": ["admin", "dev1", "dev2"],
                    "nested_members": ["dev3", "dev4"],
                    "member_of": [],
                    "all_parent_groups": [],
                    "properties": {
                        "type": "department",
                        "cost_center": "IT001"
                    },
                    "snapshot_time": datetime.utcnow() - timedelta(days=1)
                }
            ],
            "users": [
                {
                    "username": "admin",
                    "email": "admin@company.com",
                    "full_name": "System Admin",
                    "principal_name": "admin@company.com",
                    "direct_memberships": ["IT_Department", "Admins"],
                    "effective_memberships": ["IT_Department", "Admins", "All_Users"],
                    "properties": {
                        "role": "admin",
                        "access_level": "high"
                    },
                    "snapshot_time": datetime.utcnow() - timedelta(days=1)
                }
            ]
        }
    },
    {
        "report_type": "group_specific",
        "target_id": "IT_Department",
        "created_at": datetime.utcnow() - timedelta(hours=12),
        "completed_at": datetime.utcnow() - timedelta(hours=11, minutes=45),
        "status": "completed",
        "properties": {
            "depth": "all",
            "include_nested": True,
            "include_indirect": True
        },
        "snapshots": {
            "groups": [
                {
                    "group_name": "IT_Department",
                    "description": "IT Department Group",
                    "direct_members": ["admin", "dev1", "dev2"],
                    "nested_members": ["dev3", "dev4"],
                    "member_of": [],
                    "all_parent_groups": [],
                    "properties": {
                        "type": "department",
                        "cost_center": "IT001"
                    },
                    "snapshot_time": datetime.utcnow() - timedelta(hours=12)
                }
            ]
        }
    }
]
