from selenium.webdriver import Firefox, FirefoxOptions
from spider.logger import Logger


class Base(Logger):

    def __init__(self):
        Logger.__init__(self)
        self.logger.info("Starting Firefox..")
        options = FirefoxOptions()
        options.add_argument("--headless")
        try:
            self.browser = Firefox(options=options)
            self.logger.info("Firefox Ready..")
        except Exception as e:
            self.logger.error("Firefox could not be started.")
            self.logger.error(e)
            quit(-1)

    def quit(self):
        if self.browser:
            self.logger.info("Quitting Firefox..")
            self.browser.quit()
