def is_pangram(sentence):
    palabra = set()
    for i in sentence:
        lowercased_i = i.lower()
        if lowercased_i.isalpha():
            palabra.add(lowercased_i)
    
    if len(palabra) >= 26:
        return True
    else:
        return False