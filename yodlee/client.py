import requests
import time


from . import error, config


class Client(object):

    def __init__(self, rest_url):
        self.rest_url = rest_url
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self.set_session()

    def set_session(self):
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def __call__(self, attr, path, *args, **kwargs):
        url = self.rest_url + path

        for i in range(config.RETRIES):
            try:
                r = getattr(self.session, attr)(url, *args, **kwargs)
            except requests.ConnectionError:
                self.set_session()
                time.sleep(config.RETRY_SLEEP)
            else:
                break
        else:
            raise error.MaxRetries

        try:
            ret = r.json()
        except ValueError:
            ret = {}

        if r.status_code >= 400:
            raise error.get(ret)

        return ret

    def delete(self, path, *args, **kwargs):
        return self.__call__('delete', path, *args, **kwargs)

    def get(self, path, *args, **kwargs):
        return self.__call__('get', path, *args, **kwargs)

    def post(self, path, *args, **kwargs):
        return self.__call__('post', path, *args, **kwargs)

    def put(self, path, *args, **kwargs):
        return self.__call__('put', path, *args, **kwargs)
