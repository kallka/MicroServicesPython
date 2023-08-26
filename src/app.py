# Name: Karina Kallas
# Last Edited: August 26, 2023
# Description: Practice app for microservices - Flask/Docker/Kubernetes.

# ---------------------------------------------------------------------------------------------------------------------#
#
#                                IMPORTS
#
# ---------------------------------------------------------------------------------------------------------------------#
from flask import Flask, jsonify, render_template
import socket

# ---------------------------------------------------------------------------------------------------------------------#
#
#                                 SETUP and FUNCTIONS
#
# ---------------------------------------------------------------------------------------------------------------------#
app = Flask(__name__)


def fetchDetails():
    """Fetch hostname and ip address of host."""
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print(f"Hostname: {host_name}")
        print(f"IP: {ip_address}")
        return host_name, ip_address
    except:
        return "Unable to retrieve host name and/or ip address."

# ---------------------------------------------------------------------------------------------------------------------#
#
#                               ROUTES
#
# ---------------------------------------------------------------------------------------------------------------------#
@app.route("/")
def homePage():
    hostname, ip = fetchDetails()
    hostname = str(hostname)
    ip = str(ip)
    return render_template('index.html', HOSTNAME=hostname, IP=ip)


@app.route("/health")
def healthPage():
    return jsonify(
        status="UP"
    )


# ---------------------------------------------------------------------------------------------------------------------#
#
#                               MAIN
#
# ---------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
