import getpass
from typing import List

Usuario = List[str]
senha = List[int]

print('Olá seja bem-vindo a sua carteira virutal!')

verificacao_usuario = str(input('Possui registro em nosso sistema? [S/N]')).strip().upper()

if verificacao_usuario in 'S':
    pesquisa_usuario = str(input('Por favor digite o seu nome de usuário: '))
    if pesquisa_usuario in Usuario:
        print(f'Seja muito bem vindo(a)! {pesquisa_usuario in UsuarioS}')
    elif pesquisa_usuario not in Usuario[:]:
        print('Usuário não encontrado!')
