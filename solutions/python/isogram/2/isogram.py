def is_isogram(string):
    clear_string = set()
    letters_only = ""
    loweredcased_string = string.lower()
    for letter in loweredcased_string:
        if letter.isalpha() == True:
            letters_only += letter
            clear_string.add(letter)
    return len(clear_string) == len(letters_only)
    
        
        
        
        
