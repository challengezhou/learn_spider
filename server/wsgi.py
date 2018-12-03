from wsgiref.simple_server import make_server
from server.application import application

httpd = make_server('', 8080, application)
print('http listen on port 8080...')
httpd.serve_forever()