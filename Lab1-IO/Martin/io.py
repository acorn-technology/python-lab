from math import pi

while True:
    print("Enter the number of decimals: ", end='')
    try:
        dec = int(input())
        assert dec >= 0
    except Exception as e:
        print("Supply a positive integer")
        continue
    format_string = f"%.{dec}f"
    print(f"Pi has the value {format_string}" % pi)
    break