import unittest
from super_init import super_init

class Parent:
    def __init__(self):
        self.value = "Parent initialized"

@super_init
class Child(Parent):
    def __init__(self):
        self.child_value = "Child initialized"

class TestSuperInit(unittest.TestCase):
    def test_without_super(self):
        child = Child()
        self.assertFalse(hasattr(child, "value"))  # Parent __init__ should not run

    def test_with_super(self):
        child = Child(_use_super=True)
        self.assertTrue(hasattr(child, "value"))  # Parent __init__ should run

if __name__ == "__main__":
    unittest.main()

