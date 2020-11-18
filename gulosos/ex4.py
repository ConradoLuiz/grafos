modulos = [[1, 5], [1, 7], [1, 3], [3, 6], [4, 12], [5, 12], [2, 8], [
    4, 9], [7, 11], [15, 19], [8, 12], [14, 17], [15, 18], [18, 23], [23, 27]]

# ordenando pelo menor fim
modulos = sorted(modulos, key=lambda mod: mod[1])
n_pessoas = 0
print(modulos)


def alocar_pessoa(modulos):
    print('Pessoa -----------------------')
    modulos_pessoa = []
    ultimo = modulos[0][1]
    modulos_pessoa.append(modulos[0])
    modulos = modulos[1:]
    for i, modulo in enumerate(modulos):
        if modulo[0] >= ultimo:
            ultimo = modulo[1]
            modulos.pop(i)
            modulos_pessoa.append(modulo)
    print(modulos_pessoa)
    return modulos


while len(modulos) > 0:
    modulos = alocar_pessoa(modulos)
    n_pessoas += 1

# modulos = alocar_pessoa(modulos)
print(modulos)
print(n_pessoas)
