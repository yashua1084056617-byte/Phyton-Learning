def encode(message, rails):
    rail= 0
    direction = 1
    #Creando el patron de encode
    if rails == 1:
        return message
    fence = [""] * rails
    for char in message:
        #anadiendo la letra segun rail
        fence[rail] += char
        rail += direction
        #generando limites en rail
        if rail == 0 or rail == rails -1:
            direction *= -1
    #Uniendo todo el mensaje 
    return "".join(fence)
        
    


def decode(encoded_message, rails):
    if rails == 1:
        return encoded_message
        #creando variables que vamos a usar
    counts = [0] * rails
    pattern = []
    start = 0
    rail = 0
    rail_parts = []
    direction = 1
    result = ""
    #Creando el patron de trails que vamos a ocupar (filas)
    for _ in encoded_message:
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails -1:
            direction *= -1
    #Contando las veces que cierta letra pasa por un trail y guardandola en lista
    for r in pattern:
        counts[r] +=1
    #Asignando el rango que abarca sierto trail en las letras del code y separandolas por listas
    for c in counts:
        part = encoded_message[start:start+c]
        rail_parts.append(part)
        start += c
    rail_parts = [list(p) for p in rail_parts]
    #Armando el mensaje final
    for r in pattern:
        result += rail_parts[r].pop(0)
    #Mostrando el resultado
    return result
    
