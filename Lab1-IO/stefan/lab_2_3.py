
import sys
from lab_2_2 import multi_tail

class NotPositiveIntegerException(Exception):
    """Raised when input string cant be converted to positive integer"""
    pass

def getPositiveInteger(str):
  try:
    result = int(str)
    if result < 0:
        raise NotPositiveIntegerException
    return result
  except ValueError:
    raise NotPositiveIntegerException

def main(argv):
        multi_tail(argv[1:], getPositiveInteger(argv[0]))
    
if __name__ == "__main__":
    main(sys.argv[1:])
