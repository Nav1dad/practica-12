def invertir_cadena(cadena):

    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena(cadena_original)
print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {cadena_invertida}")
