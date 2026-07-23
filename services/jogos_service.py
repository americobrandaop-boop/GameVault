"""
jogos_service.py

Responsável pelas operações relacionadas aos jogos.
"""
def gerar_id(jogos):
    '''
    Gera um novo ID para o jogo.
    '''
    
    if len(jogos) == 0:
        return 1
    
    maior_id = max(jogo["id"]for jogo in jogos)
    
    return maior_id + 1

def cadastrar_jogo(jogos):
    """
    Cadastra um novo jogo.
    """

    jogo = {}

    print("\n===== CADASTRO DE JOGO =====")

    jogo["id"] = gerar_id(jogos)

    jogo["nome"] = input("Nome: ")
    jogo["genero"] = input("Gênero: ")
    jogo["plataforma"] = input("Plataforma: ")
    jogo["preco"] = float(input("Preço: R$ "))
    jogo["nota"] = float(input("Nota (0 a 10): "))

    jogos.append(jogo)

    print("\nJogo cadastrado com sucesso!\n")

    print("TESTE - JOGO DENTRO DA FUNÇÃO:")
    print(jogos)


def listar_jogos(jogos):
    """
    Exibe todos os jogos cadastrados.
    """

    if len(jogos) == 0:
        print("\nNenhum jogo cadastrado.\n")
        return

    print("\n========== JOGOS CADASTRADOS ==========\n")

    for jogo in jogos:
        
        print(f"ID.............:{jogo['id']}")
        print(f"Nome........: {jogo['nome']}")
        print(f"Gênero......: {jogo['genero']}")
        print(f"Plataforma..: {jogo['plataforma']}")
        print(f"Preço.......: R$ {jogo['preco']:.2f}")
        print(f"Nota........: {jogo['nota']}")
        print("-" * 40)

def buscar_jogo(jogos):
    """
    Busca um jogo pelo nome.
    """

    if len(jogos) == 0:
        print("\nNenhum jogo cadastrado.\n")
        return


    pesquisa = input("\nDigite o nome do jogo: ").lower()


    encontrado = False


    for jogo in jogos:

        if pesquisa in jogo["nome"].lower():

            print("\n========== JOGO ENCONTRADO ==========\n")

            print(f"ID.............:{jogo['id']}")
            print(f"Nome........: {jogo['nome']}")
            print(f"Gênero......: {jogo['genero']}")
            print(f"Plataforma..: {jogo['plataforma']}")
            print(f"Preço.......: R$ {jogo['preco']:.2f}")
            print(f"Nota........: {jogo['nota']}")

            print("-" * 40)

            encontrado = True


    if encontrado == False:

        print("\nNenhum jogo encontrado.\n")

def editar_jogo(jogos):
    """
    Edita um jogo pelo ID.
    """

    if len(jogos) == 0:
        print("\nNenhum jogo cadastrado.\n")
        return


    try:
        id_jogo = int(input("\nDigite o ID do jogo: "))

    except ValueError:
        print("\nDigite apenas números!\n")
        return


    for jogo in jogos:

        if jogo["id"] == id_jogo:

            print("\n========== EDITAR JOGO ==========\n")

            print("Deixe vazio para manter o valor atual.\n")


            nome = input(f"Nome ({jogo['nome']}): ")

            genero = input(f"Gênero ({jogo['genero']}): ")

            plataforma = input(f"Plataforma ({jogo['plataforma']}): ")


            preco = input(f"Preço ({jogo['preco']}): ")

            nota = input(f"Nota ({jogo['nota']}): ")



            if nome:
                jogo["nome"] = nome


            if genero:
                jogo["genero"] = genero


            if plataforma:
                jogo["plataforma"] = plataforma


            if preco:
                jogo["preco"] = float(preco)


            if nota:
                jogo["nota"] = float(nota)



            print("\nJogo atualizado com sucesso!\n")

            return


    print("\nJogo não encontrado.\n")


def excluir_jogo(jogos):
    """
    Exclui um jogo pelo ID.
    """

    if len(jogos) == 0:
        print("\nNenhum jogo cadastrado.\n")
        return


    try:
        id_jogo = int(input("\nDigite o ID do jogo: "))

    except ValueError:
        print("\nDigite apenas números!\n")
        return


    for jogo in jogos:

        if jogo["id"] == id_jogo:

            print("\nJogo encontrado:")
            print(f"Nome: {jogo['nome']}")

            confirmar = input(
                "Deseja excluir? (s/n): "
            )


            if confirmar.lower() == "s":

                jogos.remove(jogo)

                print("\nJogo excluído com sucesso!\n")

            else:

                print("\nExclusão cancelada.\n")


            return


    print("\nJogo não encontrado.\n")

def estatisticas(jogos):
    """
    Exibe estatísticas dos jogos cadastrados.
    """

    print("\n========== ESTATÍSTICAS ==========\n")

    quantidade = len(jogos)

    if quantidade == 0:
        print("Nenhum jogo cadastrado.\n")
        return

    print(f"Quantidade de jogos: {quantidade}")

    # Preço médio
    soma = 0

    for jogo in jogos:
        soma += jogo["preco"]

    media = soma / quantidade

    print(f"Preço médio: R$ {media:.2f}")

    # Valor total da biblioteca
    total = soma

    print(f"Valor total da biblioteca: R$ {total:.2f}")

    # Jogo mais caro
    jogo_mais_caro = jogos[0]

    for jogo in jogos:

        if jogo["preco"] > jogo_mais_caro["preco"]:
            jogo_mais_caro = jogo

    print(f"\nJogo mais caro: {jogo_mais_caro['nome']}")
    print(f"Preço: R$ {jogo_mais_caro['preco']:.2f}")

    # Melhor avaliado
    jogo_melhor_nota = jogos[0]

    for jogo in jogos:

        if jogo["nota"] > jogo_melhor_nota["nota"]:
            jogo_melhor_nota = jogo

    print(f"\nMelhor avaliado: {jogo_melhor_nota['nome']}")
    print(f"Nota: {jogo_melhor_nota['nota']}")








        

