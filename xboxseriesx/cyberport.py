from os import environ as env


class Cyberport:

    def __init__(self, link, pre_status, spider):
        self.browser = spider.browser
        self.logger = spider.logger
        self.store_link = link
        self.pre_status = pre_status
        self.store = "cyberport"

    def main(self):
        self.browser.get(self.store_link)
        status = "true"
        cart = self.browser.find_elements_by_xpath("//article[contains(@data-product-name, 'Xbox Series X')]")
        if not cart:
            status = "false"
            self.logger.info(self.store, ":", "Not available")
        if status != self.pre_status:
            self.update_status(status)

    def update_status(self, status):
        update_link = env['BASE_URL'] + "?" + env['UPDATE_PATH']
        self.browser.get(update_link.format(self.store, status))
