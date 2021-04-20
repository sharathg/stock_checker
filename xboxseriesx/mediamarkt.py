from xboxseriesx.saturn import Saturn


class MediaMarkt(Saturn):

    def __init__(self, link, pre_status, spider):
        Saturn.__init__(self, link, pre_status, spider)
        self.store = "mediamarkt"
