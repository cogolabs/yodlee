import responses
import unittest


class Base(unittest.TestCase):

    credentials = {
        'cobrand': 'cobrand',
        'cobrand_id': 1,
        'password': 'password',
        'user_password': 'user_password',
        'rest_wrapper': 'https://yodlee.com/services/srest/restserver/v1.0/',
        'rest_url': 'https://yodlee.com/ysl/restserver/',
        'node_url': 'https://yodlee.com/authenticate/restserver/'
    }

    def add_response(self, path, json={}, status=200, method='get'):
        responses.add(
            getattr(responses, method.upper()),
            self.credentials['rest_url'] + path,
            json=json,
            status=status
        )

    @responses.activate
    def run(self, result=None):
        super(Base, self).run(result)
