from test_base import Base

from yodlee import error


class TestError(Base):

    def test_error(self):
        with self.assertRaises(error.MissingCredentials):
            raise error.get({'errorCode': 'Y001', 'errorMessage': ''})

        with self.assertRaises(error.Error):
            raise error.get({})
