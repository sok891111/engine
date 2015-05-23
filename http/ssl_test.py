import socket
try:
    import ssl
except ImportError:
    pass

# context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
# context.verify_mode = ssl.CERT_REQUIRED
# context.check_hostname = True
# context.load_verify_locations("/etc/ssl/certs/ca-certificates.crt")
conn = ssl.SSLSocket(socket.socket(socket.AF_INET))
conn.connect(("www.ibm.com\\/us\\/en", 443))
conn.sendall("HEAD / HTTP/1.1\r\nHost: www.ibm.com\\/us\\/en\r\n\r\n")
print conn.recv(8024)
