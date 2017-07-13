class TestClazzWithInit:

    def __init__(self, parameter):
        self.parameter = parameter

    def test_something_with_init(self):
        assert True

    def with_init_something_test(self):
        assert True

    def some_method_with_init(self):
        assert False
