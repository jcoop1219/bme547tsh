def main():
    fileName = "test_data.txt"
    personDict = createDict(fileName)


def createDict(fileName):
    dataFile = open(fileName, "r")
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
            personDict[personNum]["First Name"] = firstName
            personDict[personNum]["Last Name"] = lastName
        elif lineType == 2:  # age line
            age = int(line.rstrip("\n"))
            personDict[personNum]["Age"] = age
        elif lineType == 3:  # gender line
            gender = line.rstrip("\n")
            personDict[personNum]["Gender"] = gender
        else:  # TSH line
            tshList = line.lstrip("TSH,").rstrip("\n").split(",")
            for idx, item in enumerate(tshList):
                tshList[idx] = float(item)
            personDict[personNum]["TSH"] = tshList
    return personDict

if __name__ == "__main__":
    main()
