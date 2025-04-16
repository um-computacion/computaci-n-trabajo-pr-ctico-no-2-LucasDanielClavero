def is_palindrome(texto):
    texto_limpio = ""
    contador = 0

    while contador < len(texto):
        caracter = texto[contador]
        if caracter not in [" ", ",", ".", ":", ";", "!", "?", "'", "\"", "-", "(", ")", "[", "]", "{", "}", "_"]:
            texto_limpio += caracter.lower()
        contador += 1
        
    return False

