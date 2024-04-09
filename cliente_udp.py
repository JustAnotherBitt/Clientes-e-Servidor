import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM porque é udp
try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("127.0.0.1", 4433))  # encode() para tranformar a msg em bytes
        client.sendto(msg.encode(), ("127.0.0.1", 4422))  # encode() para tranformar a msg em bytes

        data, sender = client.recvfrom(1024)  # 1° elemento da tupla = data; 2° elemento (uma tupla) = sender
        print(sender[0] + ": " + data.decode())
# sender[0] para pegar apenas o 1° elemento da tupa (que conta como string) porque não pode concatenar tupla com string

        if data.decode() == "sair\n" or msg == "sair\n":
            break

    client.close()
except Exception as error:
    print("Erro de conexão")
    print(error)
    client.close()

