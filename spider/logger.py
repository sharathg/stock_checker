import logging


class Logger:
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s %(levelname)s:%(message)s',
            level=logging.INFO)
        self.logger = logging
