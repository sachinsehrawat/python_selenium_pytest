# Fixtures:
# fixtures are used to define pre-requisite  and post runs after test
# fixtures is defined by @pytest.fixture()

import pytest

@pytest.fixture()
def test_fixture01():
    print("I will be executed 1st")
    yield
    print("I will be executed last")

def test_basics01(test_fixture01):
    print(" I am main test")

# In case of large number of test and fixture is required for all tests
# Then a fixture is defined for a class and all the tests under the class will run the fixture

@pytest.mark.usefixtures("test_fixture01")
class Test_class01:
    def test_fixture02(self):
        print(" I am fixture 02")

    def test_fixture03(self):
        print("I am fixture 03")

#If we want to run the fixture only for the class level, before class execution and after execution
# we need to define the scope to class
@pytest.fixture(scope='class')
def test_fixture02():
    print("I will be executed 1st")
    yield
    print("I will be executed last")


@pytest.mark.usefixtures("test_fixture02")
class Test_class02:
    def test_fixture04(self):
        print(" I am fixture 04")

    def test_fixture05(self):
        print("I am fixture 05")
