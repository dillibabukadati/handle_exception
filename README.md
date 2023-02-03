# HandleException - Python Wrapper Class to Catch Exceptions

[![PyPI version](https://badge.fury.io/py/handle-exception.svg)](https://badge.fury.io/py/handle-exception)

HandleException is a Python wrapper class that helps to catch exceptions and raise them to an upper level. With HandleException, you can easily wrap any function that you want to monitor for exceptions and handle them as desired.

## Installation
```
pip install handle-exception
```
## Usage
To use HandleException, simply decorate the function that you want to wrap with the HandleException decorator. For example:

```
from handle_exception import HandleException

@HandleException
def my_function():
    raise ValueError("Test exception")
```
In this example, if the function my_function raises an exception, HandleException will catch it and raise it to the upper level. This way, you can handle exceptions in a centralized way, instead of having to write try-except blocks in multiple places.

## Custom Exceptions
HandleException also allows you to catch specific custom exceptions by passing a list of exception classes as an argument to the ExceptionRaiser decorator. For example:
```
from handle_exception import ExceptionRaiser

class CustomException(Exception):
    pass

@ExceptionRaiser(exceptions=[CustomException])
def my_function():
    raise CustomException("This is a custom exception.")
```
In this example, the function my_function raises a custom exception, CustomException, which will be caught by HandleException.

## Example
```
from handle_exception import HandleException

@HandleException
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
```
In this example, the divide function is decorated with the HandleException decorator. This means that any exceptions raised in the divide function will be caught and handled by the HandleException class. The code is much cleaner and easier to understand, as it doesn't contain a try-except block or have to worry about handling exceptions manually.
## Contributing
We welcome contributions to HandleException! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and write tests for them.
4. Submit a pull request.

## License

HandleException is released under the MIT License.

We welcome contributions to this library. If you have an idea for a new feature or have found a bug, please open an issue on Github.

## Buy me a Coffee
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dillibabukadati)

