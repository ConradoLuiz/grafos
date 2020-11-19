

str_numeros = input('Digite o vetor de números separados por espaço:')

vetor = str_numeros.split(' ')
vetor = [float(n) for n in vetor]
media = 0
for n in vetor:
    media += n/len(vetor)

print(media)
print('O algoritmo é O(n) pois é necessário iterar sobre todo o array para saber a média')
