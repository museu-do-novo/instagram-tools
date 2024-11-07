import instaloader
import os
from colorama import Fore, Style, init

# Inicializa o colorama para cores no terminal
init(autoreset=True)

def realizar_login(L):
    """Tenta carregar a sessão salva; se não existir, solicita nome de usuário e senha, faz login e salva a sessão."""
    nome_de_usuario = input("Digite seu nome de usuário: ")

    try:
        # Tenta carregar a sessão salva com o nome do usuário
        L.load_session_from_file(nome_de_usuario)
        print(Fore.GREEN + f"Login realizado com a sessão salva para {nome_de_usuario}.")
    except FileNotFoundError:
        # Caso não haja uma sessão salva, pede a senha, faz login e salva
        senha = input("Digite sua senha: ")
        print(Fore.RED + "Sessão não encontrada, realizando login manual...")
        L.login(nome_de_usuario, senha)
        if input(Fore.CYAN + "Salvar sessão para futuros logins? (s/n): ").lower() == 's':
            L.save_session_to_file()
            print(Fore.GREEN + "Sessão salva com sucesso.")

def carregar_perfil(L, usuario_alvo):
    """Carrega o perfil do usuário alvo para verificar stories."""
    try:
        perfil = instaloader.Profile.from_username(L.context, usuario_alvo)
        print(Fore.GREEN + f"Perfil {usuario_alvo} carregado com sucesso.")
        return perfil
    except Exception as e:
        print(Fore.RED + f"Erro ao carregar o perfil {usuario_alvo}: {e}")
        return None

def baixar_stories(perfil, L, usuario_alvo):
    """Baixa os stories públicos do usuário alvo."""
    if perfil.has_public_story:
        print(Fore.CYAN + f"Baixando stories de {usuario_alvo}...")
        try:
            stories = L.get_stories(userids=[perfil.userid])
            for story in stories:
                for item in story.get_items():
                    L.download_storyitem(item, usuario_alvo)
            print(Fore.GREEN + f"Stories de {usuario_alvo} baixados com sucesso!")
        except Exception as e:
            print(Fore.RED + f"Erro ao baixar stories: {e}")
    else:
        print(Fore.YELLOW + f"{usuario_alvo} não tem stories públicos no momento.")

def iniciar_download_stories():
    os.system("clear")
    L = instaloader.Instaloader()

    # Realiza login
    realizar_login(L)

    # Definir o usuário alvo e iniciar o download dos stories
    usuario_alvo = input("Digite o nome do perfil alvo para baixar stories: ")
    perfil = carregar_perfil(L, usuario_alvo)
    if perfil:
        baixar_stories(perfil, L, usuario_alvo)

# Executa o programa principal
iniciar_download_stories()
