def convert(number):
    Fizz = ""
    if number % 3 == 0:
        Fizz += "Pling"
        
    if number % 5 == 0:
        Fizz += "Plang"
        
    if number % 7 == 0:
        Fizz += "Plong"
        
    if Fizz == "":
        return str(number)
    return Fizz
