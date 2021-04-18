def iniciais(frase):
        arr_palavras = frase.split(' ')
        arr_inicias = []
        for palavra in arr_palavras:
            arr_inicias.append(palavra[0])
        print(arr_inicias)