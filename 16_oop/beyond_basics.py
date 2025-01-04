class Parent:
    def print_hello(self):
        print('Hello, World!')


class Child(Parent):
    def some_new_method(self):
        print('Parent class objects don\'t have this method')


class GrandChild(Child):
    def another_new_method(self):
        print('Only Grandchild class objects have this method')


print('Create a Parent class object and call its methods')
parent = Parent()
parent.print_hello()
print(end='\n\n')

print('Create a Child class object and call its methods')
child = Child()
child.print_hello()
child.some_new_method()
print(end='\n\n')

print('Create a GrandChild class object and call its methods')
grandchild = GrandChild()
grandchild.print_hello()
grandchild.some_new_method()
grandchild.another_new_method()
print(end='\n\n')

print('An error:')
parent.some_new_method()