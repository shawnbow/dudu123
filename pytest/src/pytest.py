#!/usr/bin/env python
import sys
import os
from xml.etree import ElementTree
import commands

def main():
    fd = os.popen('ls -l')
    
    s = fd.read()
    print s
    print commands.getstatusoutput('git show')
    
if __name__ == '__main__':
    main()