"""SQL queries for project operations"""

INSERT_PROJECT = """
INSERT INTO projects (
    name, description, properties,
    created_at, modified_at, evaluated_at
) VALUES (?, ?, ?, ?, ?, ?)
"""

INSERT_PROJECT_VERSION = """
INSERT INTO project_versions (
    project_id, name, description,
    properties, created_at, modified_at,
    evaluated_at, archived_at
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""" 