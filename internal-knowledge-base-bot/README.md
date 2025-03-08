# Internal Knowledge Base Bot

This project is an Internal Knowledge Base Bot that utilizes a multilingual chat interface powered by GPT, with a Streamlit GUI for user interaction. The bot connects to a MongoDB database for managing and retrieving knowledge base entries, and it leverages CUDA for efficient multi-processing.

## Project Structure

```
internal-knowledge-base-bot
├── src
│   ├── app.py                # Main entry point of the application
│   ├── bot
│   │   ├── __init__.py       # Bot module initialization
│   │   ├── chat.py           # ChatBot class for user interactions
│   │   └── knowledge_base.py  # KnowledgeBase class for MongoDB management
│   ├── gui
│   │   ├── __init__.py       # GUI module initialization
│   │   └── streamlit_app.py  # Streamlit application code
│   ├── utils
│   │   ├── __init__.py       # Utility functions initialization
│   │   └── mongo_utils.py     # MongoDB utility functions
│   └── config.py             # Configuration settings
├── requirements.txt           # Project dependencies
├── setup.py                   # Packaging information
├── Dockerfile                 # Docker image instructions
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/internal-knowledge-base-bot.git
   cd internal-knowledge-base-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the MongoDB connection in `src/config.py`.

## Usage

To run the application, execute the following command:
```
python src/app.py
```

This will start the Streamlit GUI, allowing users to interact with the bot.

## Features

- Multilingual support using GPT for natural language processing.
- Integration with MongoDB for knowledge base management.
- Streamlit-based user interface for easy interaction.
- CUDA support for enhanced performance in processing.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.