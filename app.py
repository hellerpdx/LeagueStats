import os
import csv
import operator
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

def moneyteams(file):
    f = open(file)
    reader = csv.reader(f)
    reader.next()

    balance = {}

    for row in reader:
        if row[3] in balance:
            if row[2] == 'CORRECT':
                balance[row[3]] += int(row[4])
            else:
                balance[row[3]] -= int(row[4])
        else:
            if row[2] == 'CORRECT':
                balance[row[3]] = int(row[4])
            else:
                balance[row[3]] = int(row[4]) * -1
    
    sorted_x = sorted(balance.iteritems(), key=operator.itemgetter(1), reverse=True)
    top3 = sorted_x[0:3]
    bottom3 = sorted_x[-3:]
    

@app.route("/")

def calculate():
    return render_template('playerplot.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

