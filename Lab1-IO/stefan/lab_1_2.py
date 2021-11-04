import math
from lab_1_1 import output_pi

def input_pi_decimals():
    decimals = int(input("Enter wanted number of decimals: "))
    print("Pi has the value: ", output_pi(decimals))

def main():
    input_pi_decimals()
    
if __name__ == "__main__":
    main()
 