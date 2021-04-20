import json

from os import environ as env
from spider import Spider
from xboxseriesx.saturn import Saturn
from xboxseriesx.mediamarkt import MediaMarkt
from xboxseriesx.gamestop import GameStop
from xboxseriesx.cyberport import Cyberport


class XBoxSeriesX:

    def __init__(self):
        self.spider = Spider()
        try:
            self.run()
        except Exception as e:
            self.spider.logger.error(e)
        finally:
            self.spider.quit()

    def run(self):
        self.spider.browser.get(env['BASE_URL'] + "?json=1")
        s = self.spider.browser.find_element_by_xpath("//body").text
        data = json.loads(s)
        for item in data:
            if item['store'] == "saturn":
                Saturn(item['link'], item['availability'], self.spider).main()
            elif item['store'] == "mediamarkt":
                MediaMarkt(item['link'], item['availability'], self.spider).main()
            elif item['store'] == "gamestop":
                GameStop(item['link'], item['availability'], self.spider).main()
            elif item['store'] == "cyberport":
                Cyberport(item['link'], item['availability'], self.spider).main()
