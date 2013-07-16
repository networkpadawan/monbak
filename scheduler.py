#!/usr/bin/python
import logging,os,salt.client
logging.basicConfig(filename='test.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


import salt.client
client = salt.client.LocalClient()

logging.info("trying storage ip")
call = client.cmd('rpi256', ['cmd.script salt://scripts/bak.py']
logging.info("endedrpi256")
logging.info("started rpiquarto")
call = client.cmd('rpiquarto', ['cmd.script salt://scripts/bak.py']
logging.info("ended rpiquatro")
