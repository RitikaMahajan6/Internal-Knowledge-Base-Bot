import streamlit as st
from bot.chat import ChatBot
from bot.knowledge_base import KnowledgeBase
from utils.mongo_utils import connect_to_mongo

def main():
    st.title("Internal Knowledge Base Bot")
    
    # Connect to MongoDB
    mongo_client = connect_to_mongo()
    knowledge_base = KnowledgeBase(mongo_client)
    chatbot = ChatBot(knowledge_base)

    # User input
    user_input = st.text_input("Ask a question:")
    
    if st.button("Submit"):
        if user_input:
            response = chatbot.get_response(user_input)
            st.write("Bot:", response)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()