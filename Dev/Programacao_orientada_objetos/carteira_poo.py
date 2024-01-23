from time import sleep
from getpass import getpass
import json


class molde():

    def __init__(self):
        self.gerenciamento_Usuarios = {'id_Usuario': [], 'usuario_Senha': []}

        '''Futuramente pensarei em uma estrutura de dados que junte id_Usuario e usuario_Senha'''

    def gravar_Dados(self):
        with open('Agrupamento_dados.json', 'w') as arquivos:
            json.dump(self.gerenciamento_Usuarios, arquivos)

    def carregar_Dados(self):
        try:
            with open('Agrupamento_dados.json', 'r') as arquivos:
                self.gerenciamento_Usuarios = json.load(arquivos)
        except FileNotFoundError:
            pass

    def login_Usuario(self):
        verificador_Usuario = str(input('Por favor digite o nome de seu usuário: '))
        self.carregar_Dados()
        print(self.gerenciamento_Usuarios)
        if verificador_Usuario in self.gerenciamento_Usuarios['id_Usuario']:
            verificar_Senha = getpass(prompt='Por favor confirme a sua senha: ')
            if verificar_Senha in self.gerenciamento_Usuarios['usuario_Senha']:
                print('teste')
        elif verificador_Usuario not in self.gerenciamento_Usuarios['id_Usuario']:
            print('Usuario não encontrado!')

    def novo_Usuario(self):
        print('Certo, a partir de agora iremos criar a sua conta!')
        sleep(2)
        self.criador_Usuario = str(input('Por favor defina o nome do seu usuario: '))
        self.criador_senha = getpass('Senha: ')
        self.gerenciamento_Usuarios['id_Usuario'].append(self.criador_Usuario)
        self.gerenciamento_Usuarios['usuario_Senha'].append(self.criador_senha)
        self.gravar_Dados()



    def inicio(self):
        print('Olá, seja bem-vindo(a)!')
        verificador_Usuario = str(input('Já possui uma conta? [S/N] ')).strip().upper()
        '''Incluir um contador para definir limite de tentativas'''
        if verificador_Usuario[0] in 'S':
            self.login_Usuario()
        elif verificador_Usuario[0] in 'N':
            self.novo_Usuario()


Iniciador = molde()

Iniciador.inicio()
