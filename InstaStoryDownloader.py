import instaloader
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Inicializa o colorama para colorir o terminal

def listar_sessoes():
    """Listar todas as sessões salvas no diretório atual."""
    sessoes = [f for f in os.listdir() if f.endswith('.session')]
    if sessoes:
        print(Fore.CYAN + "\nSessões salvas:")
        for idx, sessao in enumerate(sessoes):
            print(f"{Fore.YELLOW}[{idx + 1}] {sessao.replace('.session', '')}")
        return sessoes
    else:
        print(Fore.RED + "Nenhuma sessão salva encontrada.")
        return []

def selecionar_sessao(sessoes):
    """Permite que o usuário escolha uma sessão da lista de sessões salvas."""
    escolha = input(Fore.CYAN + "\nSelecione uma sessão pelo número ou pressione Enter para login manual: ")
    if escolha.isdigit() and 1 <= int(escolha) <= len(sessoes):
        return sessoes[int(escolha) - 1].replace('.session', '')
    return None

def realizar_login(L, usuario, senha):
    """Realiza o login e salva a sessão, caso ainda não exista."""
    if os.path.exists(f"{usuario}.session"):
        try:
            L.load_session_from_file(usuario)
            print(Fore.GREEN + f"Login realizado com sessão salva para {usuario}.")
            return True
        except Exception as e:
            print(Fore.RED + f"Erro ao carregar sessão salva: {e}")

    try:
        L.login(usuario, senha)
        if input(Fore.CYAN + "Salvar sessão para futuros logins? (s/n): ").lower() == 's':
            L.save_session_to_file()
            print(Fore.GREEN + "Sessão salva com sucesso.")
        return True
    except Exception as e:
        print(Fore.RED + f"Erro ao fazer login: {e}")
    return False

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

    # Listar sessões salvas e permitir seleção
    sessoes = listar_sessoes()
    sessao_selecionada = selecionar_sessao(sessoes)

    if sessao_selecionada:
        # Login com sessão salva
        try:
            L.load_session_from_file(sessao_selecionada)
            print(Fore.GREEN + f"Login realizado com a sessão salva para {sessao_selecionada}.")
        except Exception as e:
            print(Fore.RED + f"Erro ao carregar sessão salva {sessao_selecionada}: {e}")
            return
    else:
        # Login manual
        seu_usuario = input("Digite seu nome de usuário do Instagram: ")
        sua_senha = input("Digite sua senha do Instagram: ")

        if not realizar_login(L, seu_usuario, sua_senha):
            print(Fore.RED + "Falha no login. Verifique suas credenciais.")
            return

    # Definir o usuário alvo e iniciar o download dos stories
    usuario_alvo = input("Digite o nome do perfil alvo para baixar stories: ")
    perfil = carregar_perfil(L, usuario_alvo)
    if perfil:
        baixar_stories(perfil, L, usuario_alvo)

# Executa o programa principal
iniciar_download_stories()
