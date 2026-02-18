def equilateral(sides):
    a,b,c = sides
    if (a==b and b==c and c==b) and (a + b + c > 0):
       return True
    else:
        return False

def isosceles(sides):
    a,b,c = sides
    if len(set(sides)) <= 2 and (a + b >= c and b + c >= a and a + c >= b):
        return True
    else:
        return False

def scalene(sides):
    a,b,c = sides
    if len(set(sides)) >= 3 and (a + b >= c and b + c >= a and a + c >= b):
        return True
    else:
        return False
