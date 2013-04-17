#!/usr/bin/python
#v1.1
# zabbix status
# 0 ok
# 1 mount error
# 2 connection error
# 3 rsync error, check log for more info
import os,logging,sys,datetime,shutil,commands
logging.basicConfig(filename='sync.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def test_connection():
        global zstatus
        logging.info("trying storage ips")
        for testip in open('storageips.txt', 'r'):
                conn = os.system("ping -c 1 -W 1 " + testip)
                if conn == 0:
                        zstatus = 0;
                else:
                        logging.error("connection error: %s is unreachable" %(testip.rstrip('\n')))
                        zstatus = 2;
        return zstatus

def test_mountpoint():
        global zstatus
        logging.info("checking mountpoints")
        for path in open('mountpoints.txt', 'r'):
                mount=os.path.ismount(path.rstrip('\n'))
                if mount == True:
                        zstatus = 0
                else:
                        logging.error("mountpoint %s is unmounted, trying to force mount" %(path.rstrip('\n')))
                        zstatus = force_mount()
        return zstatus

def force_mount():
        global zstatus, mountlog
        status, output = commands.getstatusoutput("mount -a")
        zstatus = os.system ("mount -a")
        if zstatus != 0:
                zstatus = 1
                logging.error("force mount failed, reason:")
                logging.error(output)
        else:
                logging.info("force mount ok")
        return zstatus

def backup_bacula():
        global zbacula
        dbuser='root'
        dbpass='atwork@pass'
        db='bacula'
        logging.info("sending status to zabbix")
        shutil.copytree('/var/lib/bacula/', '/media/remotenfs/BACULA/DAILY_BSRS/' + datetime.date.today().isoformat() + '/', ignore = shutil.ignore_patterns('*.sql','*.mail','*.state'))
        logging.info("dumping db")
        os.system ("mysqldump -u"+dbuser +" -p"+dbpass + " --single-transaction --opt " + db +  '> /media/remotenfs/BACULA/DAILY_BSRS/' + datetime.date.today().isoformat() + '/bacula_mysql_dump.sql')
        logging.info("syncing bacula config files")
        zbacula=os.system("rsync -avrz /etc/bacula/ /media/remotenfs/BACULA/CONFIGS/synced/")
        compare = datetime.date.today()
        if compare.weekday() == 6:
                logging.info("sunday, making separate copy of config files")
                os.system('rsync -avrz /media/remotenfs/BACULA/CONFIGS/synced /media/remotenfs/BACULA/CONFIGS/copied')
        return zbacula

def backup_volumes():
        global zrsync
        logging.info("syncing bacula volumes")
        zrsync=os.system("rsync -avrz /media/Backups/VOLUMES/ /media/remotenfs/BACULA/VOLUMES/")
        return zrsync

def monitor():
        global zbacula,zrsync,zstatus
        logging.info("sending status to zabbix")
        if zstatus == 0:
                os.system("/usr/bin/zabbix_sender -z 172.22.6.164 -s CLOUD-GLOBAL -o " + str(zrsync) + " -k vols.rsync")
                os.system("/usr/bin/zabbix_sender -z 172.22.6.164 -s CLOUD-GLOBAL -o " + str(zbacula) + " -k bsrs.rsync")
        else:
                os.system("/usr/bin/zabbix_sender -z 172.22.6.164 -s CLOUD-GLOBAL -o " + str(zstatus) + " -k vols.rsync")
                os.system("/usr/bin/zabbix_sender -z 172.22.6.164 -s CLOUD-GLOBAL -o " + str(zstatus) + " -k bsrs.rsync")

#main
logging.info("Starting Program")
test_connection()
test_mountpoint()
if zstatus == 0:
        test_mountpoint()
        if zstatus == 0:
                backup_bacula()
                if zbacula == 0:
                        backup_volumes()
monitor()
logging.info("Ending Program")
