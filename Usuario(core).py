class Usuario:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
    	self.account_balance += amount
        
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        if(self.account_balance < 0):
            print(f'el saldo de {self.name} es insuficiente')
    
    def display_user_balance(self):
        print(f'Su Nombre es {self.name} - Su email es {self.email} - Su Saldo es {self.account_balance}')
        

# JUANITA
Juanita = Usuario('Juanita', 'Juanita123@gmail.com')
Juanita.make_deposit(100)
Juanita.make_deposit(50)
Juanita.make_deposit(10)
Juanita.make_withdrawal(50)
Juanita.display_user_balance()
# PEDRITO
Pedrito = Usuario('Pedro', 'Pedro@gmail.com')
Pedrito.make_deposit(50)
Pedrito.make_deposit(50)
Pedrito.make_withdrawal(50)
Pedrito.make_withdrawal(60)
Pedrito.display_user_balance()
# ESTEBAN
Esteban = Usuario('Esteban', 'EstebanElCuchuflí@gmail.com')
Esteban.make_deposit(200)
Esteban.make_withdrawal(10)
Esteban.make_withdrawal(60)
Esteban.make_withdrawal(15)
Esteban.display_user_balance()


