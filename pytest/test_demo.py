# Basic Pytest:
# pytest file name always starts/ends with test_ or _test
# name of the function inside pytest starts with test
# pytest run command to run all pytest file via cmd -> py.test -v -s
# run specific files via pytest -> py.test <filename.py> -v -s
# py.test test_demo.py -v -s
# run tests using regex -> py.test -k <test regex name> -v -s
# py.test -k  api -v -s

def test_first_program():
    print("Hello")

def test_api02():
    print(" I am api 02")

def test_mobile02():
    print("I am mobile 02")

def test_web01():
    print("I am web01")
