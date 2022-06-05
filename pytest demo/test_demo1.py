import pytest


def test_first():
    print("hello")


@pytest.mark.smoke
def test_second(setup):
    print("learning fixtures")


# @p
# @pytest.mark.xfail
def test100(cross_browser):
    print("cross_browser[1]")
