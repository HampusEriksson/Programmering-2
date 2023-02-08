class Test:
    my_tests = []
    def __init__(self, name):
        self.name = name
        my_tests.append(self)

    @classmethod
    def print_all():
        print(cls.my_tests)

t1 = Test()
Test.print_all()
