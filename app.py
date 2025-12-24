from flask import Flask
import python2
app = Flask(__name__)

@app.route("/")
def home():
    mac = hex(uuid.getnode())
    return f"Running | MAC: {mac}"

if __name__ == "__main__":
    app.run()
