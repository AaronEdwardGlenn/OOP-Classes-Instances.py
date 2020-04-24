# data and functions associated with a specific class are reffered to as ATTRIBUTES and METHODS. methods are a function that is associated with a class


class Employee:
    pass    # NOTE this would error without the pass here.

# lets go over the differences between a class and an instance of a class


emp_1 = Employee()
emp_2 = Employee()

# both of these instances of the Employee class have unique ids in memory
print(emp_1)
print(emp_2)
# NOTE these are instance variables. Class variables are very different and for the next lesson

emp_1.first = 'Aaron'
emp_1.last = 'Glenn'
emp_1.email = 'a@co.com'
emp_1.pay = 100000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test@co.com'
emp_2.pay = 1111100000

print(emp_1.email)
print(emp_2.email)

# now we are going to make this more readable with less code


class Employee1:

    def __init__(self)


emp_11 = Employee1()
emp_22 = Employee1()

print(emp_1)
print(emp_2)


emp_1.first = 'Aaron'
emp_1.last = 'Glenn'
emp_1.email = 'a@co.com'
emp_1.pay = 100000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test@co.com'
emp_2.pay = 1111100000

print(emp_1.email)
print(emp_2.email)
