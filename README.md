# Administrador de Contatos

 Este é o README da sua aplicação. Aqui você encontrará informações sobre como configurar, instalar e usar sua aplicação.

## Instalação

 Para instalar os requisitos da aplicação, você pode usar o arquivo `requirements.txt`. Certifique-se de ter o Python instalado em sua máquina. Execute o seguinte comando:

`pip install -r requirements.txt`

**É importante que tenha um ambiente virtual criado.**
_____
 Após a instalação do requirements.txt e a criação do ambiente virtual, 
execute a API, no diretório raiz, com:

`(env)$ python app.py`

_____

Para verificar a documentação no swagger basta entrar:

`http://127.0.0.1:5000/apidocs`

## Para o Dockerfile
1. Instale o Docker em sua máquina
2. Depois utilize o comando `docker build -t (nome do container) .` para criar o container.
3. E por fim para rodar `docker run -d --name (nome do container) --network (nome da network) -p 8080:80 (nome da container image)`
    1. Talvez seja necessário criar o network para integrar o front e o back.
    2. Utilize este comando para a criação do network `docker network create (nome da network)`
