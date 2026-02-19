def square(number):
    if (number < 1) or (number > 64):
        raise ValueError("square must be between 1 and 64")
    potencia = number-1
    number = 2**potencia
    
        
    return number
        
    


def total():
    result = 0
    for n in range(1,65):
        potencia = n-1
        result += 2**potencia
    return result
        
