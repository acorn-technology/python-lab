
import sys
from lab_2_1 import single_tail

def multi_tail(files, lines):
    for filname in files:
        print("\n==> ", filname, " <==")
        single_tail(filname, lines)    

def main(argv):
    multi_tail(argv, 10)
    
if __name__ == "__main__":
    main(sys.argv[1:])
