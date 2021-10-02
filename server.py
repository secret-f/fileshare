from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary

def check(fn):
    return '\\' in fn or '/' in fn

def uploadfile(file):
    content = file.read()
    try:
        f = open(file.name, 'xb')
    except FileExistsError:
        return 1
    else:
        f.write(content)
        f.close()
    return 0

def getfile(filename):
    try:
        assert not check(filename)
        return Binary(open(filename, 'rb').read())
    except (AssertionError, FileNotFoundError):
        return 1

s = SimpleXMLRPCServer(("", 56233))
s.register_function(uploadfile)
s.register_function(getfile)
s.serve_forever()