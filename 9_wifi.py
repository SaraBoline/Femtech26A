import network
import socket

# -------------------------
# WIFI ACCESS POINT
# -------------------------

SSID = "FemTech"
PASSWORD = "12345678"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD)

while not ap.active():
    pass

ip = ap.ifconfig()[0]

print("FemTech server startet")
print("IP:", ip)

# -------------------------
# GLOBAL BESKED
# -------------------------

current_message = "NONE"

# -------------------------
# HTML
# -------------------------

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

body {
    font-family: Arial;
    text-align: center;
    margin-top: 40px;
}

button {
    width: 250px;
    height: 70px;
    font-size: 24px;
    margin: 10px;
}

</style>
</head>
<body>

<h1>FemTech Awareness Network</h1>

<form action="/help">
<button>HELP</button>
</form>

<form action="/idea">
<button>IDEA</button>
</form>

<form action="/collaborate">
<button>COLLABORATE</button>
</form>

<form action="/break">
<button>BREAK</button>
</form>

</body>
</html>
"""

# -------------------------
# WEB SERVER
# -------------------------

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Webserver klar")

while True:

    client, address = server.accept()

    request = client.recv(1024)

    try:
        request = request.decode()
    except:
        request = ""

    # -------------------------
    # NOTIFIKATIONER
    # -------------------------

    if "/help" in request:
        current_message = "HELP"
        print("HELP")

    elif "/idea" in request:
        current_message = "IDEA"
        print("IDEA")

    elif "/collaborate" in request:
        current_message = "COLLABORATE"
        print("COLLABORATE")

    elif "/break" in request:
        current_message = "BREAK"
        print("BREAK")

    # -------------------------
    # API ENDPOINT
    # -------------------------

    if "/message" in request:

        response = current_message

        client.send(
            "HTTP/1.0 200 OK\r\n"
            "Content-type: text/plain\r\n\r\n"
        )

        client.send(response)

    else:

        client.send(
            "HTTP/1.0 200 OK\r\n"
            "Content-type: text/html\r\n\r\n"
        )

        client.send(html)

    client.close()
