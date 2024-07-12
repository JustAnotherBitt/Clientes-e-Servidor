# Ferramentas simples de rede
Aqui você encontra um trio: **cliente_udp**, **cliente_tcp** e **servidor** (esses dois últimos andam juntos). Essas são ferramentas simples e fáceis de usar e, como tudo no mundo da programação, podem ser melhoradas.
Elas foram feitas em python, e uma biblioteca importante utilizada nos programas foi a biblioteca socket, que permitiu fazer as conexões entre cliente e servidor.

> _Observação: Um **soquete de rede** (em inglês: **network socket**) é um ponto final de um fluxo de comunicação entre processos através de uma rede, e um **endereço de soquete** (**socket address**) é a combinação de um endereço de IP e um número da porta, como pode ser visto nesses programas._

## Como cada ferramenta funciona?
É simples! Vamos em etapas:

Antes de tudo, você deve saber rodar cada programa. Para isso, clique no ícone de _start_ ou _play_, descrito como ***run***, na parte superior do PyCharm (a IDE que usei para fazer os programas).

![image](https://github.com/LeRodrigues2005/clientes-e-servidor/assets/97632543/6ddaddb4-6c83-4c83-9ebd-f7b9b553bc81)

## Executando o servidor:

1°) execute o arquivo ***servidor.py***;

2°) abra um terminal e digite o seguinte comando: ` nc 127.0.0.1 4466 ` 


![image](https://github.com/LeRodrigues2005/clientes-e-servidor/assets/97632543/d315f88f-6ac4-4f08-8ea2-bef7594f1ec4)

- O que for escrito no terminal será salvo no arquivo _output.txt_.

## Executando o cliente_udp:

1°) abra um terminal e digite o seguinte comando: ` nc -lvup 127.0.0.1 4466 ` 

2°) execute o arquivo ***cliente_udp***.


![image](https://github.com/LeRodrigues2005/clientes-e-servidor/assets/97632543/a89fa36e-04b5-4db9-850d-e34eca2bd077)


## Executando o cliente_tcp no servidor:

- O cliente TCP é uma aplicação que se conecta ao servidor TCP. Para fazer a conexão, seiga os seguintes passos:

1°) execute o arquivo ***servidor***;

2°) abra outro terminal e viaje até a pasta em que está localizado o programa (passo importante!!);

3°) execute o programa ***cliente_tcp*** com o seguinte comando: ` python cliente_tcp.py ` 

![image](https://github.com/LeRodrigues2005/clientes-e-servidor/assets/97632543/248c64ef-89d5-4980-83ee-1ffe5db0c4da)

- Será criado um arquivo chamado _output.txt_, que conterá o que foi inserido no ` client.send ` em ***cliente_tcp***. 
