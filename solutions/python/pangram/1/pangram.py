def is_pangram(sentence):
    palabra = set()
    for i in sentence:
        i = i.lower()
        if i.isalpha():
            palabra.add(i)
    
    if len(palabra) >= 26:
        return True
    else:
        return False