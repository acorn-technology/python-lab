b_name = __name__

if __name__ == '__main__':
    from bar import c
    
    print(f'b: {b_name}')
    print(f'c: {c.c_name}')