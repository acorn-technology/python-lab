import sys

def getFilesFromArg():
    return sys.argv[1:]

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
    return row.replace('\n','')

def printFileName(file, numberOfFiles):
    if(numberOfFiles > 1):
        print(f'File: {file}')

if __name__ == '__main__':
    try:
        files = getFilesFromArg()
        for indexFile, file in enumerate(files):
            printFileName(file, len(files))
            rows = getTailOfFile(file, 10)
            for indexRow, row in enumerate(rows):
                print(formatRow(row))
    except:
        print('Error') 
