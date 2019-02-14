def main():
    inFile = "test_data.txt"
    jsonDir = "JSONfiles"
    dataFile = readFile(inFile)
    personDict = fileToDict(dataFile)
    personDict = calculateDx(personDict)
    outputToJSON(personDict, jsonDir)


def readFile(inFile):
    dataFile = open(inFile, "r")
    return dataFile


def fileToDict(dataFile):
    lineCount = 0
    personNum = -1
    personDict = []
    for line in dataFile:
        if line.startswith("END"):  # if we're at the end of the file, quit
            break
        lineCount += 1
        lineType = lineCount % 4
        if lineType == 1:  # name line
            personNum += 1
            personDict.append({})
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
            personDict = storeToDict(personDict, personNum, firstName,
                                     lastName, age, gender, tshList)
    return personDict


def storeToDict(personDict, personNum, firstName,
                lastName, age, gender, tshList):
    personDict[personNum]["First Name"] = firstName
    personDict[personNum]["Last Name"] = lastName
    personDict[personNum]["Age"] = age
    personDict[personNum]["Gender"] = gender
    personDict[personNum]["TSH"] = tshList
    return personDict


def calculateDx(personDict):
    for person in personDict:
        tshList = person["TSH"]
        diagnosis = "normal thyroid function"
        for tshVal in tshList:
            if tshVal < 1.0:
                diagnosis = "hyperthyroidism"
            elif tshVal > 4.0:
                diagnosis = "hypothyroidism"
        person["Diagnosis"] = diagnosis
    return personDict


def outputToJSON(personDict, jsonDir):
    import json
    makeDirectory(jsonDir)
    for person in personDict:
        firstName = person["First Name"]
        lastName = person["Last Name"]
        fileName = firstName + "-" + lastName + ".json"
        outFile = open(fileName, "w")
        json.dump(person, outFile)
        outFile.close


def makeDirectory(jsonDir):
    import os
    if os.path.isdir(jsonDir) is False:
        os.mkdir(jsonDir)
    os.chdir(jsonDir)

if __name__ == "__main__":
    main()
