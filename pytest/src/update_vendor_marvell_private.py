#!/usr/bin/env python
import os

extra_projects = \
    ['vendor/marvell/private/android-builder',
     'vendor/marvell/private/customer-config',
     'vendor/marvell/private/deployconf',
     'vendor/marvell/private/metaconfig',
     'vendor/marvell/private/mkupdate',
     'vendor/marvell/private/mlsdk',
     'vendor/marvell/private/product-release'
    ]

prefix_url = 'http://sh2-git01.marvell.com/git/'

os.system('mkdir -p vendor/marvell/private')

for project in extra_projects:
    if os.path.exists(project+'/.git'):
        os.system('cd ' + project + ';' + 'git pull --rebase')
    else:
        os.system('git clone ' + prefix_url + project + ' ' + project)
# 
# 
# pdir = os.popen('find . -name .git')
# print pdir
# for str in pdir:
#     str = str.replace('.git\n', '')
#     os.system('cd ' + str + ';' + 'git pull --rebase')
