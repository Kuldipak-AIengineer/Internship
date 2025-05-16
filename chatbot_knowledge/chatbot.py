# Chatbot interface to respond based on the knowledge base
from knowledge_base import search_knowledge_base

def chatbot_response(user_query):
    # Search the knowledge base for relevant information
    results = search_knowledge_base(user_query)
    
    # Extract and return the best match
    if results:
        return f"I found some information: {results[0][0]}"
    else:
        return "Sorry, I don't know the answer to that."

# Example: Testing the chatbot
if __name__ == "__main__":
    query = "Where is the Eiffel Tower?"
    print(chatbot_response(query))
