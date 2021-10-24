import sys

class File:
    name = ''
    numberOfLines = 10

    def __init__(self, name):
        self.name = name

def getFilesFromArg(argv):
    files = []
    currentFileIndex = -1
    for argIndex, arg in enumerate(argv[1:]):
        if(currentFileIndex >= 0 and arg.startswith('-')):
            f = files[currentFileIndex]
            f.numberOfLines = int(arg[1:])
        else:
            files.append(File(arg))
            currentFileIndex += 1
    return files


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
        files = getFilesFromArg(sys.argv)
        for indexFile, file in enumerate(files):
            printFileName(file.name, len(files))
            rows = getTailOfFile(file.name, file.numberOfLines)
            for indexRow, row in enumerate(rows):
                print(formatRow(row))
    except:
        print('Error') 
