import uuid


def is_valid_uuid4(value: str) -> bool:
    try:
        id = uuid.UUID(value, version=4)
    except:
        return False
    
    return str(id) == value.lower()