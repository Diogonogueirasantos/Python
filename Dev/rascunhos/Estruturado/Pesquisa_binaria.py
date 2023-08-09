from random import choice

id_Usuario = []

for cadastros in range(0, 100):
    id_Usuario.append(cadastros)

marcador_usuario = choice(id_Usuario)
marcador_alto = len(id_Usuario)
marcador_baixo = 0

print(f'Usuario selecionado {marcador_usuario} marcador alto da lista {marcador_alto}')

if marcador_usuario == marcador_alto:
    print(f'Usuario encontrado! o usuario selecionado é {marcador_usuario}')
elif marcador_usuario < marcador_alto:
    marcador_baixo = marcador_alto - marcador_usuario
    print(f'Usuarios restantes {marcador_baixo}')

    usuario_Encontrado = marcador_alto - marcador_baixo

    print(f'O usuario selecionado é {usuario_Encontrado}')