import os
from flask import Flask


app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

@app.route("/")

def hello():
    return "League Stats!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)