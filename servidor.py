# este é um servidor TCP
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = open("output.txt", "w")  # cria um arquivo para o output

try:
    server.bind(("0.0.0.0", 4422))
    server.listen(5)  # escuta em até 5 conexões simultâneas
    print("Listening...")

    client_socket, address = server.accept()  # aceita a conexão (retorna duas tuplas)
    print("Received from: " + address[0])  # pega o primeiro elemento da segunda tupla (colocada na var "address")

    data = client_socket.recv(1024).decode()

    file.write(data)  # escreve o conteúdo de data no arquivo do output

    server.close()

except Exception as error:
    print("Erro: ", error)
    server.close()

