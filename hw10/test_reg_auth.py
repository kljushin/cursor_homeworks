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
            self.reg.login_rules('qw')
        with self.assertRaises(ex.LoginBlackListException):
            self.reg.login_rules('qw*')

    def test_psw_rules(self):
        self.assertTrue(self.reg.login_rules('Passw0rd'))
        with self.assertRaises(ex.PswLengthException):
            self.reg.psw_rules('12')
        with self.assertRaises(ex.PswLowCaseNeededException):
            self.reg.psw_rules('PASSSS')
        with self.assertRaises(ex.PswUpperCaseNeededException):
            self.reg.psw_rules('passss')
        with self.assertRaises(ex.PswDigitsNeededException):
            self.reg.psw_rules('PaSSSS')

    def test_email_rules(self):
        self.assertTrue(self.reg.email_rules('qwe@qwe.wqe'))
        with self.assertRaises(ex.EmailError):
            self.reg.email_rules('qwe')
            self.reg.email_rules('@qwe')
            self.reg.email_rules('')

    def test_reg_user(self):
        test_user = {'login': 'Login', 'psw': 'Passw0rd', 'email': 'login@email.com'}
        self.assertEqual(self.reg.reg_user(test_user), '200')

        with self.assertRaises(ex.RegistrationUserExistError):
            self.reg.reg_user(test_user)


class TestAuth(unittest.TestCase):
    def setUp(self) -> None:
        db = reg_auth.UsersDB()
        db.add_user({'login': 'Login', 'psw': 'Passw0rd', 'email': 'login@email.com'})
        self.auth = reg_auth.Auth(db)
        self.users = [[{'login': 'Login', 'psw': 'Passw0rd'}, True],
                      [{'login': 'Login', 'psw': 'Passw0rd1'}, False],
                      [{'login': 'Login1', 'psw': 'Passw0rd'}, False]
                      ]

    def test_user_exist(self):
        for user in self.users:
            self.assertIs(self.auth.user_exist(user[0]), user[1])

    def test_auth(self):
        self.assertIsInstance(self.auth.auth(self.users[0][0]), reg_auth.UserToken)
        with self.assertRaises(ex.AuthError):
            for item in range(1, len(self.users) - 1):
                self.auth.auth(self.users[item][0])


if __name__ == '__main__':
    unittest.main()