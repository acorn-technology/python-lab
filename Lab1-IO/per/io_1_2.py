import math

if __name__ == '__main__':
    n_decimals = int(input("Enter wanted number of decimals: "))
    print("{{:.{}f}}".format(n_decimals).format(math.pi))
