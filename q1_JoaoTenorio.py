# Autor: João Pedro Rodrigues Tenório
# Matrícula: 1810518
# Disciplina: Programação Funcional
# Avaliação: AV2

import sys

class Customer:
    def __init__(self, user):
        self.user = user

    def initiate_transaction(self, amount, payment_method):
        transaction = Transaction(self.user)
        return transaction.create_transaction(amount, payment_method)

class User:
    def __init__(self, username, password, name, balance):
        self.username = username
        self.password = password
        self.name = name
        self.balance = balance

    def verify_login(self, entered_username, entered_password):
        return lambda: self.username == entered_username and self.password == entered_password

    def debit_balance(self, amount):
        check_balance = lambda balance, amt: balance - amt if balance >= amt else balance
        self.balance = check_balance(self.balance, amount)
        return self.balance != amount

class Transaction:
    def __init__(self, user):
        self.status = 'open'
        self.user = user

    def create_transaction(self, amount, payment_method):
        payment_methods = {
            'dinheiro': lambda: Cashier(self).receive_cash(amount),
            'transferência': lambda: Cashier(self).process_transfer(amount),
            'crédito': lambda: Cashier(self).process_credit(amount)
        }
        return payment_methods.get(payment_method, lambda: False)()

    def close_transaction(self):
        print("Transação completa.")
        self.status = 'closed'

    def cancel_transaction(self):
        print("Transação cancelada.")
        self.status = 'cancelled'

class Cashier:
    def __init__(self, transaction):
        self.transaction = transaction

    def receive_cash(self, amount):
        cash_flow = lambda: (
            print("Dinheiro Recebido"),
            print("Recibo de Pagamento Impresso"),
            print("Entregando Recibo de Pagamento"),
            self.transaction.close_transaction(),
            True
        ) if self.transaction.user.debit_balance(amount) else (
            self.transaction.cancel_transaction(),
            False
        )
        return cash_flow()[4]

    def process_transfer(self, amount):
        print("Providenciando detalhes do depósito bancário")
        process = lambda: self.receive_cash(amount) if self.bank_confirmation() else (self.transaction.cancel_transaction(), False)[1]
        return process()

    def process_credit(self, amount):
        print("Recolhendo dados de crédito da conta")
        process = lambda: self.receive_cash(amount) if self.bank_confirmation() else (self.transaction.cancel_transaction(), False)[1]
        return process()

    def bank_confirmation(self):
        response = input("O pagamento foi confirmado pelo banco? (sim/não): ").lower()
        return response == "sim"

def system_login(users):
    entered_username = input("Digite o usuário: ")
    entered_password = input("Digite a senha: ")
    check_login = lambda user: user.verify_login(entered_username, entered_password)()
    valid_users = [user for user in users if check_login(user)]
    return valid_users[0] if valid_users else print("Falha no login. Por favor, verifique seu usuário e senha.") or None

def main():
    users = [
        User(username="tenorio", password="12345", name="João Tenório", balance=1000),
        User(username="samuel", password="54321", name="Samuel Lincoln", balance=500)
    ]
    print("Bem-vindo ao Sistema de Pagamentos")
    logged_user = system_login(users)
    
    if logged_user:
        print(f"Login bem-sucedido! Bem-vindo(a) {logged_user.name}. Seu saldo é {logged_user.balance}.")
        successful_transaction = False
        while not successful_transaction:
            amount = float(input("Digite o valor da transação: "))
            if amount > logged_user.balance:
                print("Saldo insuficiente para realizar a transação.")
                continue
            payment_method = input("Escolha o método de pagamento (dinheiro, transferência, crédito): ").lower()
            customer = Customer(logged_user)
            successful_transaction = customer.initiate_transaction(amount, payment_method)
            if not successful_transaction:
                print("Erro na transação, tente novamente.")
    else:
        print("Erro de autenticação.")

if __name__ == "__main__":
    main()