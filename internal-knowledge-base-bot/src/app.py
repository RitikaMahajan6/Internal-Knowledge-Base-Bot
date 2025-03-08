from bot.chat import ChatBot
from gui.streamlit_app import run_streamlit_app
from utils.mongo_utils import connect_to_mongo
from config import Config

def main():
    # Connect to MongoDB
    mongo_client = connect_to_mongo(Config.MONGO_URI)
    
    # Initialize the chatbot
    chatbot = ChatBot(mongo_client)
    
    # Start the Streamlit GUI
    run_streamlit_app(chatbot)

if __name__ == "__main__":
    main()