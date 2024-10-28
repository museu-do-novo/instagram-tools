# InstaFollowerTracker

**InstaFollowerTracker** é um script em Python que utiliza a biblioteca Instaloader para acessar e extrair dados de seguidores e seguidos de perfis públicos do Instagram. O programa permite login seguro e opcionalmente armazena a sessão para facilitar acessos futuros.

## Funcionalidades

1. **Login Seguro e Persistente**: Faz login na conta do Instagram e salva a sessão para uso futuro, reduzindo a necessidade de múltiplos logins.
2. **Coleta de Seguidores e Seguidos**: Extrai e salva as listas de seguidores e perfis seguidos de qualquer perfil público do Instagram.
3. **Salvamento em JSON**: Armazena as listas de seguidores e seguidos em um arquivo JSON, facilitando a análise e manipulação futura dos dados.
4. **Tratamento de Erros e Mensagens Informativas**: Fornece feedback ao usuário em cada etapa, garantindo uma experiência mais amigável e com mensagens de erro detalhadas.

## Pré-requisitos

- Python 3.7 ou superior
- Instaloader: Instale a biblioteca com `pip install instaloader`

## Como Usar

1. **Execute o script**: Inicie o programa no terminal com `python insta_follower_tracker.py`.
2. **Login**:
   - Insira seu nome de usuário e senha do Instagram.
   - Opcionalmente, você pode salvar a sessão para simplificar logins futuros.
3. **Selecionar Perfil Alvo**:
   - Insira o nome de usuário do perfil que deseja monitorar.
4. **Coleta de Dados**:
   - O programa coletará seguidores e perfis seguidos do usuário alvo.
   - As listas serão salvas em um arquivo JSON com o nome do perfil alvo.

## Estrutura do Código

### Funções

- **realizar_login**: Realiza o login no Instagram com suporte para salvar a sessão localmente.
- **carregar_perfil**: Carrega o perfil do usuário alvo no Instagram.
- **coletar_seguidores**: Coleta e retorna a lista de seguidores do perfil.
- **coletar_seguidos**: Coleta e retorna a lista de perfis que o usuário alvo segue.
- **salvar_dados**: Salva os dados de seguidores e seguidos em um arquivo JSON para fácil acesso.
 
## Exemplo de Uso

    $ python insta_follower_tracker.py
    Digite seu nome de usuário do Instagram: seu_usuario
    Digite sua senha do Instagram: sua_senha
    Salvar sessão para logins futuros? (s/n): s
    Digite o nome do perfil alvo: perfil_exemplo
    Perfil perfil_exemplo carregado.
    Coletando seguidores de perfil_exemplo...
    30 seguidores coletados.
    Coletando perfis seguidos por perfil_exemplo...
    20 seguidos coletados.
    Dados de perfil_exemplo salvos em perfil_exemplo_dados.json

## Arquivo de Saída

    perfil_exemplo_dados.json: Contém as listas de seguidores e seguidos do perfil alvo em formato JSON.

## Exemplo do arquivo JSON

json

{
    "seguidores": ["seguidor1", "seguidor2", "seguidor3"],
    "seguidos": ["seguido1", "seguido2"]
}

## Observações

Privacidade: O programa só acessa perfis públicos ou perfis aos quais você tem permissão de visualização.
Login Persistente: Para segurança, as sessões são salvas no dispositivo local.

## Erros Comuns

  Erro de Login: Pode ocorrer caso o nome de usuário ou senha estejam incorretos, ou se houver problemas de conexão.
  Acesso Negado ao Perfil: Certifique-se de que o perfil alvo é público ou acessível.

==============================================================================================================

# InstaStoryDownloader

**InstaStoryDownloader** é um programa em Python que utiliza a biblioteca Instaloader para fazer login no Instagram e baixar stories públicos de um perfil alvo, salvando-os localmente. 

## Funcionalidades

1. **Login Seguro**: O programa realiza o login no Instagram com a opção de salvar a sessão para facilitar futuros logins.
2. **Download de Stories Públicos**: Baixa os stories disponíveis de um perfil público especificado pelo usuário.
3. **Feedback Informativo**: Fornece mensagens detalhadas em cada etapa, ajudando o usuário a entender o progresso do download.
4. **Opção de Limpeza da Tela**: Permite ao usuário escolher se deseja limpar a tela ao iniciar, ideal para uso em terminais.

## Pré-requisitos

- **Python 3.7** ou superior
- **Instaloader**: Instale com `pip install instaloader`
- **Variáveis de Ambiente**: Recomendado para armazenar o nome de usuário e senha com segurança, evitando hardcoding.

## Como Usar

1. **Execute o script**:
   ```shell
   python insta_story_downloader.py

    Login:
        Insira seu nome de usuário e senha do Instagram.
        Escolha se deseja salvar a sessão para simplificar futuros logins.
    Baixar Stories:
        Insira o nome do perfil alvo (perfil público) para baixar os stories.
    Concluir:
        Os stories serão baixados e salvos na pasta padrão de saída.

## Estrutura do Código:
  Funções Principais:

    realizar_login: Gerencia o login, incluindo a opção de salvar a sessão.
    carregar_perfil: Carrega o perfil alvo e verifica a disponibilidade de stories públicos.
    baixar_stories: Realiza o download dos stories públicos do perfil alvo.
    iniciar_download_stories: Função principal que gerencia o fluxo de execução e interações com o usuário.

## Exemplo de Uso:

    $ python insta_story_downloader.py
    Deseja limpar a tela antes de iniciar? (s/n): s
    Digite seu nome de usuário do Instagram: seu_usuario
    Digite sua senha do Instagram: sua_senha
    Salvar sessão para futuros logins? (s/n): s
    Digite o nome do perfil alvo para baixar stories: perfil_exemplo
    Perfil perfil_exemplo carregado com sucesso.
    Baixando stories de perfil_exemplo...
    Stories de perfil_exemplo baixados com sucesso!

## Observações

    Privacidade: O programa acessa apenas stories públicos ou de perfis aos quais você tenha permissão de visualização.
    Login Persistente: Para maior segurança, a sessão salva fica armazenada apenas localmente.

## Erros Comuns

    Erro de Login: Verifique se as credenciais estão corretas e se há conexão com a internet.
    Stories Não Disponíveis: Caso o perfil alvo não tenha stories públicos ativos, o programa notificará o usuário.
