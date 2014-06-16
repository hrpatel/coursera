## quiz0a q1
print type(3.14159)
print
print


## q3
def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60

print clock_helper(90)
print
print


## q5
my_string = "blah"

#print my_string[len(my_string)]
print my_string[-1]
#print my_string.last()
#print my_string.pop()
print
print


## q7
val1 = [1, 2, 3]
val2 = val1[1:]
val1[2]  = 4

print val2[1]
print
print


## q9
def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    i = 0
    while i < 25:
        lst.append(lst[-1] + lst[-2] + lst[-3])
        i += 1
    
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three
print sum_three[10]
print sum_three[20]
print
print


## q10
class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fees = 0
       
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            self.fees += 5
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees

    
my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()
    
    

