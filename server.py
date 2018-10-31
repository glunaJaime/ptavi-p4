#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import socketserver


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    dicc = {}
    
    def get_expires(self, mensaje):
        time = mensaje.split("EXPIRES: ")[1]
        time = time.split("\r")[0]
        return(int(time))
    
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"Hemos recibido tu peticion")
        IP = self.client_adress
        print("IP: " + IP)
        PORT = self.client_address
        print("PORT: " + str(PORT))
        
        whilen 1: 
            line = self.rfile.read()
            print("El cliente nos manda ", line.decode('utf-8'))

if __name__ == "__main__":
    try:
        # Listens at localhost ('') port 6001 
        # and calls the EchoHandler class to manage the request
        serv = socketserver.UDPServer(('', 6001), EchoHandler) 
        print("Lanzando servidor UDP de eco...")
        serv.serve_forever()
    except KeyboardInterrupt:
            print("Finalizado servidor")
