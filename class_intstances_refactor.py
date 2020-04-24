# now we are going to make this more readable with less code


class Employee:
    def __init__(self, first, last, pay):  # this is like the constructor on initialize
        # when we create methods within a class, they recieve the first instance automatically. (self) is what it should be called
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # forgeting self here will error "takes 0 positional arguments but 1 was given"
        return('{}, {}'.format(self.first, self.last))


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)

print(emp_1)
print(emp_2)


print(emp_1.email)
print(emp_2.email)

# now we will add methods to the class
# so lets put the functionality for this in one place this starts on line 12
print('{}, {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())
