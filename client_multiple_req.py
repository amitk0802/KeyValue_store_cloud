# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:53:29 2021

@author: amitk
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:46:37 2021

@author: amitk
"""

import socket

HEADER = 2048
server_ip = '10.138.0.2'
server_port = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "quit"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
#sentence = input("> ")
req = ['get S520', 'get E516', 'get B505']
multi_req = req * 100



def send_req(sentence):
    message = sentence.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)
    print(client_socket.recv(2048).decode(FORMAT))

connected = True
while connected:
    for i in multi_req:
        sentence = i
        if sentence == 'quit':
            break
        else:
            send_req(sentence)






#modifiedSentence = client_socket.recv(1024)
#print(f"From Server: {modifiedSentence}")
#client_socket.close()

