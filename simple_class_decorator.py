from typing import Any, Callable

class SimpleClassDecorator:
    """
    Our simple test decorator class
    """
    def __init__(self, func: Callable) -> None:
        """
        Args:
            func (Callable): Function that we're going to decorate
        """
        self.func = func
        
    def __call__(self, *args: Any, **kwargs: Any) -> Callable:
        """
        Returns:
            Callable: We return our function to get returned value
        """
        print('до вызова функции', self.func.__name__)
        decorated_func = self.func(*args, **kwargs)
        print('после вызова функции', self.func.__name__)
        return decorated_func
