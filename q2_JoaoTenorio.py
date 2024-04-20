# Autor: João Pedro Rodrigues Tenório
# Matrícula: 1810518
# Disciplina: Programação Funcional
# Avaliação: AV2

import unittest
from unittest.mock import patch
from q1_JoaoTenorio import User, Customer, system_login, main

class TestPaymentSystem(unittest.TestCase):
    def setUp(self):
        self.users = (lambda: [
            User(username="tenorio", password="12345", name="João Tenório", balance=1000),
            User(username="samuel", password="54321", name="Samuel Lincoln", balance=500),
            User(username="lucas", password="123", name="Lucas", balance=100)
        ])()

    @patch('builtins.input', side_effect=['tenorio', '12345'])
    def test_successful_login(self, mock_inputs):
        user = (lambda: system_login(self.users))()
        assertions = (lambda u: (
            self.assertIsNotNone(u),
            self.assertEqual(u.name(), 'João Tenório')
        ))(user)

    @patch('builtins.input', side_effect=['tenorio', '40028922'])
    def test_failed_login(self, mock_inputs):
        user = (lambda: system_login(self.users))()
        assertion = (lambda u: self.assertIsNone(u))(user)

    @patch('builtins.input', side_effect=['sim'])
    def test_bank_confirmation_success(self, mock_inputs):
        logged_user = (lambda: self.users[0])()
        customer = (lambda: Customer(logged_user))()
        transaction_success = (lambda: customer.initiate_transaction(100, 'transferência'))()
        assertion = (lambda success: self.assertTrue(success))(transaction_success)

    @patch('builtins.input', side_effect=['tenorio', '40028922'] * 10)
    def test_stress_login_failure(self, mock_inputs):
        assertions = (lambda tests: [self.assertIsNone(system_login(self.users)) for _ in tests])(range(10))

if __name__ == '__main__':
    unittest.main()