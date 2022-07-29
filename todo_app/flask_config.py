import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.API_KEY = os.environ.get('TRELLO_API_KEY')
        if not self.API_KEY:
            raise ValueError("No TRELLO_API_KEY set for Flask application. Did you follow the setup instructions?")
        self.API_TOKEN = os.environ.get('TRELLO_API_TOKEN')
        if not self.API_TOKEN:
            raise ValueError("No TRELLO_API_TOKEN set for Flask application. Did you follow the setup instructions?")
        self.BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
        if not self.BOARD_ID:
            raise ValueError("No TRELLO_BOARD_ID set for Flask application. Did you follow the setup instructions?")
