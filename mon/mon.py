#!/usr/bin/python
import commands, MySQLdb, sys, socket, time
#good enough commands
totalcpu = commands.getoutput("ps -eo pcpu,pid,user,args | awk '{ sum += $0 } END { print sum }'")
iowaitcpu = commands.getoutput("iostat | awk 'NR==4' |  awk '{print $4}'")
totalmem = commands.getoutput("free -m | grep Mem | awk '{print $2}'")
usedmem = commands.getoutput("free -m | grep Mem | awk '{print $3}'")
freemem = commands.getoutput("free -m | grep Mem | awk '{print $4}'")
topname = commands.getoutput("ps -eo pcpu,pid,user,args | sort -k 1 -r -n | head -1 | awk '{print $4}'")
topvalue = commands.getoutput("ps -eo pcpu,pid,user,args | sort -k 1 -r -n | head -1 | awk '{print $1}'")
usedsize = commands.getoutput("df -h | awk 'NR==2'  | awk '{print $5}' | sed 's/%//g'")
date = time.strftime('%Y-%m-%d %H:%M:%S')
host = socket.gethostname()
#write to bd
conn = MySQLdb.connect (host = "192.168.1.6", user = "testuser", passwd = "testuser", db = "testdb")
cursor = conn.cursor()

comm = """CREATE TABLE IF NOT EXISTS %s (
      Id INT PRIMARY KEY AUTO_INCREMENT,
      DATE DATETIME,
      TOTALCPU FLOAT,
      IOWAITCPU FLOAT,
      TOTALMEM FLOAT,
      USEDMEM FLOAT,
      FREEMEM FLOAT,
      TOPNAME CHAR(15),
      TOPVALUE FLOAT,
      USEDSIZE FLOAT)""" % host

cursor.execute(comm)

comm = """INSERT INTO {0} (date, totalcpu, iowaitcpu, totalmem, usedmem, freemem, topname, topvalue, usedsize) \
          VALUES ('{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}')"""  \
          .format(host, date, totalcpu, iowaitcpu, totalmem, usedmem, freemem, str(topname), topvalue, int(usedsize))


try:
   cursor.execute(comm)
   conn.commit()
except:
   conn.rollback()
conn.close()
