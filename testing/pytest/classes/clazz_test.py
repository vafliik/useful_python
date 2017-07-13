"""
This file will be inspected, as it matches *_test.py pattern
"""


class ClazzTest:
    """
    This class won't be discovered, as it does not start with Test...
    """
    def test_something_useful(self):
        # discovered: method starts with test_
        assert True

    def something_useful_test(self):
        # not discovered
        assert True

    def some_useful_method(self):
        # not discovered
        assert False


class TestAnotherClazz:
    """
    This class will be discovered, as it starts with Test...
    """
    def test_another_clazz_method(self):
        # discovered: method starts with test_
        assert True
