class Person:

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Employee(Person):

    def __init__(self, first, last, staffnum):
        # Person.__init__(self, first, last)
        super().__init__(first, last)
        self.staff_number = staffnum

    def get_employee_data(self):
        return self.get_full_name() + ", " + self.staff_number


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

# Marge
print(x.get_full_name())

print(80*"#")

# Homer
print(y.get_full_name())
print(y.get_employee_data())
