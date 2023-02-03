# Created by @dillibk777 at 03/02/23
import unittest
from handle_exception import HandleException


class TestHandleException(unittest.TestCase):
    def test_handle_exception(self):
        @HandleException
        def my_function():
            raise ValueError("Test exception")

        with self.assertRaises(ValueError):
            my_function()
