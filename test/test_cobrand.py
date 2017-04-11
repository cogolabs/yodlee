from test_base import Base
import test_data

from yodlee import Cobrand


class TestCobrand(Base):

    def setUp(self):
        self.add_response(
            'cobrand/login',
            json=test_data.cobrand_login,
            method='post'
        )

        self.cobrand = Cobrand(**self.credentials)


    def test_get_webhooks(self):
        self.add_response('cobrand/config/notifications/events')
        self.cobrand.get_webhooks()

    def test_edit_webhook(self):
        self.add_response(
            'cobrand/config/notifications/events/REFRESH',
            method='post'
        )
        self.cobrand.edit_webhook(callback_url='')
