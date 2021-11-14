b_name = __name__

if __name__ == '__main__':
    from bar.c import c_name
    
    print(f'b: {b_name}')
    print(f'c: {c_name}')