import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


app = Flask(__name__)

app.config.update(
    DEBUG = True,
)


@app.route("/")

def hello():
    return render_template('playerplot.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
