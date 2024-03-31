# Leia.Me

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Comece por aqui

1. Vou assumir que para chegar ate aqui você já tenha o python instalado no seu PC. Portanto, ao clonar o projeto, primeiro execute o comando abaixo para criar o ambiente virtual; 

> `python -m venv venv`.

2. Se estiver usando o PowerShel do Windows, vai ser importante lembrar de que primeiro deve executar o comando abaixo para que ele possa reconhecer alguns comandos necessários ao projeto; 

> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`



3. Feito isso, certifique-se de **ativar** o ambiente virtual criado, execute o comando; `.\venv\Scripts\activate.ps1` - para ativar o ambiente no Windows.

> **Instalando as Dependencias do Projeto**: Lembre-se de rodar o comando `pip install -r requirements.txt`, aguarde a instalação completar. 

> **Importante Lembrar**: Nunca enviamos a `SECRET_KEY` para o Github, portanto vamos precisar fazer uma cópia do arquivo `.env_exemplo`, renomear a cópia para `.env` apenas, e dentro desse arquivo criar uma chave de segurança lá.

4. Outro detalhe importante, nunca enviamos o arquivo do banco de dados para o Github tambem, portanto, vai ser necessário agora rodar as migrações para criar todas as tabelas localmente no seu DB. Execute o comando a seguir `python manage.py migrate`, aguarde as tabelas serem criadas localmente.

5. Repara que seu banco de dados local acabou de ser criado, portanto, não existe nenhum usuario cadastrado. Vamos resolver isso. Execute o comando `python manage.py createsuperuser`. 

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
