import re

def mask_sensitive_data(logs):
    # Mask long numbers (account numbers etc.)
    logs = re.sub(r'\b\d{6,}\b', 'XXXXXX', logs)

    # Mask emails
    logs = re.sub(r'\S+@\S+', 'masked@email.com', logs)

    return logs