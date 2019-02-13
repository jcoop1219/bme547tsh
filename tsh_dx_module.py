def main:
    dataFile = open("test_data.txt", "r")

def readFile:
    dataFile = open("test_data.txt", "r")
    lineCount = 0
    for line in dataFile:
        if line.startswith("END"):
            break
        lineCount += 1
        if lineCount % 4 == 1:
            firstName = line.rstrip("\n").split(" ")[0]
            lastName = line.rstrip("\n").split(" ")[1]


if __name__ == "__main__":
    main()
