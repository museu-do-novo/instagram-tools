import instaloader
import os
import json
from colorama import Fore, Style, init

# Inicializa o colorama para cores no terminal
init(autoreset=True)
os.system("clear")

def carregar_sessao(L):
    """Carregar a sessão salva ou fazer login e salvar uma nova sessão."""
    nome_de_usuario = input("Digite seu nome de usuário: ")
    
    try:
        # Tentar carregar a sessão salva
        L.load_session_from_file(nome_de_usuario)
        print(Fore.GREEN + f"Sessão carregada com sucesso para {nome_de_usuario}.")
    except FileNotFoundError:
        print(Fore.YELLOW + "Sessão não encontrada. Fazendo login...")

        # Solicita a senha somente se a sessão não for encontrada
        senha = input("Digite sua senha: ")
        L.login(nome_de_usuario, senha)
        L.save_session_to_file()
        print(Fore.GREEN + "Sessão salva com sucesso.")

def carregar_perfil(L, usuario_alvo):
    """Carrega o perfil do usuário alvo no Instagram."""
    try:
        perfil = instaloader.Profile.from_username(L.context, usuario_alvo)
        print(Fore.GREEN + f"Perfil {usuario_alvo} carregado com sucesso.")
        return perfil
    except Exception as e:
        print(Fore.RED + f"Erro ao carregar o perfil {usuario_alvo}: {e}")
        return None

def coletar_seguidores(perfil):
    """Coleta a lista de seguidores de um perfil."""
    seguidores = []
    try:
        print(Fore.CYAN + f"Coletando seguidores de {perfil.username}...")
        for follower in perfil.get_followers():
            seguidores.append(follower.username)
        print(Fore.GREEN + f"{len(seguidores)} seguidores coletados.")
    except Exception as e:
        print(Fore.RED + f"Erro ao coletar seguidores: {e}")
    return seguidores

def coletar_seguidos(perfil):
    """Coleta a lista de perfis seguidos por um perfil."""
    seguidos = []
    try:
        print(Fore.CYAN + f"Coletando perfis seguidos por {perfil.username}...")
        for following in perfil.get_followees():
            seguidos.append(following.username)
        print(Fore.GREEN + f"{len(seguidos)} seguidos coletados.")
    except Exception as e:
        print(Fore.RED + f"Erro ao coletar perfis seguidos: {e}")
    return seguidos

def salvar_dados(usuario_alvo, seguidores, seguidos):
    """Salva seguidores e seguidos em um arquivo JSON."""
    dados = {
        "seguidores": seguidores,
        "seguidos": seguidos
    }
    with open(f"{usuario_alvo}_dados.json", 'w') as f:
        json.dump(dados, f, indent=4)
    print(Fore.GREEN + f"Dados de {usuario_alvo} salvos em {usuario_alvo}_dados.json")

def listar_seguidores_e_seguidos():
    L = instaloader.Instaloader()

    # Carregar a sessão ou fazer login
    carregar_sessao(L)

    # Definir o usuário alvo e iniciar o processo de coleta
    usuario_alvo = input("Digite o nome do perfil alvo: ")
    perfil = carregar_perfil(L, usuario_alvo)
    if perfil is None:
        return

    seguidores = coletar_seguidores(perfil)
    seguidos = coletar_seguidos(perfil)
    salvar_dados(usuario_alvo, seguidores, seguidos)

    print(Fore.CYAN + f"\nResumo: {usuario_alvo} possui {len(seguidores)} seguidores e segue {len(seguidos)} perfis.")

# Executa a função principal
listar_seguidores_e_seguidos()
