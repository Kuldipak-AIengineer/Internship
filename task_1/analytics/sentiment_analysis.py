import json

def average_rating(log_path):
    ratings = []
    with open(log_path, "r") as f:
        for line in f:
            entry = json.loads(line)
            if entry.get("rating") is not None:
                ratings.append(entry["rating"])
    return sum(ratings)/len(ratings) if ratings else 0
