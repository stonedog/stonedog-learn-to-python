import cherrypy

class Root:
    pass

class XmlRpc(cherrypy._cptools.XMLRPCController):
    @cherrypy.expose
    def add(self, a, b):
        res={}
        res['param1']=a
        res['param2']=b
        res['result']=a+b
        return res

root = Root()
root.xmlrpc = XmlRpc()

cherrypy.tree.mount(root, config={'/': {
'request.dispatch': cherrypy.dispatch.XMLRPCDispatcher(),
}})

cherrypy.quickstart(root)
