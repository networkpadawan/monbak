#!/usr/bin/python
#v1.1
# status
# 0 ok
# 1 mount error
# 2 connection error
# 3 rsync error, check log for more info
import os,logging,sys,datetime,shutil,commands, socket,re
logging.basicConfig(filename='sync.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def check_target():
        global me
        me = (socket.gethostname())
        return me

def test_connection():
        global connstatus
        logging.info("trying storage ip")
        for testip in open('storageip.txt', 'r'):
                conn = os.system("ping -c 1 -W 1 " + testip)
                if conn == 0:
                        connstatus = 0;
                else:
                        logging.error("connection error: %s is unreachable" %(testip.rstrip('\n')))
                        connstatus = 2;
        return connstatus

def test_mountpoint():
        global mountstatus
        logging.info("checking mountpoints")
        for path in open('mountpoints.txt', 'r'):
                mount=os.path.ismount(path.rstrip('\n'))
                if mount == True:
                        mountstatus = 0
                else:
                        logging.error("mountpoint %s is unmounted, trying to force mount" %(path.rstrip('\n')))
                        mountstatus = force_mount()
        return mountstatus

def force_mount():
        mountstatus, output = commands.getstatusoutput("mount -a")
        #change mount!
        mountstatus = os.system ("mount -a")
        if mountstatus != 0:
                mountstatus = 1
                logging.error("force mount failed, reason:")
                logging.error(output)
        else:
                logging.info("force mount ok")
        return mountstatus

def dump_mysql(dbuser,dbpass,dbname,dbdestiny_changeme):
        global dumpstatus
        dbuser='user'
        dbpass='password'
        dbname='dbname'
        logging.info("dumping db")
        os.system ("mysqldump -u"+dbuser +" -p"+dbpass + " --single-transaction --opt " + db + dbdestiny_changeme + datetime.date.today().isoformat() + '/mysql_dump.sql')
        return dumpstatus

def rpibk():
    print "convert bash to py"
    #bprocess.call([rpifull.sh], cwd='/tmp')

def ubuntubk():
    print "not implemented"

def mybk():
        global rsyncstatus
        rsync_destination = /media/stuff
        logging.info("Rsyncing ...")
        #syncstatus=os.system("rsync -avrz " + " --files-from=" + mybk.txt + " / "+ rsync_destination) 
        return rsyncstatus

def monitor():
        global allstatus_chageme_many
        #dev_var
        bkstatus = 0
        logging.info("sending status to puppet")
        if bkstatus == 0:
                print "send all 0s to salt"
        else:
                print "send errors to salt and loggit"

#main
logging.info("Starting")
check_target()
test_connection()
if connstatus == 0:
        test_mountpoint()
        if mountstatus == 0:
                options = {"rpiquarto" : rpibk,
                        "rpisala" : rpibk,
                        "rpi256" : rpibk,
                        "mini" : mybk,
                        "master01" : ubuntubk,
                        "services01" : ubuntubk,
                        }
print me
me = "master01"
options[me]()
monitor()
logging.info("Backup ended for " + "hostname")

