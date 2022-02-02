#!/usr/bin/env python
# coding: utf-8

import socket
import threading
 
#print_lock = threading.Lock()


maPrise = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#--------------------mon ip locale
nomOrdi = socket.gethostname()
ipOrdi = socket.gethostbyname(nomOrdi)

print('adresse serveur :', ipOrdi)
print('='*50)

#--------------------le serveur
maPrise.bind((ipOrdi, 10444)) 
maPrise.listen(1)

#--------------------initialisation des variables
nbDePoste = 2
lesClients=[]
n=0


def threaded(c):
    print(c)
    while True:
 
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
             
            # lock released on exit
            #print_lock.release()
            break
 
        # reverse the given string from client
        data = data[::-1]
        for ref2 in lesClients:
                ref2.send(data)
        print(data)
    # connection closed
    c.close()

#--------------------reception des clients
while True :
        #les infos du client
        refClient, ipClient = maPrise.accept()
        #affichage
        print('-'*20+' '+str(ipClient)+' '+'-'*20)
        #memorisations
        lesClients.append(refClient)
        #deux réponses au client
        #print_lock.acquire()
        threading.Thread(target=threaded, args=(refClient,)).start()


#--------------------renvoi des info à tous
        
maPrise.close() 
print('FIN===')
