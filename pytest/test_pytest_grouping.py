# Grouping:
# run test by defining them under a category, such as smoke:
# add @pytest.mark.<name of the category/grouping>
# py.test -m smoke -v -s
# run grouped test -> py.test -m <name of the category/group defined> -v -s
# skip any test with @pytest.mark.skip
# py.test -v -s
# run a test but if dont include in the report be it fail or pass -> @pytest.mark.xfail
# py.test -v -s

import pytest

def test_api03():
    print(" I am api 02")

@pytest.mark.skip
def test_mobile03():
    print("I am mobile 02")
    
@pytest.mark.smoke
def test_web02():
    print("I am web01")

@pytest.mark.xfail
def test_xfail():
    print("Xfail not faield yet")
    assert 1==2, "Failed"

