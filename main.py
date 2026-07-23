from pedrolib.menus import menu_principal

from services.jogos_service import (
    cadastrar_jogo,
    listar_jogos,
    buscar_jogo,
    editar_jogo,
    excluir_jogo,
    estatisticas,
    
)

from services.arquivo_service import (
    criar_arquivo,
    carregar_jogos,
    salvar_jogos,
  

)

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

arquivo = os.path.join(BASE_DIR, "data", "jogos.json")


criar_arquivo(arquivo)

jogos = carregar_jogos(arquivo)


while True:

    menu_principal()

    try:
        opcao = int(input("Escolha uma opção: "))

    except ValueError:
        print("\nDigite apenas números!\n")
        continue


    if opcao == 1:

        cadastrar_jogo(jogos)

        salvar_jogos(arquivo, jogos)


    elif opcao == 2:

        listar_jogos(jogos)


    elif opcao == 3:

        buscar_jogo(jogos)


    elif opcao == 4:

        editar_jogo(jogos)
        salvar_jogos(arquivo,jogos)


    elif opcao == 5:

        excluir_jogo(jogos)
        salvar_jogos(arquivo,jogos)


    elif opcao == 6:

        estatisticas(jogos)
        


    elif opcao == 0:

        print("\nObrigado por utilizar o GameVault!")
        break


    else:

        print("\nOpção inválida!\n")