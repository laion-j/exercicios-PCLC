def alfabeto(frase):
    arr_palavras = frase.upper().split(' ')
    arr_alfabeto = []
    for palavra in arr_palavras:
        cont = 0
        while cont < len(palavra):
            letra = palavra[cont]
            if letra not in arr_alfabeto:
                arr_alfabeto.append(letra)
            cont += 1
    print(arr_alfabeto)