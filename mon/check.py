#!/usr/bin/python
import commands, MySQLdb, sys, socket, time

list = ["rpi256","rpi256","rpi256"]
for host in list:
    conn = MySQLdb.connect (host = "192.168.1.6", user = "tiago", passwd = "1", db = "testdb")
    cursor = conn.cursor()
    query = "select * from %s order by Id desc LIMIT 10" %(host)
    print query
    cursor.execute(query)
    result = cursor.fetchall()
    id = []
    date = []
    totalcpu = []
    iowaitcpu = []
    totalmem = []
    usedmem = []
    freemem = []
    topname = []
    topvalue = []
    usedsize = []
    for record in result:
        id = record[0]
        date= record[1]
        totalcpu = record[2]
        iowaitcpu = record[3]
        totalmem = record[4]
        usedmem = record[5]
        freemem = record[6]
        topname = record[7]
        topvalue = record[8]
        usedsize = record[9]
        print id, date, totalcpu, iowaitcpu, totalmem, usedmem, freemem, topname, topvalue, usedsize
