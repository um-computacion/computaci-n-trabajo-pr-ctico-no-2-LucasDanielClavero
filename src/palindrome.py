def is_palindrome(texto):
    texto_limpio = ""
    contador = 0

    while contador < len(texto):
        caracter = texto[contador]
        if caracter not in [" ", ",", ".", ":", ";", "!", "?", "'", "\"", "-", "(", ")", "[", "]", "{", "}", "_"]:
            texto_limpio += caracter.lower()
        contador += 1

    texto_invertido = texto_limpio[::-1]

    if texto_limpio == texto_invertido:
        return True
    else:
        return False
    
texto_ingresado = str(input("Ingrese una palabra o frase"))

analisar = is_palindrome(texto_ingresado)
if analisar == True:
    print(f"{texto_ingresado} es un palíndromo")
else:
    print(f"{texto_ingresado} no es un palíndromo")

