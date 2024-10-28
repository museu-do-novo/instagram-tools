import instaloader
import os
import json
import time

def realizar_login(L, usuario, senha):
    """Realiza o login no Instagram e salva a sessão."""
    if os.path.exists(f"{usuario}.session"):
        try:
            L.load_session_from_file(usuario)
            print(f"Login bem-sucedido com sessão salva para {usuario}.")
            return True
        except Exception as e:
            print(f"Erro ao carregar sessão salva: {e}")
    
    # Tenta login caso não haja sessão ou se o carregamento falhar
    for tentativa in range(3):
        try:
            L.login(usuario, senha)
            if input("Salvar sessão para logins futuros? (s/n): ").lower() == 's':
                L.save_session_to_file()
                print("Sessão salva com sucesso.")
            return True
        except Exception as e:
            print(f"Tentativa {tentativa + 1}/3 - Erro ao fazer login: {e}")
            if tentativa < 2:
                print("Tentando novamente...")
                time.sleep(2)
    return False

def carregar_perfil(L, usuario_alvo):
    """Carrega o perfil do usuário alvo no Instagram."""
    try:
        perfil = instaloader.Profile.from_username(L.context, usuario_alvo)
        print(f"Perfil {usuario_alvo} carregado.")
        return perfil
    except Exception as e:
        print(f"Erro ao carregar o perfil {usuario_alvo}: {e}")
        return None

def coletar_seguidores(perfil):
    """Coleta a lista de seguidores de um perfil."""
    seguidores = []
    try:
        print(f"Coletando seguidores de {perfil.username}...")
        for follower in perfil.get_followers():
            seguidores.append(follower.username)
        print(f"{len(seguidores)} seguidores coletados.")
    except Exception as e:
        print(f"Erro ao coletar seguidores: {e}")
    return seguidores

def coletar_seguidos(perfil):
    """Coleta a lista de perfis seguidos por um perfil."""
    seguidos = []
    try:
        print(f"Coletando perfis seguidos por {perfil.username}...")
        for following in perfil.get_followees():
            seguidos.append(following.username)
        print(f"{len(seguidos)} seguidos coletados.")
    except Exception as e:
        print(f"Erro ao coletar perfis seguidos: {e}")
    return seguidos

def salvar_dados(usuario_alvo, seguidores, seguidos):
    """Salva seguidores e seguidos em um arquivo JSON."""
    dados = {
        "seguidores": seguidores,
        "seguidos": seguidos
    }
    with open(f"{usuario_alvo}_dados.json", 'w') as f:
        json.dump(dados, f, indent=4)
    print(f"Dados de {usuario_alvo} salvos em {usuario_alvo}_dados.json")

def listar_seguidores_e_seguidos():
    L = instaloader.Instaloader()
    usuario = input("Digite seu nome de usuário do Instagram: ")
    senha = input("Digite sua senha do Instagram: ")

    if not realizar_login(L, usuario, senha):
        print("Falha no login após 3 tentativas. Encerrando o programa.")
        return

    usuario_alvo = input("Digite o nome do perfil alvo: ")
    perfil = carregar_perfil(L, usuario_alvo)
    if perfil is None:
        return

    seguidores = coletar_seguidores(perfil)
    seguidos = coletar_seguidos(perfil)
    salvar_dados(usuario_alvo, seguidores, seguidos)

    print(f"{usuario_alvo} possui {len(seguidores)} seguidores e segue {len(seguidos)} perfis.")

# Executa a função principal
listar_seguidores_e_seguidos()
