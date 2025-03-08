class ChatBot:
    def __init__(self, gpt_model, mongo_db):
        self.gpt_model = gpt_model
        self.mongo_db = mongo_db

    def process_input(self, user_input, language='en'):
        # Process the user input through the GPT model
        response = self.gpt_model.generate_response(user_input, language)
        return response

    def handle_user_interaction(self, user_input, language='en'):
        # Handle the interaction with the user
        response = self.process_input(user_input, language)
        return response

    def multilingual_support(self, user_input, target_language):
        # Translate user input to the target language if necessary
        translated_input = self.translate_input(user_input, target_language)
        response = self.process_input(translated_input, target_language)
        return response

    def translate_input(self, user_input, target_language):
        # Implement translation logic here
        # This is a placeholder for actual translation functionality
        return user_input  # Return the input as-is for now

    def save_interaction_to_db(self, user_input, response):
        # Save the interaction to the MongoDB database
        interaction_data = {
            'user_input': user_input,
            'response': response
        }
        self.mongo_db.save_interaction(interaction_data)