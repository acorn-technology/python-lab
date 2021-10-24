import math

def validateDecimal(dec):
    int(dec) > 0

def formatNumber(number, dec):
    return f'{number:.{dec}f}'

if __name__ == '__main__':
    dec = input('Enter wanted number of decimals:')
    try:
        validateDecimal(dec)
        print(formatNumber(math.pi, dec))
    except:
        print('Not valid input') 


