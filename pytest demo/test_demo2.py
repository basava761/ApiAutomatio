import pytest


# @pytest.mark.skip

def test_creditcard():
    print("i dont have credit card")


@pytest.mark.smoke
def test_2credit_card(setup):
    print("i have 3 crdit card")


pytest.fixture()


def setup():
    print("iam executing first")


def test_fixture_demo(setup):
    print("ill execute steps in fixture demo")
