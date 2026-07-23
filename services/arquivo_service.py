'''
arquivo_service.py

Responsavel por salvar e carregar arquivos JSON.
'''

import json
import os


def salvar_jogos(nome_arquivo, jogos):
    """
    Salva a lista de jogos no arquivo JSON.
    """

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        json.dump(
            jogos,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

   

def criar_arquivo(nome_arquivo):
    '''
    Criar um arquivo JSON caso ele não exista.
    '''

    pasta = os.path.dirname(nome_arquivo)

    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)

    if not os.path.exists(nome_arquivo):

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(
                [],
                arquivo,
                ensure_ascii=False,
                indent=4
            )
def carregar_jogos(nome_arquivo):
    '''
    Carregar os jogos do arquivo JSON.
    '''

    
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        jogos = json.load(arquivo)

    return jogos
7
