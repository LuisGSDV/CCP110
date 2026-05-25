import json
import os
import time
from textwrap import wrap
from colorama import Fore, Style, Back

# Caminhos dos arquivos de dados
PASTA            = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_USUARIOS = os.path.join(PASTA, "usuarios.json")
ARQUIVO_VIDEOS   = os.path.join(PASTA, "videos.json")

# Estilizacao
a  = Fore.BLUE
r  = Style.RESET_ALL
s  = Style.BRIGHT
bw = Back.WHITE
ITENS_POR_PAGINA = 3

# Guarda o usuario que esta logado (None = ninguem logado)
usuario_logado = None


# Funcoes de tela
# ----------------------

def trunc(texto, tamanho=60):
    margem = " "
    linhas = wrap(texto, width=tamanho)
    if len(linhas) == 0:
        print()
        return
    for linha_txt in linhas:
        print(margem + linha_txt)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def linha():
    print(" " + "-" * 60)

def cabecalho(titulo):
    limpar_tela()
    linha()
    trunc(bw + a + "  FEItv  " + r + " | " + titulo)
    linha()
    print()

def pausar():
    input(" Pressione Enter para continuar...")

def ler_numero(mensagem="\n Opção: "):
    entrada = input(mensagem)
    if entrada.isdigit():
        return int(entrada)
    return -1


# Funcoes de arquivo
# -------------------------

def carregar_arquivo(caminho):
    if not os.path.exists(caminho):
        return []
    arquivo = open(caminho, "r", encoding="utf-8")
    try:
        conteudo = json.load(arquivo)
    except json.JSONDecodeError:
        conteudo = []
    arquivo.close()
    return conteudo

def salvar_arquivo(caminho, dados):
    arquivo = open(caminho, "w", encoding="utf-8")
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()


# Salvar alteracoes do usuario logado
# -------------------------------------

def salvar_usuario_logado():
    usuarios = carregar_arquivo(ARQUIVO_USUARIOS)
    for i in range(len(usuarios)):
        if usuarios[i]["email"] == usuario_logado["email"]:
            usuarios[i] = usuario_logado
    salvar_arquivo(ARQUIVO_USUARIOS, usuarios)



# Mostrar informacoes de um video
# ---------------------------------

def mostrar_video(video, numero=None):
    total_curtidas = len(video["curtidas"])

    if usuario_logado["email"] in video["curtidas"]:
        cor = Fore.GREEN
        txt = " (curtido)"
    else:
        cor = Fore.RED
        txt = " (nao curtido)"

    if numero != None:
        trunc(a + "[" + str(numero) + "] " + video["titulo"] + r)
    else:
        trunc(a + "Titulo   : " + r + video["titulo"])

    trunc(a + "Curso    : " + r + video["curso"])
    trunc(a + "Autor    : " + r + video["autor"])
    trunc(a + "Descricao: " + r + video["descricao"])
    trunc(a + "Curtidas : " + r + str(total_curtidas) + cor + txt + r)
    print()
    linha()
    print()


# Paginacao para listar todos os videos
# --------------------------------------

def paginacao(lista, pagina=1):
    limpar_tela()
    cabecalho("Todos os Videos")

    inicio = (pagina - 1) * ITENS_POR_PAGINA
    fim    = inicio + ITENS_POR_PAGINA

    itens_pagina = lista[inicio:fim]

    for item in itens_pagina:
        if item["tipo"] == "curso":
            trunc("Curso: " + item["nome"])
            linha()
        elif item["tipo"] == "video":
            mostrar_video(item["dados"])

    total = (len(lista) - 1) // ITENS_POR_PAGINA + 1

    print()
    trunc("[0] Voltar")

    if pagina > 1:
        trunc("[1] Anterior")

    if pagina < total:
        trunc("[2] Proxima")

    trunc("Pagina " + str(pagina) + "/" + str(total))

    op = ler_numero()

    if op == 1 and pagina > 1:
        paginacao(lista, pagina - 1)
    elif op == 2 and pagina < total:
        paginacao(lista, pagina + 1)


# Login e cadastro
# -----------------

def tela_login():
    global usuario_logado

    cabecalho("Login")
    email = input(" E-mail: ")
    senha = input(" Senha : ")
    print()

    usuarios = carregar_arquivo(ARQUIVO_USUARIOS)

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            usuario_logado = usuario
            trunc("Login realizado com sucesso! Bem-vindo(a), " + usuario["nome"] + "!")
            time.sleep(1.5)
            return True

    trunc("E-mail ou senha incorretos. Tente novamente.")
    pausar()
    return False

def tela_cadastro():
    cabecalho("Cadastro de Usuario")

    nome  = input(" Nome  : ")
    email = input(" E-mail: ")
    senha = input(" Senha : ")

    if nome == "" or email == "" or senha == "":
        trunc("Preencha todos os campos.")
        pausar()
        return

    usuarios = carregar_arquivo(ARQUIVO_USUARIOS)

    for usuario in usuarios:
        if usuario["email"] == email:
            trunc("Ja existe um usuario com esse e-mail.")
            pausar()
            return

    novo_usuario = {
        "nome"     : nome,
        "email"    : email,
        "senha"    : senha,
        "favoritos": []
    }

    usuarios.append(novo_usuario)
    salvar_arquivo(ARQUIVO_USUARIOS, usuarios)

    trunc("Cadastro realizado com sucesso! Faca o login para entrar.")
    pausar()


# Busca de videos
# -----------------------

def tela_buscar():
    cabecalho("Buscar Video")

    termo = input(" Digite o nome do video (ou parte): ").lower()

    videos = carregar_arquivo(ARQUIVO_VIDEOS)

    resultados = []
    for video in videos:
        if termo in video["titulo"].lower():
            resultados.append(video)

    if len(resultados) == 0:
        trunc("Nenhum video encontrado.")
        pausar()
        return

    trunc(a + str(len(resultados)) + r + " resultado(s) encontrado(s):")
    print()

    for i in range(len(resultados)):
        mostrar_video(resultados[i], i + 1)

    pausar()


# Curtir e descurtir
# ---------------------

def tela_curtir():
    cabecalho("Curtir / Descurtir Video")

    termo = input(" Busque o video pelo nome: ").lower()

    videos = carregar_arquivo(ARQUIVO_VIDEOS)

    # Guarda o indice real de cada video na lista original
    resultados = []
    for i in range(len(videos)):
        if termo in videos[i]["titulo"].lower():
            resultados.append(i)

    if len(resultados) == 0:
        trunc("Nenhum video encontrado.")
        pausar()
        return

    for j in range(len(resultados)):
        mostrar_video(videos[resultados[j]], j + 1)

    escolha = ler_numero(" Escolha o numero do video (0 para cancelar): ")

    if escolha == 0 or escolha < 1 or escolha > len(resultados):
        return

    indice_real = resultados[escolha - 1]
    video = videos[indice_real]
    email = usuario_logado["email"]

    if email in video["curtidas"]:
        video["curtidas"].remove(email)
        trunc("Curtida removida de '" + video["titulo"] + "'.")
    else:
        video["curtidas"].append(email)
        trunc("Voce curtiu '" + video["titulo"] + "'!")

    videos[indice_real] = video
    salvar_arquivo(ARQUIVO_VIDEOS, videos)
    pausar()


# Favoritos
# ─-------------------

def tela_favoritos():
    while True:
        cabecalho("Favoritos")

        favoritos = usuario_logado["favoritos"]

        if len(favoritos) == 0:
            trunc("Voce ainda nao tem listas de reproducao.")
            print()
        else:
            for i in range(len(favoritos)):
                lista = favoritos[i]
                trunc("[" + str(i + 1) + "] " + lista["nome"] + "  (" + str(len(lista["videos"])) + " video(s))")
            print()

        linha()
        trunc("1. Criar lista")
        trunc("2. Editar nome da lista")
        trunc("3. Excluir lista")
        trunc("4. Ver e gerenciar videos de uma lista")
        trunc("5. Voltar")
        linha()

        op = ler_numero()

        if op == 1:
            criar_lista()
        elif op == 2:
            editar_lista()
        elif op == 3:
            excluir_lista()
        elif op == 4:
            gerenciar_videos_lista()
        elif op == 5:
            break
        else:
            trunc("Opcao invalida.")
            pausar()

def criar_lista():
    nome = input(" Nome da nova lista: ")
    if nome == "":
        trunc("O nome nao pode ser vazio.")
        pausar()
        return
    usuario_logado["favoritos"].append({"nome": nome, "videos": []})
    salvar_usuario_logado()
    trunc("Lista criada com sucesso!")
    pausar()

def editar_lista():
    favoritos = usuario_logado["favoritos"]

    if len(favoritos) == 0:
        trunc("Voce nao tem listas.")
        pausar()
        return

    for i in range(len(favoritos)):
        trunc("[" + str(i + 1) + "] " + favoritos[i]["nome"])

    idx = ler_numero(" Numero da lista: ") - 1

    if idx < 0 or idx >= len(favoritos):
        trunc("Numero invalido.")
        pausar()
        return

    novo_nome = input(" Novo nome: ")
    if novo_nome == "":
        trunc("O nome nao pode ser vazio.")
        pausar()
        return

    usuario_logado["favoritos"][idx]["nome"] = novo_nome
    salvar_usuario_logado()
    trunc("Nome atualizado com sucesso!")
    pausar()

def excluir_lista():
    favoritos = usuario_logado["favoritos"]

    if len(favoritos) == 0:
        trunc("Voce nao tem listas.")
        pausar()
        return

    for i in range(len(favoritos)):
        trunc("[" + str(i + 1) + "] " + favoritos[i]["nome"])

    idx = ler_numero(" Numero da lista para excluir (0 para cancelar): ") - 1

    if idx == -1:
        return

    if idx < 0 or idx >= len(favoritos):
        trunc("Numero invalido.")
        pausar()
        return

    confirmacao = input(" Tem certeza que quer excluir '" + favoritos[idx]["nome"] + "'? (s/n): ")
    if confirmacao.lower() == "s":
        usuario_logado["favoritos"].pop(idx)
        salvar_usuario_logado()
        trunc("Lista excluida.")
    pausar()

def gerenciar_videos_lista():
    favoritos = usuario_logado["favoritos"]

    if len(favoritos) == 0:
        trunc("Voce nao tem listas.")
        pausar()
        return

    for i in range(len(favoritos)):
        trunc("[" + str(i + 1) + "] " + favoritos[i]["nome"])

    idx = ler_numero(" Numero da lista: ") - 1

    if idx < 0 or idx >= len(favoritos):
        trunc("Numero invalido.")
        pausar()
        return

    lista = usuario_logado["favoritos"][idx]

    while True:
        cabecalho("Lista: " + lista["nome"])

        if len(lista["videos"]) == 0:
            trunc("(lista vazia)")
            print()
        else:
            for j in range(len(lista["videos"])):
                trunc("[" + str(j + 1) + "] " + lista["videos"][j])
            print()

        linha()
        trunc("1. Adicionar video")
        trunc("2. Remover video")
        trunc("3. Voltar")
        linha()

        op = ler_numero()

        if op == 1:
            adicionar_video_lista(lista)
        elif op == 2:
            remover_video_lista(lista)
        elif op == 3:
            break
        else:
            trunc("Opcao invalida.")
            pausar()

    salvar_usuario_logado()

def adicionar_video_lista(lista):
    termo = input(" Busque o video pelo nome: ").lower()
    videos = carregar_arquivo(ARQUIVO_VIDEOS)

    resultados = []
    for video in videos:
        if termo in video["titulo"].lower():
            resultados.append(video)

    if len(resultados) == 0:
        trunc("Nenhum video encontrado.")
        pausar()
        return

    for i in range(len(resultados)):
        trunc("[" + str(i + 1) + "] " + resultados[i]["titulo"] + " - " + resultados[i]["curso"])

    idx = ler_numero(" Numero do video (0 para cancelar): ") - 1

    if idx == -1:
        return

    if idx < 0 or idx >= len(resultados):
        trunc("Numero invalido.")
        pausar()
        return

    titulo = resultados[idx]["titulo"]

    if titulo in lista["videos"]:
        trunc("Esse video ja esta na lista.")
    else:
        lista["videos"].append(titulo)
        trunc("'" + titulo + "' adicionado a lista!")
    pausar()

def remover_video_lista(lista):
    if len(lista["videos"]) == 0:
        trunc("A lista esta vazia.")
        pausar()
        return

    for i in range(len(lista["videos"])):
        trunc("[" + str(i + 1) + "] " + lista["videos"][i])

    idx = ler_numero(" Numero do video para remover (0 para cancelar): ") - 1

    if idx == -1:
        return

    if idx < 0 or idx >= len(lista["videos"]):
        trunc("Numero invalido.")
        pausar()
        return

    removido = lista["videos"].pop(idx)
    trunc("'" + removido + "' removido da lista.")
    pausar()


# Listar todos os videos
# -------------------------

def tela_listar_todos():
    videos = carregar_arquivo(ARQUIVO_VIDEOS)

    if len(videos) == 0:
        cabecalho("Todos os Videos")
        trunc("Nenhum video cadastrado.")
        pausar()
        return

    cursos = {}
    for video in videos:
        curso = video["curso"]
        if curso not in cursos:
            cursos[curso] = []
        cursos[curso].append(video)

    itens = []
    for curso in cursos:
        itens.append({"tipo": "curso", "nome": curso})
        for video in cursos[curso]:
            itens.append({"tipo": "video", "dados": video})

    paginacao(itens)


# Menu principal (usuario logado)
# --------------------------------

def menu_principal():
    global usuario_logado

    while True:
        cabecalho("Ola, " + usuario_logado["nome"] + "!")
        trunc("1. Buscar video")
        trunc("2. Curtir / Descurtir video")
        trunc("3. Favoritos")
        trunc("4. Listar todos os videos")
        trunc("5. Sair da conta")
        linha()

        op = ler_numero()

        if op == 1:
            tela_buscar()
        elif op == 2:
            tela_curtir()
        elif op == 3:
            tela_favoritos()
        elif op == 4:
            tela_listar_todos()
        elif op == 5:
            usuario_logado = None
            break
        else:
            trunc("Opcao invalida.")
            pausar()


# Menu inicial (sem login)
# -------------------------

def menu_inicial():
    os.system("mode con: cols=64 lines=45")
    while True:
        cabecalho("Bem-vindo!")
        trunc("1. Login")
        trunc("2. Cadastro")
        trunc("3. Sair")
        print()
        linha()

        op = ler_numero()

        if op == 1:
            logou = tela_login()
            if logou:
                menu_principal()
        elif op == 2:
            tela_cadastro()
        elif op == 3:
            limpar_tela()
            trunc("Ate logo!")
            break
        else:
            trunc("Opcao invalida.")
            pausar()


# Inicio do programa
# ---------------------

menu_inicial()