class LoginLengthException(Exception):
    pass


class LoginBlackListException(Exception):
    pass


class PswLengthException(Exception):
    pass


class PswLowCaseNeededException(Exception):
    pass


class PswUpperCaseNeededException(Exception):
    pass


class PswDigitsNeededException(Exception):
    pass


class PasswordBlackListException(Exception):
    pass


class EmailError(Exception):
    pass


class RegistrationUserExistError(Exception):
    pass


class RegistrationError(Exception):
    pass


class AuthError(Exception):
    pass
