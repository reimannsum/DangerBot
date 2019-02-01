import requests


class Http(object):
    """A wrapper around the requests library so we can effectively test http related functions"""
    def __init__(self):
        self.session = requests.session()

    def get(self, url, query_params):
        return self.session.get(url, params=query_params).text

    def post(self, url, data):
        return self.session.post(url, data=data).text
