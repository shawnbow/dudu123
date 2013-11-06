#!/usr/bin/env python
import os
import sys
import time

if len(sys.argv) != 2:
    print 'TIP: please input branch name'
    sys.exit()

branch = sys.argv[1]

os.system('repo init -b ' + branch)
os.system('repo sync -d')
os.system('repo manifest -r -o ' + branch + '-' + time.strftime('%Y%m%d%H%M',time.localtime(time.time()))+'.xml')

