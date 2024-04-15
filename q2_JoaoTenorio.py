# Autor: João Pedro Rodrigues Tenório
# Matrícula: 1810518
# Disciplina: Programação Funcional
# Avaliação: AV2

import unittest
from unittest.mock import patch
from q1_JoaoTenorio import User, Customer, system_login, Transaction, Cashier

class TestPaymentSystem(unittest.TestCase):
    def setUp(self):
        # Usuários de teste
        create_users = lambda: [
            User("tenorio", "12345", "João Tenório", 1000),
            User("samuel", "54321", "Samuel Lincoln", 500)
        ]
        self.users = create_users()

    @patch('builtins.input', side_effect=["tenorio", "12345"])
    def test_login_success(self, mocked_input):
        print("Testar login bem-sucedido")
        user = system_login(self.users)
        self.assertEqual(user, self.users[0])

    @patch('builtins.input', side_effect=["tenorio", "senhaerrada"])
    def test_login_failure(self, mocked_input):
        print("Testar falha no login")
        user = system_login(self.users)
        self.assertIsNone(user)

    @patch('builtins.input', side_effect=["sim"])
    def test_bank_confirmation_success(self, mocked_input):
        print("Testar confirmação do banco com sucesso")
        create_cashier = lambda: Cashier(Transaction(self.users[0]))
        cashier = create_cashier()
        result = cashier.bank_confirmation()
        self.assertTrue(result)

    def system_login(users, entered_username, entered_password):
        check_login = lambda user: user.verify_login(entered_username, entered_password)()
        valid_users = [user for user in users if check_login(user)]
        return valid_users[0] if valid_users else print("Falha no login. Por favor, verifique seu usuário e senha.") or None

if __name__ == "__main__":
    unittest.main()