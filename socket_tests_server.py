#!/usr/bin/python 
# 
# Coded by: Alisson Machado
# Contact: alisson.copyleft@gmail.com
# servidor que recebe mensagens de aplicação client parecido com o netsend
#
import socket 
host = 'localhost' 
port = 5432 
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(10) 
print ('aguardando conexao') 
con, cliente = serv_socket.accept() 
print ('conectado') 
print ("aguardando mensagem") 
recebe = con.recv(1024) 
print ("mensagem recebida: "+ str(recebe)) 
