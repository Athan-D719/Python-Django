import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000)) #server running on port 9000
#127.0.0.1 is the ipv4 connection called 'LOOP BACK'
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
#OPEN THE SIMPLE SERVER
'''
HTTP /1.1 200 OK
Content-Type: text/html; charset=utf-8
<html><body>Hello World</body></html>
'''