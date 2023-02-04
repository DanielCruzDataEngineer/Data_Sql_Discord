#!/usr/bin/python
# Coded by: Alisson Machado
# Contact: alisson.machado@responsus.com.br
#

import socket 

ip = input('digite o ip de conexao: ') 
port = 5432 
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 
mensagem = bytearray(input("digite uma mensagem para enviar ao servidor "),encoding='utf-8') 
client_socket.send(mensagem) 
print ('mensagem enviada') 
client_socket.close()