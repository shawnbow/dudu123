import os
import shutil

os.chdir('/home/shawn/android/src/vendor')

pdir = os.popen('find . -name .git')
print pdir
for str in pdir:
    str = str.replace('.git\n', '')
    os.system('cd ' + str + ';' + 'git pull --rebase')
