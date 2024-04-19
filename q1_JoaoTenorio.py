import os

os.system('cls')

class Customer:
    def __init__(self, user):
        self.user = lambda: user

    def initiate_transaction(self, amount, payment_method):
        transaction = lambda: Transaction(self.user())
        return transaction().create_transaction(amount, payment_method)

class User:
    def __init__(self, username, password, name, balance):
        self.username = lambda: username
        self.password = lambda: password
        self.name = lambda: name
        self.balance = lambda: balance

    def verify_login(self, entered_username, entered_password):
        return lambda: self.username() == entered_username and self.password() == entered_password

    def debit_balance(self, amount):
        check_balance = lambda balance, amt: balance - amt if balance >= amt else balance
        update_balance = lambda: (lambda new_balance: setattr(self, 'balance', lambda: new_balance))(check_balance(self.balance(), amount))
        update_balance()
        return lambda: self.balance() != amount

class Transaction:
    def __init__(self, user):
        self.status = lambda: 'open'
        self.user = lambda: user

    def create_transaction(self, amount, payment_method):
        payment_methods = {
            'dinheiro': lambda: Cashier(self).receive_cash(amount),
            'transferência': lambda: Cashier(self).process_transfer(amount),
            'crédito': lambda: Cashier(self).process_credit(amount)
        }
        return payment_methods[payment_method]() if payment_method in payment_methods else lambda: False()

    def close_transaction(self):
        print("Transação completa.")
        self.status = lambda: 'closed'

    def cancel_transaction(self):
        print("Transação cancelada.")
        self.status = lambda: 'cancelled'

class Cashier:
    def __init__(self, transaction):
        self.transaction = lambda: transaction

    def receive_cash(self, amount):
        cash_flow = lambda: (
            print("Dinheiro Recebido"),
            print("Recibo de Pagamento Impresso"),
            print("Entregando Recibo de Pagamento"),
            self.transaction().close_transaction(),
            True
        ) if self.transaction().user().debit_balance(amount)() else (
            self.transaction().cancel_transaction(),
            False
        )
        return cash_flow()[4]

    def process_transfer(self, amount):
        print("Providenciando detalhes do depósito bancário")
        process = lambda: (print("Transação completa."), True) if self.bank_confirmation() else (print("Transação cancelada."), False)
        return process()[1]

    def process_credit(self, amount):
        print("Requisitando detalhes da conta de crédito")
        process = lambda: (print("Transação completa."), True) if self.bank_confirmation() else (print("Transação cancelada."), False)
        return process()[1]

    def bank_confirmation(self):
        get_response = lambda: input("O pagamento foi confirmado pelo banco? (sim/não): ").lower()
        return get_response() == "sim"


def system_login(users):
    credentials = lambda: (input("Digite o usuário: "), input("Digite a senha: "))
    entered_credentials = lambda: credentials()
    check_login = lambda user, creds: user.verify_login(creds[0], creds[1])()
    valid_users = lambda creds: [user for user in users if check_login(user, creds)]
    result = lambda v_users: v_users[0] if v_users else print("Falha no login. Por favor, verifique seu usuário e senha.") or None
    return result(valid_users(entered_credentials()))

def main():
    users = [
        User(username="tenorio", password="12345", name="João Tenório", balance=1000),
        User(username="samuel", password="54321", name="Samuel Lincoln", balance=500),
        User(username="lucas", password="123", name="Lucas", balance=100)
    ]
    print("Bem-vindo ao Sistema de Pagamentos")
    logged_user = system_login(users)
    
    if logged_user:
        print(f"Login bem-sucedido! Bem-vindo(a) {logged_user.name()}. Seu saldo é {logged_user.balance()}.")
        successful_transaction = False
        while not successful_transaction:
            amount = float(input("Digite o valor da transação: "))
            if amount > logged_user.balance():
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
