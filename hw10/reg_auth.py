import string
import reg_auth_exceptions as ex  # exceptions
import random
import re

class UsersDB:
    '''
    Database class
    '''
    def __init__(self):
        self.users_db = {}

    def add_user(self, user):
        if not user['login'] in list(self.users_db.keys()):
            self.users_db[user['login']] = {'psw': user['psw'], 'email': user['email']}
            return True
        else:
            raise ex.RegistrationUserExistError


class UserToken:
    def __init__(self, token):
        self.token = token


class Registration:
    '''
    Registration service
    '''
    def __init__(self, database):
        self.db = database

    def rules_check(self, user):
        if not self.login_rules(user['login']):
            return False
        if not self.psw_rules(user['psw']):
            return False
        if not self.email_rules(user['email']):
            return False
        return True

    def reg_user(self, user):
        if self.rules_check(user):
            if self.db.add_user(user):
                print(self.db.users_db)
                return '200'

    def login_rules(self, login):  # Check login
        if len(login) < 3:
            raise ex.LoginLengthException
        if not set(login).isdisjoint(string.punctuation):
            raise ex.LoginBlackListException
        return True

    def psw_rules(self, psw):  # Check password
        _low = set(string.ascii_lowercase)
        _upper = set(string.ascii_uppercase)
        _digits = set(string.digits)
        set_psw = set(psw)
        if len(psw) < 6:
            raise ex.PswLengthException
        if not set(set_psw).isdisjoint(string.punctuation):
            raise ex.PasswordBlackListException
        if set_psw.isdisjoint(_low):
            raise ex.PswLowCaseNeededException
        if set_psw.isdisjoint(_upper):
            raise ex.PswUpperCaseNeededException
        if set_psw.isdisjoint(_digits):
            raise ex.PswDigitsNeededException

        return True

    def email_rules(self, email):  # Check email
        # email_components = email.split('@')
        # if not len(email_components) == 2:
        #     raise ex.EmailError
        # if len(email_components[0]) == 0 or len(email_components[1]) == 0:
        #     raise ex.EmailError
        # return True
        if re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
            return True
        else:
            raise ex.EmailError


class Auth:
    '''
    Authentication
    '''
    def __init__(self, database):
        self.db = database

    def auth(self, user):
        if self.user_exist(user):
            return UserToken(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16)))
        else:
            raise ex.AuthError

    def user_exist(self, user):  # user exists check
        if user['login'] in list(self.db.users_db.keys()):
            if user['psw'] == self.db.users_db[user['login']]['psw']:
                return True
            else:
                return False
        return False
