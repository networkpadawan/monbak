#!/usr/bin/python
import sys
import matplotlib
matplotlib.use('Agg')
from pylab import *
import MySQLdb
db = MySQLdb.connect (host = "192.168.1.6", user = "tiago", passwd = "1", db = "testdb")

cursor = db.cursor()

query = sys.argv[1]
cursor.execute(query)
result = cursor.fetchall()
t = []
s = []
a = []
for record in result:
  t.append(record[0])
  s.append(record[1])

subplot(t, s)
axis([min(t), max(t), min(s), max(s)])
title("Teste")
grid(False)

F = gcf()
DPI = F.get_dpi()
F.savefig('plot.png',dpi = (115))
