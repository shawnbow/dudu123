import test_module1
import test_module2
import sys

g_pytest = 1

def main():
    print g_pytest
    
    test_module1.func1()
    
    print g_pytest
    
    test_module2.func2()
    
    print g_pytest

if __name__ == '__main__':
    main()
    print sys.modules