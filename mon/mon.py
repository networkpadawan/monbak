import commands, MySQLdb, _mysql, sys

#good enough commands
totalcpu = commands.getoutput("ps -eo pcpu,pid,user,args | awk '{ sum += $0 } END { print sum }'")
iowaitcpu = commands.getoutput("iostat | awk 'NR==4' |  awk '{print $4}'")
totalmem = commands.getoutput("free -m | grep Mem | awk '{print $2}'")
usedmem = commands.getoutput("free -m | grep Mem | awk '{print $3}'")
freemem = commands.getoutput("free -m | grep Mem | awk '{print $4}'")
topname = commands.getoutput("ps -eo pcpu,pid,user,args | sort -k 1 -r -n | head -3 | awk '{print $4}'")
topvalue = commands.getoutput("ps -eo pcpu,pid,user,args | sort -k 1 -r -n | head -3 | awk '{print $1}'")
usedsize = commands.getoutput("df -h | awk 'NR==2'  | awk '{print $5}'")

#write to bd
conn = MySQLdb.connect (host = "192.168.1.6", user = "testuser", passwd = "testuser", db = "testdb")
cursor = conn.cursor()
    
comm = """CREATE TABLE IF NOT EXISTS RPIMON (
      Id INT PRIMARY KEY AUTO_INCREMENT,
      DATETIME DEFAULT NULL,
      TOTALCPU FLOAT,
      IOWAITCPU FLOAT,
      TOTALMEM FLOAT,
      USEDMEM FLOAT,
      FREEMEM FLOAT,
      TOPNAME FLOAT,         
      TOPVALUE FLOAT, 
      USEDSIZE FLOAT )"""
         
cursor.execute(comm)
    
comm = """INSERT INTO RPIMON(totalcpu, iowaitcpu, totalmem, usedmem, freemem, topname, topvalue, usedsize) \
          VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s,')""" % \
          (totalcpu, iowaitcpu, totalmem, usedmem, freemem, topname, topvalue, usedsize)

try:
   cursor.execute(comm)
   conn.commit()
except:
   conn.rollback()
conn.close()
