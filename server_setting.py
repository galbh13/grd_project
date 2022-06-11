import socket
#region ================  C O N S T A N T S ==============
IP = "0.0.0.0"
PORT = 50111
SERVER_IP = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
SIZE = 1024
approved = "yes"
not_approved = "no"
#endregion
print(SERVER_IP)
