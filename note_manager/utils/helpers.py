from datetime import datetime
import uuid

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError:
        return None

def validate_status(status):
    valid_statuses = ["новая", "в процессе", "выполнена"]
    return status if status in valid_statuses else None

def generate_unique_id():
    return str(uuid.uuid4())
