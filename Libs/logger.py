import logging

class Logger:
    def __init__(self, name, file="app.log") -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(file)
        handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        self.logger.addHandler(handler)
        
    def log(self, message):
        self.logger.info(message)