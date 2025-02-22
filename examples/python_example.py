from super_init import super_init

class Parent:
    def __init__(self):
        print("Parent __init__ called")

@super_init
class Child(Parent):
    def __init__(self):
        print("Child __init__ called")

child1 = Child()  # Parent's __init__ is not called
child2 = Child(_use_super=True)  # Parent's __init__ is called

