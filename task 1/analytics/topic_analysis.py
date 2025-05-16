from collections import Counter
import json

def get_common_topics(log_path):
    topics = []
    with open(log_path, "r") as f:
        for line in f:
            entry = json.loads(line)
            topics.append(entry.get("topic", "general"))
    return Counter(topics).most_common(5)
