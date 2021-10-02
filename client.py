from xmlrpc.client import Server, Binary
import sys, cmdapi

help_doc = '''\
help - 显示帮助

download <filename> -> 下载文件
upload <filename> -> 上传文件
quit - 退出\
'''

def uploadfile(filename):
    try: 
        f = open(filename, 'rb')
    except FileNotFoundError:
        pass
    else:
        s.uploadfile(filename, Binary(f.read()))
        f.close()

def getfile(filename):
    try:
        f = open(filename, 'wb')
    except FileNotFoundError:
        pass
    else:
        c = s.getfile(filename)
        f.write(c.data)
        f.close()
    

def help():
    print(help_doc)

s = Server(input("服务器IP：")+":56233")

cmds = {
    'upload': uploadfile, 
    'download': getfile, 
    'help': help, 
    'quit': sys.exit
}
argnum = {
    'upload': 1, 
    'download': 1,
    'help': 0, 
    'quit': 0
}
cmd = cmdapi.Cmd('> ', cmds, argnum)
try:
    while True:
        res = cmd.run()
        if res:
            if res&2:
                print("参数错误。使用 help 查看帮助。")
            if res&4:
                print("错误的命令。使用 help 查看帮助。")
except KeyboardInterrupt: 
    pass