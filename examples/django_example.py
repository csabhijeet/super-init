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

# Example usage
obj = MyModel(_use_super=True)  # Calls BaseModel's __init__

