def score(x, y):
    outside = 0
    outer = 1
    middle = 5
    inner = 10
    if (x*x + y*y) > 100:
        return outside
    elif (x*x + y*y) <= 1:
        return inner
    elif (x*x + y*y) <= 25:
        return middle
    else:
        return outer
        
    