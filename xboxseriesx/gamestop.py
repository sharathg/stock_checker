from os import environ as env


class GameStop:

    def __init__(self, link, pre_status, spider):
        self.browser = spider.browser
        self.logger = spider.logger
        self.store_link = link
        self.pre_status = pre_status
        self.store = "gamestop"

    def main(self):
        self.browser.get(self.store_link)
        cart = self.browser.find_element_by_id("btnAddToCart")
        status = "true"
        if not cart.is_displayed():
            status = "false"
            unavailable = self.browser.find_element_by_class_name("buyDisabled")
            self.logger.info(self.store + " : " + unavailable.text)
        if status != self.pre_status:
            self.update_status(status)

    def update_status(self, status):
        update_link = env['BASE_URL'] + "?" + env['UPDATE_PATH']
        self.browser.get(update_link.format(self.store, status))
