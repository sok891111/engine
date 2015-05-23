import socket
import libssh2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('128.121.216.148', 22))

session = libssh2.Session()
session.startup(sock)
session.userauth_password('john', '******')

channel = session.channel()
channel.execute('ls -l')

print channel.read(1024)