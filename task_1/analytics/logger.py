import json
from datetime import datetime

def log_query(user_id, query, response, topic="general", rating=None):
    log_entry = {
        "timestamp": str(datetime.now()),
        "user_id": user_id,
        "query": query,
        "response": response,
        "topic": topic,
        "rating": rating
    }
    with open("data/user_logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
