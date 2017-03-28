from .client import Client


class Cobrand(Client):

    def __init__(self, cobrand, password, rest_url, **kwargs):

        super(Cobrand, self).__init__(rest_url)

        auth = {
            'cobrand': {
                'cobrandLogin': cobrand,
                'cobrandPassword': password,
                'locale': 'en_US'
            }
        }

        r = self.post('cobrand/login', json=auth)
        self.token = r['session']['cobSession']
        self.headers['Authorization'] = '{{cobSession={}}}'.format(self.token)

        self.set_session()

    def edit_webhook(self,  callback_url, event='REFRESH', method='post'):
        return getattr(self, method)(
            'cobrand/config/notifications/events/{}'.format(event),
            json={'event': {'callbackUrl': callback_url}}
        )

    def get_webhooks(self):
        return self.get('cobrand/config/notifications/events')
