'''
 * File: main.py
 * Date: 12-02-27
 *
 * Desc: entry-point
 *
 * Author: H. N. Skjevling
'''

import TheWorld
from Entities.Actors import Person
from Entities.Actors import Bear
from Entities import Items, Resources
import time
#import sys
import traceback
import datetime

try:
  subject1 = Person("Jon Ole")
  subject2 = Person("Fredrik")
  subject3 = Bear()
  entries = [subject1, subject2, subject3]
  man = TheWorld.MainMan(entries)

  Resources.initResourceMap()
  Items.initItemMap()

  t0 = time.localtime()
  elapsed = time.localtime()
  startTime = time.mktime(t0)
  clockLoopTimer = 0.000000
  totalTime = 0.0

  while(True):
    localSeconds = time.mktime(time.localtime())

    #totalTime = localSeconds - time.mktime(t0)
    elapsed = localSeconds - startTime
    startTime = localSeconds
    totalTime += elapsed
    clockLoopTimer += elapsed

    if(elapsed > 0.003):
      man.update(elapsed)

      if(clockLoopTimer >= 10.0):
        print "\nTime is now", time.strftime("%H:%M:%S")
        print "Simulation running since", time.strftime("%H:%M:%S", t0), "(", totalTime, "seconds )\n"
        clockLoopTimer = 0
      elapsed = 0

except Exception, ex:
  #print 'Exception caught:', sys.exc_info()[0], ':\n', ex
  print traceback.print_exc()