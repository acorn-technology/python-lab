import math

def output_pi(decimals):
    try:
        if decimals > 0:
            return round(math.pi - (math.pow(10, -(decimals+1))*5), decimals)
        else:
            return "Input must be larger than 0"
    except TypeError:
        return "Input must be number"

def main():
    print(output_pi(2))
    
if __name__ == "__main__":
    main()
 