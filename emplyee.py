class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
# Create employee instances
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)  # Output: 50000
emp_1.apply_raise()
print(emp_1.pay)  # Output: 52000

# Setting instance raise_amount to 0
emp_1.raise_amount = 0
emp_1.apply_raise()
print(emp_1.pay)  # Output: 0 (because raise_amount is 0)

# Resetting pay to 40000
emp_1.pay = 40000
print(emp_1.pay)  # Output: 40000

# Deleting instance raise_amount to use class variable again
del emp_1.raise_amount

# Set the class raise amount
Employee.set_raise_amt(1.5)

# Apply raise and print new pay
emp_1.apply_raise()
print(emp_1.pay)  # Output: 60000 (because class raise_amount is 1.5)

# Print number of employees and raise amount
print(Employee.num_of_emps)  # Output: 2
print(Employee.raise_amount)  # Output: 1.5