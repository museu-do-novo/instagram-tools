import instaloader
import os
import time

def realizar_login(L, usuario, senha):
    """Realiza o login e salva a sessão, caso ainda não exista."""
    if os.path.exists(f"{usuario}.session"):
        try:
            L.load_session_from_file(usuario)
            print(f"Login realizado com sessão salva para {usuario}.")
            return True
        except Exception as e:
            print(f"Erro ao carregar sessão salva: {e}")
    
    try:
        L.login(usuario, senha)
        if input("Salvar sessão para futuros logins? (s/n): ").lower() == 's':
            L.save_session_to_file()
            print("Sessão salva com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao fazer login: {e}")
    return False

def carregar_perfil(L, usuario_alvo):
    """Carrega o perfil do usuário alvo para verificar stories."""
    try:
        perfil = instaloader.Profile.from_username(L.context, usuario_alvo)
        print(f"Perfil {usuario_alvo} carregado com sucesso.")
        return perfil
    except Exception as e:
        print(f"Erro ao carregar o perfil {usuario_alvo}: {e}")
        return None

def baixar_stories(perfil, L, usuario_alvo):
    """Baixa os stories públicos do usuário alvo."""
    if perfil.has_public_story:
        print(f"Baixando stories de {usuario_alvo}...")
        try:
            stories = L.get_stories(userids=[perfil.userid])
            for story in stories:
                for item in story.get_items():
                    L.download_storyitem(item, usuario_alvo)
            print(f"Stories de {usuario_alvo} baixados com sucesso!")
        except Exception as e:
            print(f"Erro ao baixar stories: {e}")
    else:
        print(f"{usuario_alvo} não tem stories públicos no momento.")

def iniciar_download_stories():
    os.system("clear")

    # Dados de login
    seu_usuario = input("Digite seu nome de usuário do Instagram: ")
    sua_senha = input("Digite sua senha do Instagram: ")
    usuario_alvo = input("Digite o nome do perfil alvo para baixar stories: ")

    # Inicializa o Instaloader
    L = instaloader.Instaloader()

    if not realizar_login(L, seu_usuario, sua_senha):
        print("Falha no login. Verifique suas credenciais.")
        return

    perfil = carregar_perfil(L, usuario_alvo)
    if perfil is None:
        return

    baixar_stories(perfil, L, usuario_alvo)

# Executa o programa principal
iniciar_download_stories()
