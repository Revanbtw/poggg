import socket
import threading

maPrise = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


nomOrdi = socket.gethostname()
ipOrdi = socket.gethostbyname(nomOrdi)

print('adresse serveur :', ipOrdi)
print('='*50)

maPrise.bind((ipOrdi, 10444)) 
maPrise.listen(1)
lesClients=[]


def threaded(c):
    print(c)
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            break
        data = data[::-1]
        for ref2 in lesClients:
                ref2.send(data)
        print(data)
    c.close()

while True :
        refClient, ipClient = maPrise.accept()
        print('-'*20+' '+str(ipClient)+' '+'-'*20)
        lesClients.append(refClient)
        threading.Thread(target=threaded, args=(refClient,)).start()

maPrise.close() 
print('FIN===')
