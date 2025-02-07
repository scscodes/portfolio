
def log_group_version_change(old_state: Dict[str, Any], new_state: Dict[str, Any], changes: Dict[str, Any]):
    """Log changes between group versions in a structured way"""
    print(f"\nGroup Version Change")
    print(f"Group: {old_state['name']}")
    print(f"Timestamp: {datetime.utcnow().isoformat()}")
    
    if changes['added'] or changes['removed']:
        print("Member Changes:")
        if changes['added']:
            print(f"  Added: {changes['added']}")
        if changes['removed']:
            print(f"  Removed: {changes['removed']}")
    
    # Log cascaded versions
    if changes['cascaded_versions']:
        print("Cascaded Versions:")
        for entity in changes['cascaded_versions']:
            print(f"  {entity['type'].title()}: {entity['id']}")
    
    # Log other field changes
    changed_fields = []
    for field in ['name', 'description', 'properties']:
        if old_state[field] != new_state[field]:
            changed_fields.append(field)
    
    if changed_fields:
        print(f"Updated Fields: {changed_fields}")
    print("-" * 50) 