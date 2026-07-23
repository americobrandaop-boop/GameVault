"""
menus.py

Biblioteca responsável pela exibição de menus e títulos do sistema.
"""

def linha(tamanho=60):
    """
    Exibe uma linha horizontal.

    Parâmetro:
        tamanho (int): quantidade de caracteres.
    """

    print("=" * tamanho)


def titulo(texto):
    """
    Exibe um título formatado.

    Parâmetro:
        texto (str): texto que será mostrado.
    """

    linha()

    print(texto.center(60))

    linha()


def menu_principal():
    '''
    Exibe o menu principal do Sistema.
    '''
    titulo("GAMEVAULT")

    print("[1] Cadastrar jogo")

    print("[2] Listar jogos")

    print("[3] Buscar jogo")

    print("[4] Editar jogo")

    print("[5] Excluir jogo")

    print("[6] Estatísticas ")

    print("[0] Sair")

    linha()