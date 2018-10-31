#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Clase (y programa principal) para un servidor de eco en UDP simple."""

import sys
import socketserver
import json
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """Echo server class."""

    Client_data = {}

    def register2json(self):
        """Json creator."""
        with open('registered.json', "w") as outfile:
            json.dump(self.Client_data, outfile, sort_keys=True, indent=4)

    def json2registered(self):
        """Json file checker."""
        try:
            with open("registered.json", "r") as data_file:
                self.Client_data = json.load(data_file)
        except(FileNotFoundError):
            pass

    def comprobar_cad_del(self):
        """Output time and user's delete checker."""
        time_str = time.strftime('%Y-%m-%d %H:%M:%S +%Z',
                                 time.gmtime(time.time()))
        deleted = []
        for cosas in self.Client_data:
            if self.Client_data[cosas]['expires'] <= time_str:
                deleted.append(cosas)
        for users in deleted:
            self.Client_data.pop(users)

    def handle(self):
        """handle method of the server class."""
        atributos = {}  # Value de datos del cliente.
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

        if not self.Client_data:
            self.json2registered()

        LINE = self.rfile.read()
        DATA = LINE.decode('utf-8')
        CORTES = DATA.split(' ')
        time_expire_str = time.strftime('%Y-%m-%d %H:%M:%S +%Z',
                                        time.gmtime(time.time() +
                                                    int(CORTES[3][:-4])))
        if CORTES[0] == 'REGISTER':
            atributos = self.client_address[0]
            self.Client_data[CORTES[1].split(':')[-1]] = atributos
            print("JULIA:", self.Client_data)
            if CORTES[3][:-4] != '0':
                tiempo = time_expire_str
            else:
                try:
                    tiempo = time.strftime('%Y-%m-%d %H:%M:%S +%Z',
                                           time.gmtime(time.time()))
                    self.Client_data[CORTES[1].split(':')
                                     [-1]].append(atributos)
                    self.comprobar_cad_del()
                except KeyError:
                    pass

        print("Datos cliente(IP, puerto): " + str(self.client_address))
        print("El cliente nos manda ", DATA[:-4])

        self.register2json()


if __name__ == "__main__":

    Server_port = int(sys.argv[1])
    serv = socketserver.UDPServer(('', Server_port), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
