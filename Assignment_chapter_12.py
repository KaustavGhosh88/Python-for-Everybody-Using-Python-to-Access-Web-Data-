import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.pythonlearn.com", 80))
mysock.send('GET /code/intro-short.txt HTTP/1.1\n')
mysock.send('Host: pythonlearn.com\n\n')

while True: 
    data = mysock.recv(512) 
    if ( len (data) < 1 ): 
        break 
    print data 

mysock.close()
