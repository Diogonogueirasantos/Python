cor = ['Branco', 'Preto', 'Azul']
tamanho = ['M', 'G']

estoque = [(ord(cor, tamanho)) for cores in cor for tamanhos in tamanho ]
print(estoque)