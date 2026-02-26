def is_isogram(string):
    loweredcase_string = string.lower()
    verification = 0
    string_clear = ""
    
    for letter in loweredcase_string:
        if letter.isalpha():
            string_clear += letter 
        verification += string_clear.count(letter)
        
    if verification == len(string_clear):
        return True
    else:
        return False
        
        
        
