#!/usr/bin/python
#v1.1
# status
# 0 ok
# 1 mount error
# 2 connection error
# 3 rsync error, check log for more info
import os,logging,sys,datetime,shutil,commands
logging.basicConfig(filename='sync.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def check_target():
        global platform_changeme
        #obtain host
        return platform_changeme
        
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
        global bkstatus
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
        global mountstatus
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

def dd_rpi()
        global status
        #do
        return status

def changeme_rsync(whattobackup_changeme,destiny_changem):
        global rsyncstatus
        logging info("Rsyncing ...")
        zrsync=os.system("rsync -avrz" + " " + "") 
        return rsyncstatus

def monitor():
        global allstatus_chageme_many
        logging.info("sending status to puppet")
        if bkstatus == 0:
                #send all 0s to puppet
        else:
                #send errors to puppet log

#main
logging.info("Starting")
checktarget()
test_connection()
if connstatus == 0:
        test_mountpoint()
        if mountstatus == 0:
                #case 
                checktarget() = rpixbmc
                        dd_rpi()
                checktarget() = rpixbmc
                        dd_rpi()
                checktarget() = osx1
                        #todo
                checktarget() = vm01
                        #todo
                checktarget() = vm02
monitor()
logging.info("Backup nded for " + "hostname")
