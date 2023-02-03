# Created by @dillibk777 at 03/02/23
class HandleException:
    """A wrapper class that catches exceptions and raises them to the next level.

    This class takes a function as an argument in its constructor and creates a callable
    object that calls the given function when it is invoked. The callable object also
    catches any exceptions that are raised by the function and re-raises them, so that
    they can be handled at a higher level in the call stack.

    By default, all exceptions are caught and re-raised. However, it is possible to
    specify a list of custom exceptions to catch, using the 'exceptions' argument.

    Args:
    func (callable): The function to be wrapped
    exceptions (list, optional): A list of custom exceptions to catch. Defaults to None,
        which means that all exceptions will be caught.

    Example:
    @HandleException
    def my_function():
        # Your code here
        pass
    """

    def __init__(self, func, exceptions=None):
        self.func = func
        self.exceptions = exceptions

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as e:
            if self.exceptions is None or type(e) in self.exceptions:
                raise e
