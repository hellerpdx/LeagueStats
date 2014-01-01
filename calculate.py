import csv

correct = 0
incorrect = 0

f = open('static/files/ler210.csv')
reader = csv.reader(f)
reader.next()

for row in reader:
    if row[2] == 'CORRECT':
        correct += 1
    else:
        incorrect += 1

print "Correct =", correct
print "Incorrect =", incorrect