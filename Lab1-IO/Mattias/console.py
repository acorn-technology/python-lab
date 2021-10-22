from math import pi

def read_int(promt):
    try:
        return int(input(promt))
    except ValueError:
        print("Invalid input, try again")
        return read_int(promt)


def console():
    decimals = read_int("Enter wanted number of decimals: ")
    print('Pi has the value {{:.{}f}}'.format(decimals).format(pi))

if __name__ == "__main__":
    console()