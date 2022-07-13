#!/usr/bin/env python3

import socket, requests

# Make sure we clean up when we fail
def cleanup(e):
    print(e)
    conn.close()
    sock.close()
    exit(1)

# External port to listen on and report status to HAProxy
listen_port = 5555

# Location of the Patroni API
data_target = 'http://localhost:8008'

# Get the current role from Patroni's API
def getstate():
    try:
        r = requests.get(data_target)
    except:
        return 'null'
    data = r.json()
    role = data['role']
    return role

# Set up a listen socket on listen_port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', listen_port))
sock.listen(1)

# Loop waiting for client requests in blocking mode
while True:
    conn, addr = sock.accept()
    state = getstate()

    # Set our response based on the state; only `master` should be READY in read-write mode
    if state == 'master':
        data = b'READY\n'
    else:
        data = b'MAINT\n'

    # Send the data to the client
    try:
        conn.sendall(data)
        conn.close()
    except Exception as e:
        cleanup(e)
