inputFile = open("inputFile.txt","r")
for line in inputFile:
    line_splite = line.split()
    if line_splite[1] == "F":
        print(line)
inputFile.close()