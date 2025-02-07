# Portfolio API

A FastAPI backend service that provides user, group, and project management functionality.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Setup

1. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Unix/MacOS
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

3. Run the development server:
```bash
uvicorn main:app --reload
```

## API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
  - Interactive API documentation
  - Try out endpoints directly in the browser
  - View request/response schemas
  - OAuth2 authentication support

- **ReDoc**: http://localhost:8000/redoc
  - Alternative documentation view
  - Better for reading and understanding the API structure
  - Cleaner interface for sharing with stakeholders

- **OpenAPI Schema**: http://localhost:8000/openapi.json
  - Raw OpenAPI (Swagger) specification
  - Can be imported into other API tools
  - Used for generating client libraries


```mermaid
erDiagram
    %% Core Entities
    UserDB ||--o{ UserHistory : "tracks_changes"
    UserDB ||--o{ UserMembership : "has"
    
    GroupDB ||--o{ GroupHistory : "tracks_changes"
    GroupDB ||--o{ GroupMembership : "has"
    
    Membership ||--o{ UserMembership : "has"
    Membership ||--o{ GroupMembership : "has"
    Membership ||--o{ MembershipHistory : "tracks_changes"

    %% Core Tables
    UserDB {
        int user_id PK
        string user_name UK
        string email UK
        string full_name
        string principal_name UK
        json properties
    }

    GroupDB {
        int group_id PK
        string group_name UK
        string description
        json properties
    }

    Membership {
        int membership_id PK
        string membership_name
    }

    %% History Tables
    UserHistory {
        int user_history_id PK
        int user_id FK
        string user_name
        datetime start_date
        datetime end_date
    }

    GroupHistory {
        int group_history_id PK
        int group_id FK
        string group_name
        datetime start_date
        datetime end_date
    }

    MembershipHistory {
        int membership_history_id PK
        int membership_id FK
        string membership_name
        datetime start_date
        datetime end_date
    }

    %% Association Tables
    UserMembership {
        int user_membership_id PK
        int user_id FK
        int membership_id FK
    }

    GroupMembership {
        int group_membership_id PK
        int group_id FK
        int membership_id FK
    }

    %% Association History Tables
    UserMembershipHistory {
        int user_membership_history_id PK
        int user_membership_id FK
        int user_id FK
        int membership_id FK
        datetime start_date
        datetime end_date
    }

    GroupMembershipHistory {
        int group_membership_history_id PK
        int group_membership_id FK
        int group_id FK
        int membership_id FK
        datetime start_date
        datetime end_date
    }

    %% Additional Relationships
    UserMembership ||--o{ UserMembershipHistory : "tracks_changes"
    GroupMembership ||--o{ GroupMembershipHistory : "tracks_changes"
```



