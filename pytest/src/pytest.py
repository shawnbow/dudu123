#!/usr/bin/env python
import sys
import os
from xml.etree import ElementTree

def main():
    root = ElementTree.parse('2013-07-23_pxa988-jb4.2_beta2.xml').getroot()
    #iters = root.iter("project")
    print root[3].text.join('123')
    print '-'.join((x*2 for x in ('fuck1','fuck')))
    
    if (''):
        print {}, (''), [], {1,2,3}
        
    print os.path.join(os.path.dirname(__file__),'ff')
    
    
if __name__ == '__main__':
    main()