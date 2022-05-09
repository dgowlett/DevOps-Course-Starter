import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
        self.API_KEY = os.environ.get('TRELLO_API_KEY')
        if not self.API_KEY:
            raise ValueError("No TRELLO_API_KEY set for Flask application. Did you follow the setup instructions?")
        self.API_TOKEN = os.environ.get('TRELLO_API_TOKEN')
        if not self.API_TOKEN:
            raise ValueError("No TRELLO_API_TOKEN set for Flask application. Did you follow the setup instructions?")
        self.BOARD_ID = os.environ.get('TRELLO_BOARDID')
        if not self.BOARD_ID:
            raise ValueError("No BOARD_ID set for Flask application. Did you follow the setup instructions?")
