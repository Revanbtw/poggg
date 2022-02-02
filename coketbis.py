from tkinter import*
import random
import socket
from time import*
from _thread import*
import threading

print_lock = threading.Lock()

#vox.send("Sussy".encode())
vox = 0
size = 60

def play(c):
    while True:
        data = c.recv(1024)
        if not data:
            print("BYE")
            print_lock.release()
            break
        data = data[::-1].decode()
        pos = data.split(" ")
        print(pos)
        monTissu.create_oval(int(pos[0])-size/2,int(pos[1])-size/2,int(pos[0])+size/2,int(pos[1])+size/2,
                                      outline = hexacol(),width = 2,fill = hexacol())
        print(data)
    c.close()

def press():
    global vox
    vox = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hote = "10.72.208.111"
    port = 10444
    

    vox.connect((hote, port))
    start_new_thread(play, (vox,))

def hexacol():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def clic(event):
    vox.send((str(event.x)+" "+str(event.y)).encode())


maFen = Tk()
maFen.title("saluman")
monTissu = Canvas(maFen,width = 900 , height = 900, bg = "#6174EE")
monTissu.pack()
w = Button ( maFen, command=press, width = 8)
w.pack()


monTissu.bind('<Button-1>', clic)
monTissu.pack()
    
maFen.mainloop()


