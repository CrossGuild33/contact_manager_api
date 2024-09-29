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

## API Externas
 1. Utilizei a getLocation para pegar as coordenadas do endereço colocado
     1. API key da getLocation: 0e51a6e45511417ca30a54aac169e293
       
 2. Utilizei a OpenStreetMap para mostrar a localizacao das coordenadas no mapa.
    1. Não é necessário uso de nenhuma API key para a mesma, sendo ela utilizada diretamente no front-end.
       
## Para o Dockerfile
1. Instale o Docker em sua máquina
2. Depois utilize o comando `docker build -t (nome do container) .` para criar o container.
3. E por fim para rodar `docker run -d --name (nome do container) --network (nome da network) -p 8080:80 (nome da container image)`
    1. Talvez seja necessário criar o network para integrar o front e o back.
    2. Utilize este comando para a criação do network `docker network create (nome da network)`
