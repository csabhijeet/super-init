# super_init - A Flexible Inheritance Decorator for Python

## Overview
`super_init` is a Python decorator that provides more control over parent class initialization when using inheritance. It allows developers to selectively invoke the parent class's `__init__` method using a simple flag, rather than always requiring explicit `super().__init__()` calls.

This decorator is particularly useful for:
- Preventing unintended calls to parent initializers.
- Making class hierarchies more flexible.
- Reducing boilerplate code in OOP-based Python applications.

## Installation
You can install `super_init` via pip:

```bash
pip install super_init
```

## How It Works
By default, Python requires manually calling `super().__init__()` inside a subclass if you want the parent’s `__init__` to execute. The `@super_init` decorator changes this by adding an optional `_use_super` parameter to the subclass’s constructor.

### Without `@super_init` (Standard Python Inheritance)
```python
class Parent:
    def __init__(self):
        print("Parent __init__ called")

class Child(Parent):
    def __init__(self):
        print("Child __init__ called")
        super().__init__()

c = Child()
# Output:
# Child __init__ called
# Parent __init__ called
```
In this approach, the parent class’s `__init__` is always executed when `super().__init__()` is explicitly called.

### With `@super_init` Decorator
```python
from super_init import super_init

class Parent:
    def __init__(self):
        print("Parent __init__ called")

@super_init
class Child(Parent):
    def __init__(self):
        print("Child __init__ called")

c1 = Child()
# Output:
# Child __init__ called

c2 = Child(_use_super=True)
# Output:
# Child __init__ called
# Parent __init__ called
```
Now, the parent class `__init__` is **only called if explicitly requested** by passing `_use_super=True`.

## Use Cases
### 1. Simplifying OOP in Python
Many real-world applications involve complex inheritance structures where not every subclass needs to call the parent’s `__init__`. `@super_init` makes this decision explicit at runtime.

```python
@super_init
class AdvancedChild(Parent):
    def __init__(self, data):
        print(f"AdvancedChild initialized with data: {data}")
        if data:
            super().__init__()
```

### 2. Django Models Example
Django models often require calling the parent’s initializer when overriding the default behavior.

```python
from django.db import models
from super_init import super_init

@super_init
class BaseModel(models.Model):
    class Meta:
        abstract = True
    
    def __init__(self, *args, **kwargs):
        print("BaseModel __init__ called")
        super().__init__(*args, **kwargs)

@super_init
class MyModel(BaseModel):
    name = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        print("MyModel __init__ called")
        super().__init__(*args, **kwargs)

# Usage
obj = MyModel(_use_super=True)
# Output:
# MyModel __init__ called
# BaseModel __init__ called
```

### 3. Third-Party Libraries
You can use `@super_init` in frameworks like Flask, FastAPI, or Pydantic to control when base class initialization occurs dynamically.

## Existing Limitations of Python’s OOP
### 1. Unnecessary Parent Initialization
In standard Python OOP, calling `super().__init__()` is required for running parent initialization, even if it's sometimes unnecessary. This leads to redundant calls and extra processing.

### 2. Hidden Bugs in Multi-Inheritance
In multiple inheritance scenarios, forgetting to call `super().__init__()` in some subclasses can cause unexpected behavior.

### 3. Boilerplate Code
Developers often write unnecessary `super().__init__()` calls, making the code verbose.

## What `super_init` Changes
### ✅ Selective Parent Initialization
With `@super_init`, subclasses **only invoke the parent’s `__init__` when required**, reducing redundant execution.

### ✅ Cleaner Code
You don’t have to manually check whether to call `super().__init__()` in every subclass. The `_use_super` flag makes it explicit at object creation.

### ✅ Supports Existing Python Code
`@super_init` does not interfere with standard inheritance but enhances its flexibility.

## Running Tests
To verify functionality, run the tests:

```bash
pytest tests/
```

## Contributing
We welcome contributions! If you have ideas to improve `super_init`, feel free to submit a pull request.

1. Fork the repository.
2. Clone the fork:
   ```bash
   git clone https://github.com/your-username/super-init.git
   ```
3. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
4. Make changes and run tests.
5. Push and create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Developed by Abhijeet Kumar.

## Links
- **GitHub Repository**: [https://github.com/csabhijeet/super-init](https://github.com/csabhijeet/super-init)
- **PyPI Package**: [https://pypi.org/project/super-init/](https://pypi.org/project/super-init/) (Coming soon!)
