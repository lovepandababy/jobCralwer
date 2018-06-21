import requests


class BaseCrawler(object):
    base_url = None

    task = None

    def __init__(self, task):
        self.task = task
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 "
                                                   "(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"})

    def get_total_page_by_document(self, document):
        """
        根据传入放入document获取total_page
        :param document:
        :return:
        """
        raise NotImplementedError

    def get_total_page_by_html(self, html):
        """
        根据传入的html获取total_page
        :param html:
        :return:
        """
        raise NotImplementedError

    def start(self):
        """
        爬虫开始
        :return:
        """
        raise NotImplementedError

    def send_requests(self, url, form_data=None):
        """
        发送请求
        :param form_data:
        :param url:
        :return:
        """
        if form_data:
            res = self.session.post(url=url, data=form_data, timeout=20)
        else:
            res = self.session.get(url=url, timeout=20)
        if self.task.site == '51job':
            res.encoding = 'GBK'
        return res
