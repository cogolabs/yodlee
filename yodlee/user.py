try:
    import simplejson as json
except ImportError:
    import json

import urllib


from .client import Client
from .config import FASTLINK_HTML
from .error import Error


class User(Client):

    def __init__(self, cobrand_token, user_token, rest_url):

        super(User, self).__init__(rest_url)

        self.headers.update({
            'Authorization': '{{cobSession={}}},{{userSession={}}}'.format(
                cobrand_token, user_token
            )
        })

        self.user_token = user_token

        self.set_session()

    @classmethod
    def authenticate(cls, cobrand, url, auth):
        r = cobrand.post('user/{}'.format(url), json=auth)
        user_token = r['user']['session']['userSession']
        return cls(cobrand.token, user_token, cobrand.rest_url)

    @classmethod
    def login(cls, cobrand, email, password):
        auth = {
            'user': {
                'loginName': email,
                'password': password,
                'locale': 'en_US'
            }
        }

        return cls.authenticate(cobrand, 'login', auth)

    @classmethod
    def register(
        cls,
        cobrand,
        email,
        password,
        first_name,
        last_name,
        zipcode
    ):
        auth = {
            'user': {
                'loginName': email,
                'email': email,
                'password': password
            },
            'name': {
                'first': first_name,
                'last': last_name
            },
            'address': {'zip': zipcode},
            'preferences': {'locale': 'en_US'}
        }

        return cls.authenticate(cobrand, 'register', auth)

    def logout(self):
        return self.post('user/logout')

    def update(self, first_name, last_name, **params):
        user = {
            'name': {
                'first': first_name,
                'last': last_name
            }
        }
        return self.put('user', user)

    def unregister(self):
        return self.delete('user/unregister')

    def get_accounts(self, provider_account_id=None, status=None, **params):
        params['providerAccountId'] = provider_account_id
        params['status'] = status
        return self.get('accounts', params=params).get('account', [])

    def delete_account(self, account_id):
        return self.delete('accounts/{}'.format(account_id))

    def get_provider_accounts(self):
        return self.get('providerAccounts').get('providerAccount', [])

    def refresh_provider_accounts(self):
        provider_accounts = self.get_provider_accounts()
        if provider_accounts:
            ids = ','.join(str(a['id']) for a in provider_accounts)
            self.put('providerAccounts', params={'providerAccountIds': ids})

    def get_transactions(self, account_id=None, from_date=None, **params):
        params['accountId'] = account_id
        params['fromDate'] = from_date
        return self.get('transactions', params=params).get('transaction', [])

    def get_fastlink_html(self, node_url, **extra_params):
        app_id = '10003600'

        r = self.get('user/accessTokens', params={'appIds': app_id})

        return FASTLINK_HTML.format(
            url=node_url,
            app=app_id,
            token=r['user']['accessTokens'][0]['value'],
            rsession=self.user_token,
            redirect='true',
            extra_params=urllib.urlencode(extra_params)
        )

    def get_rules(self):
        return self.get('transactions/categories/rules')

    def delete_rule(self, rule_id):
        return self.delete('transactions/categories/rules/{}'.format(rule_id))

    def set_rule(self, category_id, clause):
        rule = {
            'rule': {
                'categoryId': category_id,
                'source': 'SYSTEM',
                'ruleClause': [{
                    'field': 'description',
                    'operation': 'stringContains',
                    'value': clause
                }]
            }
        }

        try:
            self.post(
                'transactions/categories/rules',
                params={'ruleParam': json.dumps(rule)}
            )
        except Error:
            rules = self.get_rules()
            rule_id = None
            for _rule in rules:
                if _rule['ruleClauses'][0]['fieldValue'] == clause:
                    rule_id = _rule['userDefinedRuleId']
                    break

            if rule_id:
                self.delete_rule(rule_id)

            self.post(
                'transactions/categories/rules',
                params={'ruleParam': json.dumps(rule)}
            )

        return self.post('transactions/categories/rules?action=run')
