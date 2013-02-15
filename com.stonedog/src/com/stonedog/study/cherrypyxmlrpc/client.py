import xmlrpclib
url='http://127.0.0.1:8080/xmlrpc'
rpcProxy=xmlrpclib.ServerProxy(url)
s=rpcProxy.add('hello','zhang')
print s
print(type(s))
