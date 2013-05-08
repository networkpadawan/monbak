#!/usr/bin/env python
import sys, MySQLdb

def PrintFields(database, table):
    """ Connects to the table specified by the user and prints out its fields in HTML format used by Ben's wiki. """
    conn = MySQLdb.connect (host = "192.168.1.6", user = "testuser", passwd = "testuser", db = "testdb")
    mysql = conn.cursor()
    sql = """ SELECT * FROM  %s """ % table
    mysql.execute(sql)
    fields=mysql.fetchall()
    print '<table border="0"><tr><th>Id</th><th>Date</th><th>TOTALCPU</th><th>IOWAITCPU</th><th>TOTALMEM </th><th>USEDMEM</th><th>FREEMEM</th><th>TOPNAME</th><th>TOPVALU$
    print '<tbody>'
    counter = 0
    for field in fields:
        counter = counter + 1
        id = str(field[0])
        date = str(field[1])
        totalcpu = str(field[2])
        iowaitcpu = str(field[3])
        totalmem = str(field[4])
        usedmem = str(field[5])
        freemem = str(field[6])
        topname = str(field[7])
        topvalue =str( field[8])
        usedsize = str(field[9])
#        print '<tr><td>' + str(counter) + '</td><td>' + name + '</td><td>' + type + '</td><td></td></tr>'
        print '<tr><td>' + id + '</td><td>' + date + '</td><td>' + totalcpu + '</td><td>' + iowaitcpu + '</td><td>' + totalmem + '</td><td>' + usedmem +  '</td><td>' + f$
    print '</tbody>'
    print '</table>'
    mysql.close()
    conn.close()

database = "testdb"
table = "rpi256"

print " HTML for mysql"
print "========================"
PrintFields(database, table)
