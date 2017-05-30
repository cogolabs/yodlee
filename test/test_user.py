from test_base import Base
import test_data

from yodlee import User, Cobrand, error


class TestUser(Base):

    def setUp(self):
        self.add_response(
            'cobrand/login',
            json=test_data.cobrand_login,
            method='post'
        )

        self.cobrand = Cobrand(**self.credentials)

        self.add_response(
            'user/login',
            json=test_data.user_login,
            method='post'
        )

        self.user = User.login(
            cobrand=self.cobrand,
            email='email',
            password=self.credentials['user_password']
        )

    def test_logout(self):
        self.add_response('user/logout', method='post')
        self.user.logout()

    def test_register(self):
        self.add_response(
            'user/register',
            json=test_data.user_login,
            method='post'
        )

        User.register(
            cobrand=self.cobrand,
            email='email',
            password=self.credentials['user_password'],
            first_name='John',
            last_name='Doe',
            zipcode='00000'
        )

    def test_unregister(self):
        self.add_response('user/unregister', method='delete')
        self.user.unregister()

    def test_update(self):
        self.add_response('user', method='put')
        self.user.update(email='e@a', first_name='Jane', last_name='Doe')

    def test_get_accounts(self):
        self.add_response('accounts', json=test_data.accounts)
        r = self.user.get_accounts()
        self.assertEqual(test_data.accounts['account'], r)

    def test_delete_account(self):
        self.add_response('accounts/28879124', method='delete')
        self.user.delete_account(account_id=28879124)

    def test_get_fastlink_html(self):
        self.add_response('user/accessTokens', json=test_data.access_tokens)
        self.user.get_fastlink_html(node_url=self.credentials['node_url'])

    def test_get_transactions(self):
        self.add_response('transactions', json=test_data.transactions)
        r = self.user.get_transactions()
        self.assertEqual(test_data.transactions['transaction'], r)

    def test_edit_transaction(self):
        self.add_response('transactions/1', method='put')
        self.user.edit_transaction(
            transaction_id=1,
            category_id=1,
            container='bank'
        )

    def test_set_rule(self):
        self.add_response('transactions/categories/rules', method='post')
        self.user.set_rule(category_id=1, clause='CHECK')

    def test_set_rule_and_replace(self):
        rules_path = 'transactions/categories/rules'
        self.add_response(rules_path, json=test_data.rules)
        self.add_response(rules_path, method='post', status=400)
        self.add_response(rules_path, method='delete')

        with self.assertRaises(error.MaxRetries):
            self.user.set_rule(category_id=1, clause='BILL PAYMENT EVERSOURCE')

    def test_get_provider_accounts(self):
        self.add_response(
            'providerAccounts',
            json=test_data.provider_accounts
        )

        r = self.user.get_provider_accounts()
        self.assertEqual(test_data.provider_accounts['providerAccount'], r)

    def test_refresh_provider_accounts_none_found(self):
        self.add_response('providerAccounts')
        self.user.refresh_provider_accounts()

    def test_refresh_provider_accounts_found(self):
        self.add_response('providerAccounts', json=test_data.provider_accounts)
        self.add_response('providerAccounts', method='put')
        self.user.refresh_provider_accounts()
