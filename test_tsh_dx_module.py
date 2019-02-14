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
def test_calculateDx(diagnosis, expectedDx):
    assert diagnosis == expectedDx
