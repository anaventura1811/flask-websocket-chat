# flask-websocket-chat

**flask-websocket-chat** é um projeto de chat em tempo real construído com Python e Flask SocketIO. O objetivo deste projeto é consolidar conceitos aprendidos na Formação em Python da Rocketseat de comunicação em tempo real utilizando websockets, desenvolvendo uma aplicação de chat simplificada e funcional.

## Sobre o Projeto

O projeto foi criado como parte dos meus estudos sobre Flask e comunicação em tempo real. Usando Flask e a biblioteca Flask-SocketIO, é possível criar uma conexão websocket para que os usuários enviem e recebam mensagens em tempo real. Esse projeto fornece uma base para entender os principais conceitos de websockets e sua implementação prática em aplicações web.

## Funcionalidades

- **Envio de Mensagens em Tempo Real**: Permite que os usuários enviem mensagens, que são imediatamente transmitidas para todos os outros usuários conectados.
- **Atualização Instantânea**: Todas as mensagens enviadas são imediatamente exibidas para todos os usuários, proporcionando uma comunicação contínua.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web usado para construir a aplicação.
- **Flask-SocketIO**: Biblioteca que facilita o uso de websockets em Flask.

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/flask-websocket-chat.git
    cd flask-websocket-chat
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor:
    ```bash
    flask run
    ```

5. Acesse o chat em tempo real pelo navegador:
    ```
    http://127.0.0.1:5000
    ```

## Licença

Este projeto é licenciado sob a Licença MIT.
