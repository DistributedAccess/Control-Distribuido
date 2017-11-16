from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib


Server = xmlrpclib.ServerProxy("http://localhost:2018")


m = Server.Ingresar('11.5.20.18','Servidor')
print(m)

for i in range(len(m)):
    for j in range(len(m[i])):
        print str(m[i][j])
