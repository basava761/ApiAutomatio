import pytest


@pytest.fixture(scope="class")
def setup():
    print("iam executing first")
    yield
    print("ill be executed last")


@pytest.fixture()
def dataload():
    print("user data defined")
    return ["patil", "basava"]


@pytest.fixture(params=[("chrome","basava"), "firefox", "IE"])
def cross_browser(request):
    return request.param
