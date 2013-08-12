#!/usr/bin/env python
import sys
import test_module2
#from pytest import g_pytest

def func1():
    sys.modules['__main__'].g_pytest = 'test_module1'

print 'fasdfasdfasdfasd'
sys.exit()