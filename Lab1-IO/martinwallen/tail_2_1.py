import sys

def getFileFromArg():
    return sys.argv[1]

def getIndex(lines, numberOfLines):
    lenght = len(lines)
    if(lenght > numberOfLines):
        return lenght - numberOfLines
    else:
        return 0

def getTailOfFile(file, numberOfLines):
    file = open(file, 'r')
    lines = file.readlines()
    index = getIndex(lines, numberOfLines)
    return lines[index:]

def formatRow(row):
    return row[1].replace('\n','')

if __name__ == '__main__':
    try:
        file = getFileFromArg()
        rows = getTailOfFile(file, 10)
        for row in enumerate(rows):
            print(formatRow(row))
    except:
        print('Error') 
