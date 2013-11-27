#!/usr/bin/env python
import sys
import os
from xml.etree import ElementTree
import commands

def main():
    fd = os.popen('ls -l')
    
    s = fd.read()
    print s
    print commands.getstatusoutput('git log ^3a3ad9a84067fa89e720924092c291166b4c357b master')
    
if __name__ == '__main__':
    main()