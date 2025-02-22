def super_init(cls):
    """
    A decorator that allows users to selectively call the parent class's __init__ method.
    """
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        if kwargs.pop("_use_super", False):
            super(cls, self).__init__(*args, **kwargs)
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

