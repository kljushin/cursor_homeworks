# Task3
# Напишіть тести до модуля реєстрації юзера (без фласк АРІ, просто окремий клас)
# тести повинні перевіряти чи відповідає пароль пошта і ім'я вимогам,
# перевіряти чи юзера з таким іменем не має в базі
# якщо юзер створений то назад отримуємо строку "200", інакше модуль реєстрації кидатиме ексепшини
# (ексепшини потрібно написати свої)
#
# тести до модуля авторизації юзера
# метод авторизації отримує пошту і пароль і звіряє чи є такі в базі данних (за бд можете використати словник)
# якщо дані введені вірно і юзер існує то назад повертаєтсья обєкт класу UserToken
# (майже пустий клас, містить тільки аргумент строку яка задається рандомним набором символів)
#
# Після написання тестів, реалізуйте ваші методи реєстрації і авторизаії
import reg_auth
import unittest
import reg_auth_exceptions as ex


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        db = reg_auth.UsersDB()
        self.reg = reg_auth.Registration(db)

    def test_login_rules(self):
        self.assertTrue(self.reg.login_rules('Boris'))
        with self.assertRaises(ex.LoginLengthException):
            self.reg.login_rules('qw')  # Login should be more then 2 symbols
        with self.assertRaises(ex.LoginBlackListException):
            self.reg.login_rules('qw*')  # Login should be without specific symbols

    def test_psw_rules(self):
        self.assertTrue(self.reg.login_rules('Passw0rd'))
        with self.assertRaises(ex.PswLengthException):
            self.reg.psw_rules('12')  # Password should be more then 5 symbols
        with self.assertRaises(ex.PswLowCaseNeededException):
            self.reg.psw_rules('PASSSS')  # Password should contain lowercase letters
        with self.assertRaises(ex.PswUpperCaseNeededException):
            self.reg.psw_rules('passss')  # Password should contain uppercase letters
        with self.assertRaises(ex.PswDigitsNeededException):
            self.reg.psw_rules('PaSSSS')  # # Password should contain digits

    def test_email_rules(self):
        test_bad_emails = ['qwe',                    # no @ detected
                           '@qwe',                   # wrong email
                           'kl*ush@gmail.com',       # forbidden symbol
                           'wrong email@gmail.com',  # space in mailbox name
                           'qwe@super domen.com',    # space in mailserver name
                           'klush@gma)il.com',       # wrong mailserver name
                           'klush@gmail.c',          # wrong mailbox TLD
                           'klush@@gmail.com',       # @@
                           '']                       # Empty str

        test_valid_emails = ['b.klush@gmail.com',
                             'klush@gmail.com',
                             'klush123@gmail.com',
                             'klush123@gmail911.com']
        for test_email in test_valid_emails:
            self.assertTrue(self.reg.email_rules(test_email))

        for test_email in test_bad_emails:
            with self.assertRaises(ex.EmailError):
                self.reg.email_rules(test_email)

    def test_reg_user(self):
        test_user = {'login': 'Login', 'psw': 'Passw0rd', 'email': 'login@email.com'}
        self.assertEqual(self.reg.reg_user(test_user), '200')  # Success registration

        with self.assertRaises(ex.RegistrationUserExistError):
            self.reg.reg_user(test_user)  # User exist


class TestAuth(unittest.TestCase):
    def setUp(self) -> None:
        db = reg_auth.UsersDB()
        db.add_user({'login': 'Login', 'psw': 'Passw0rd', 'email': 'login@email.com'})
        self.auth = reg_auth.Auth(db)
        self.users = [[{'login': 'Login', 'psw': 'Passw0rd'}, True],  # Valid user
                      [{'login': 'Login', 'psw': 'Passw0rd1'}, False],  # Wrong user
                      [{'login': 'Login1', 'psw': 'Passw0rd'}, False]  # Wrong user
                      ]

    def test_user_exist(self):
        for user in self.users:
            self.assertIs(self.auth.user_exist(user[0]), user[1])

    def test_auth(self):
        self.assertIsInstance(self.auth.auth(self.users[0][0]), reg_auth.UserToken)  # Authorization complete
        with self.assertRaises(ex.AuthError):
            for item in range(1, len(self.users) - 1):
                self.auth.auth(self.users[item][0])  # Error auth


if __name__ == '__main__':
    unittest.main()