def main:
    dataFile = open("test_data.txt", "r")

def readFile:
    dataFile = open("test_data.txt", "r")
    lineCount = 0
    for line in dataFile:
        if line.startswith("END"): # if we're at the end of the file, quit the loop
            break
        lineCount += 1
        lineType = lineCount % 4
        if lineType == 1: # name line
            firstName = line.rstrip("\n").split(" ")[0]
            lastName = line.rstrip("\n").split(" ")[1]
        elif lineType == 2: # age line
            age = int(line.rstrip("\n"))
        elif lineType == 3: # gender line
            gender = line.rstrip("\n")


if __name__ == "__main__":
    main()
