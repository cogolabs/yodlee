class Error(Exception):
    pass


class MissingCredentials(Error):
    pass


class InvalidCredentials(Error):
    pass


class AccountLocked(Error):
    pass


class InactiveUser(Error):
    pass


class SuspendedUser(Error):
    pass


class UnregisteredUser(Error):
    pass


class MissingAuthorizationHeader(Error):
    pass


class InvalidAuthorizationHeader(Error):
    pass


class MissingSessionTokens(Error):
    pass


class InvalidSession(Error):
    pass


class InvalidCobrand(Error):
    pass


class DoNotPassUserSession(Error):
    pass


class AuthenticationError(Error):
    pass


class InvalidValue(Error):
    pass


class InvalidLength(Error):
    pass


class NotAllowed(Error):
    pass


class Required(Error):
    pass


class InvalidRange(Error):
    pass


class MultipleValuesNotSupported(Error):
    pass


class InvalidInput(Error):
    pass


class NotFound(Error):
    pass


class InvalidPassword(Error):
    pass


class InvalidDate(Error):
    pass


class Duplicate(Error):
    pass


class AlreadyExists(Error):
    pass


class MissingRequired(Error):
    pass


class NoExchangeRate(Error):
    pass


class CannotFilter(Error):
    pass


class InvalidRequest(Error):
    pass


class CannotUpdate(Error):
    pass


class NotSupportedFor(Error):
    pass


class NotSupported(Error):
    pass


class ServiceNotSupported(Error):
    pass


class Oops(Error):
    pass


class ConnectionUnavailable(Error):
    pass


class InternalException(Error):
    pass


class MaxRetries(Error):
    pass


ERRORS = {
    'Y001': MissingCredentials,
    'Y002': InvalidCredentials,
    'Y003': AccountLocked,
    'Y004': InactiveUser,
    'Y005': SuspendedUser,
    'Y006': UnregisteredUser,
    'Y007': MissingAuthorizationHeader,
    'Y008': InvalidAuthorizationHeader,
    'Y009': MissingSessionTokens,
    'Y010': InvalidSession,
    'Y011': InvalidCobrand,
    'Y012': DoNotPassUserSession,
    'Y013': AuthenticationError,
    'Y800': InvalidValue,
    'Y801': InvalidLength,
    'Y802': NotAllowed,
    'Y803': Required,
    'Y804': InvalidRange,
    'Y805': MultipleValuesNotSupported,
    'Y806': InvalidInput,
    'Y807': NotFound,
    'Y808': InvalidPassword,
    'Y809': InvalidDate,
    'Y810': Duplicate,
    'Y811': AlreadyExists,
    'Y812': MissingRequired,
    'Y814': NoExchangeRate,
    'Y815': CannotFilter,
    'Y816': InvalidRequest,
    'Y819': CannotUpdate,
    'Y820': NotSupportedFor,
    'Y821': NotSupported,
    'Y901': ServiceNotSupported,
    'Y902': Oops,
    'Y903': ConnectionUnavailable,
    'Y904': InternalException,
    'Y400': Error
}


def get(r):
    error_code = r.get('errorCode', 'No error code')
    error_message = r.get('errorMessage', 'No error message')
    error = ERRORS.get(error_code, Error)
    return error('{}: {}'.format(error_code, error_message))
