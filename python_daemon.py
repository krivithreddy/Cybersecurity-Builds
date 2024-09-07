#!/usr/bin/python3
import datetime
import time
import traceback
debug = False
count = 1
while True:
    try:
        the_time = datetime.datetime.utcnow()
        log_entry = "The time is %s, coint is %d\n"%(the_time,count)
        f = open('/var/log/python_daemon.log','a')
        f.write(log_entry)
        f.close()
        if debug:
            print(log_entry)
        count += 1
        time.sleep(5)
    except:
        error_time = datetime.datetime.utcnow()
        g = open('/var/log/python_daemon_error.log','a')
        g.write('--------------------------\n')
        g.write(str(error_time)+'\n')
        g.write(traceback.format_exc()+'\n')
        g.close()
        time.sleep(60)
