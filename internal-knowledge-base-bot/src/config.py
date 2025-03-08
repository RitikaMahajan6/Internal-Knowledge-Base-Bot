# Configuration settings for the Internal Knowledge Base Bot

class Config:
    MONGODB_HOST = "your_mongodb_host"
    MONGODB_PORT = 27017
    MONGODB_DB = "your_database_name"
    MONGODB_USER = "your_username"
    MONGODB_PASSWORD = "your_password"
    
    GPT_MODEL = "gpt-3.5-turbo"  # Specify the GPT model to use
    CUDA_ENABLED = True  # Set to True if CUDA is available for processing
    LANGUAGES_SUPPORTED = ["en", "es", "fr", "de"]  # List of supported languages for the chatbot

    STREAMLIT_PORT = 8501  # Default port for Streamlit application
    DEBUG_MODE = True  # Set to True for debugging purposes

    @staticmethod
    def get_mongo_uri():
        return f"mongodb://{Config.MONGODB_USER}:{Config.MONGODB_PASSWORD}@{Config.MONGODB_HOST}:{Config.MONGODB_PORT}/{Config.MONGODB_DB}"