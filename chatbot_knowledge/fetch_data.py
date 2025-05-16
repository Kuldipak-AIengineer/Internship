# Simulate fetching new information (from API or other sources)
import time
from knowledge_base import update_knowledge_base

def fetch_new_info():
    new_data = [
        "The Eiffel Tower is in Paris.",
        "Python is a programming language.",
    ]
    update_knowledge_base(new_data)

# Simulate periodic fetching (every hour)
if __name__ == "__main__":
    while True:
        fetch_new_info()
        time.sleep(3600)  # Sleep for 1 hour
