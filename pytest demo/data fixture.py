import pytest


@pytest.mark.usefixtures("dataload")
class Test_example:

    def test_edit_profile(self, dataload):
        print(dataload[0])
        print(dataload[1])



