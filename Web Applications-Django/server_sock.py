from socket import * #import all from socket

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) #making an endpoint (socket)
    try:
        serversocket.bind(('localhost', 9000)) #one port, jut one window
                                               #will blow up if more
        serversocket.listen(5) #4 more phoncalls allowes(bidirectional-sockets)
        while (1):
            (clientsocket, address) = serversocket.accept() # blocking
            #the reason to do the 'accept' so the next line runs when the
            #phone call-page open is made.
            rd = clientsocket.recv(5000).decode() #unicode
            #sends and receives at the same time simultaniuosly
            pieces = rd.split('\n') #splitting headres
            if (len(pieces) > 0) : print(pieces[0]) #printing them
            #Prof we GOT IT! (url OK)
            data = "HTTP/1.1 200 OK\r\n" 
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            #constructing the responde
            clientsocket.sendall(data.encode()) #sending the UTF-8 version
            clientsocket.shutdown(SHUT_WR) #as soon as the response is sent
            #by protocol the connection must be closed
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    
    serversocket.close() #close the socket.

print("Access http://localhost:9000")
createServer() #infinite loop that sits and waits for phonecalls
        
'''
Access http://localhost:9000
GET / HTTP/1.1 #html response
GET /favicon.ico HTTP/1.1 #icon for the website [localhost:9000]
'''
#FROM THE client_sock and client_utrllib
'''
GET http://127.0.0.1/romeo.txt HTTP/1.0
'''