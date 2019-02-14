import pytest
import tsh_dx_module as tsh

# Populating dictionary with data for testing
inFile = "test_data.txt"
jsonDir = "JSONfiles"
dataFile = tsh.readFile(inFile)
personDictList = tsh.fileToDict(dataFile)
personDictList = tsh.calculateDx(personDictList)

# Setting up test cases for parametrize decorator
case1 = "normal thyroid function"
case2 = "hyperthyroidism"
case3 = "hypothyroidism"


@pytest.mark.parametrize("diagnosis, expectedDx", [
                        (personDictList[0]["Diagnosis"], case1),
                        (personDictList[1]["Diagnosis"], case2),
                        (personDictList[2]["Diagnosis"], case1),
                        (personDictList[3]["Diagnosis"], case3),
                        (personDictList[4]["Diagnosis"], case2),
                        (personDictList[5]["Diagnosis"], case1),
                        (personDictList[6]["Diagnosis"], case3),
                        (personDictList[7]["Diagnosis"], case2),
                        (personDictList[8]["Diagnosis"], case3),
                        (personDictList[9]["Diagnosis"], case2),
                        ])
def test_calculateDx(diagnosis, expectedDx):
    assert diagnosis == expectedDx
