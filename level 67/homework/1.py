def digital_root(n):
    
    c = 0
    for i in str(n):
        c += int(i)
    if len(str(c)) == 1:
        return c
    x = 0
    for i in str(c):
        x += int(i)
    if len(str(x)) == 1:
        return x
    y = 0
    for i in str(x):
        y += int(i)
    return y