# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

import read
read.do_read()

#import logging
#logger = logging.getLogger()
#loger.setLevel(logging.DEBUG)

#ch = logging.StreamHandler()
#ch.setLevel(loggingINFO)
#logger.addHandler(ch)

#fh = logging.FileHandler('myLog.log')
#fh.setLevel(logging.DEBUG)
#logger.addHandler(fh)
