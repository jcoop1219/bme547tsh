def main():
    inFile = "test_data.txt"
    jsonDir = "JSONfiles"
    dataFile = readFile(inFile)
    personDictList = fileToDict(dataFile)
    personDictList = calculateDx(personDictList)
    outputToJSON(personDictList, jsonDir)


def readFile(inFile):
    """Reads a file into Python

    Given an input .txt file, reads the file into Python for later usage.

    Args:
        inFile (string): the relative path location of the input .txt file

    Returns:
        dataFile (IO file): dataFile with lines which will be parsed later
    """
    dataFile = open(inFile, "r")
    return dataFile


def fileToDict(dataFile):
    """Parses lines of a data file and stores the data discretely to dictionary

    Given a multi-line data file with patient firstName, lastName, age,
    gender, and TSH values, parses the file line by line. First creates
    personDictList which will be a list of dictionaries (1 dictionary for
    each patient). Parses out patient's firstName, lastName, age, gender,
    and sorted list of TSH values. After parsing for individual patient, calls
    to storeToDict to put info in singlePersonDict unique to patient which
    then gets stored as an item in dictionary list personDictList.

    Args:
        dataFile (IO file): dataFile with lines for each patient's info

    Returns:
        personDictList (list): list of dictionaries, with each item being a
                               dictionary for a single patient
    """
    lineCount = 0
    personNum = -1
    personDictList = []
    for line in dataFile:
        if line.startswith("END"):  # if we're at the end of the file, quit
            break
        lineCount += 1
        lineType = lineCount % 4
        if lineType == 1:  # name line
            personNum += 1
            personDictList.append({})  # initialize new entry in list
            firstName = line.rstrip("\n").split(" ")[0]
            lastName = line.rstrip("\n").split(" ")[1]
        elif lineType == 2:  # age line
            age = int(line.rstrip("\n"))
        elif lineType == 3:  # gender line
            gender = line.rstrip("\n")
        else:  # TSH line
            tshList = line.lstrip("TSH,").rstrip("\n").split(",")
            for idx, item in enumerate(tshList):
                tshList[idx] = float(item)
            tshList.sort()  # sorts list of TSH values from low to high
            singlePersonDict = storeToDict(firstName, lastName, age, gender,
                                           tshList)
            personDictList[personNum] = singlePersonDict
    return personDictList


def storeToDict(firstName, lastName, age, gender,
                tshList):
    """Stores patient's info to a dictionary unique to the patient

    Stores the patient's firstName, lastName, age, gender, and TSH value list
    to a dictionary unique to the patient which will later be added to the
    dictionary list personDictList.

    Args:
        firstName (string): patient's first name
        lastName (string): patient's last name
        age (int): patient's age in years
        gender (string): patient's gender
        tshList (list): list of floats of sorted TSH values for patient

    Returns:
        singlePersonDict (dict): dictionary of info unique to this patient

    """
    singlePersonDict = {}  # initialize dict for this one patient
    singlePersonDict["First Name"] = firstName
    singlePersonDict["Last Name"] = lastName
    singlePersonDict["Age"] = age
    singlePersonDict["Gender"] = gender
    singlePersonDict["TSH"] = tshList
    return singlePersonDict


def calculateDx(personDictList):
    """Calculates the patient's diagnosis for thryoid function

    Loops over the TSH values for each patient and assigns a diagnosis
    accordingly:
        "hyperthyroidism" = has any TSH value below 1.0
        "hypothyroidism" = has any TSH value above 4.0
        "normal thyroid function" = all TSH values within 1.0 to 4.0 inclusive
    Stores to "Diagnosis" key in single patient's dictionary which is then
    stored to the personDictList dictionary list.

    Args:
        personDictList (list): list of dictionaries, with each item being a
                               dictionary for a single patient

    Returns:
        personDictList (list): list of dictionaries updated with "Diagnosis"
                               key for each patient's unique dictionary
    """
    for singlePersonDict in personDictList:
        tshList = singlePersonDict["TSH"]
        diagnosis = "normal thyroid function"
        for tshVal in tshList:
            if tshVal < 1.0:
                diagnosis = "hyperthyroidism"
            elif tshVal > 4.0:
                diagnosis = "hypothyroidism"
        singlePersonDict["Diagnosis"] = diagnosis
    return personDictList


def outputToJSON(personDictList, jsonDir):
    """Converts dictionary list to JSON files specific to each patient

    Makes a new directory (if one does not exist) to store JSON files in.
    Then loops over each single patient dictionary singlePersonDict within
    dictionary list personDictList to create a JSON file specific to each
    patient.

    Args:
        personDictList (list): list of dictionaries, with each item being a
                               dictionary for a single patient
        jsonDir (string): relative path directory name for place to store
                          output JSON files

    Returns:
        Creates JSON files within jsonDir directory
    """
    import json
    makeDirectory(jsonDir)
    for singlePersonDict in personDictList:
        firstName = singlePersonDict["First Name"]
        lastName = singlePersonDict["Last Name"]
        fileName = firstName + "-" + lastName + ".json"
        outFile = open(fileName, "w")
        json.dump(singlePersonDict, outFile)
        outFile.close


def makeDirectory(jsonDir):
    """Creates a directory for JSON files to be store

    Checks if a directory already exists to store JSON files, and if not
    creates a new directory for them.

    Args:
        jsonDir (string): relative path directory name for place to store
                          output JSON files
    Returns:
        None
    """
    import os
    if os.path.isdir(jsonDir) is False:
        os.mkdir(jsonDir)
    os.chdir(jsonDir)

if __name__ == "__main__":
    main()
