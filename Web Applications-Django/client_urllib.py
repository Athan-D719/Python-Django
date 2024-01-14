import urllib.requests

fhand = urllib.requests.urlopen('http://127.0.0.1:9000/romeo.txt')
for line in fhand:
    print(line.decode().strip())

'''
<html><body>Hello World</body></html>
'''
