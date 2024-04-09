# executar somente depois que o servidor tcp estiver em execução
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 TCP
client.settimeout(1)  # se a conexão não for estabelecida em um segundo, encerra a conexão e retorna except

try:
    client.connect(("127.0.0.1", 4422))  # ip local e porta escolhida
    client.send(b"Sua mensagem aqui\n")  # "b" transforma a string em bytes para poder ser enviada
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)

except Exception as error:
    print("Um erro ocorreu.")
    print(error)
