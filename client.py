#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

#SERVER = 'localhost'
#PORT = 6001
#LINE = '¡Hola mundo!'

def registro(mensaje, direccion):
    palabra = "REGISTER"
    palabra = palabra + "sip: " + direccion + "SIP/2.0\r\n\r\n" + mensaje
    print(palabra)
    return palabra
    
# Constantes. Dirección IP del servidor y contenido a enviar
server = sys.argv[1]
port = int(sys.argv[2])
#line = (' '.join)(sys.argv[3:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsocket(socket.SOL_SOKET, soket.SOCK_REUSADDR, 1)
my_socket.connect(server, port)

frase = ' '.join(line)
print("Enviando: " + frase)
my_socket.send(bytes(frase, 'utf-8') + b'\r\n')

my_socket.send(bytes(registro(frase, mi_direc), 'utf-8') + '\r\n')

data = my_socket.recv(1024)
print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
