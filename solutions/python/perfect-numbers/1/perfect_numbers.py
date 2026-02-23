def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    determination = 0
    
    for i in range(1,number):
        if number%i == 0:
            determination += i
            
    if determination == number:
        return "perfect"
    elif determination > number:
        return "abundant"
    else:
        return "deficient"
                    
