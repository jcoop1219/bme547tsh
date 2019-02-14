import pytest
from tsh_dx_module import main

# Setting up test cases for parametrize decorator
personDict = main()
case1 = "normal thyroid function"
case2 = "hyperthyroidism"
case3 = "hypothyroidism"


@pytest.mark.parametrize("diagnosis, expectedDx", [
                        (personDict[0]["Diagnosis"], case1),
                        (personDict[1]["Diagnosis"], case2),
                        (personDict[2]["Diagnosis"], case1),
                        (personDict[3]["Diagnosis"], case3),
                        (personDict[4]["Diagnosis"], case2),
                        (personDict[5]["Diagnosis"], case1),
                        (personDict[6]["Diagnosis"], case3),
                        (personDict[7]["Diagnosis"], case2),
                        (personDict[8]["Diagnosis"], case3),
                        (personDict[9]["Diagnosis"], case2),
                        ])
def test_main(diagnosis, expectedDx):
    assert diagnosis == expectedDx
