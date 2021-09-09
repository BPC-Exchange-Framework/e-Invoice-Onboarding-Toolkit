# certauth.server.py
from flask import Flask

MESSAGE = "shhhh, this is secret"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return MESSAGE + "\n"

if __name__ == "__main__":
    app.run(port=5684, 
        ssl_context=('server-public-key.pem', 'server-private-key.pem')
    )
