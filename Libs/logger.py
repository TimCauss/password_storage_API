import logging

class Logger:
    """
        A simple logger class for logging messages to a file.
        
        Attributes:
        logger (Logger): An instance of the logging.Logger class.
    """
    def __init__(self, name:str, file="app.log") -> None:
        """
        The constructor for the Logger class.
        
        Parameters:
            name (str): The name of the logger.
            file (str): The name of the file where logs will be written.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(file)
        handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        self.logger.addHandler(handler)
        
    def log(self, message:str):
        """
        Logs a message to the file specified in the constructor.

        Parameters:
            message (str): The message to be logged.
        """
        self.logger.info(message)
        

# Utilisation:
# logger = Logger('my_logger')
# logger.log('This is a log message')