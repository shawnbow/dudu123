#!/usr/bin/env python
import os
import sys
from xml.etree import ElementTree

def read_xml(xmlfile = ''):
    project_dict = dict()
    name_set = set()
    tree = ElementTree.parse(xmlfile)
    root = tree.getroot()

    projects = root.iter("project")
    for p in projects:
        project_dict[p.attrib['name']] = (p.attrib.get('path',p.attrib['name']), p.attrib['revision'])
        name_set.add(p.attrib['name'])
    return project_dict, name_set

#def apply_rebase(rebase_list):
#    os.system('cd ' + project + ';' + 'git pull --rebase').

def main():
    if len(sys.argv) != 3:
        print 'TIP: please input rebase-to and rebase-from manifest xml files'
        sys.exit()
        return
    else:
        try:
            project_dict_new, name_set_new = read_xml(sys.argv[1])
            project_dict_old, name_set_old = read_xml(sys.argv[2])
        except:
            print 'Error: bad xml files!'
            sys.exit()
            return
    name_set_only_new = name_set_new.difference(name_set_old)
    name_set_only_old = name_set_old.difference(name_set_new)
    name_set_both = name_set_new.intersection(name_set_old)
    
    #rebase_project_list = list()
    
    for name in name_set_both:
        if project_dict_new[name][1] != project_dict_old[name][1]:
            print 'project', project_dict_new[name][0]
            print 'git checkout -b myrebase'
            print 'git rebase --onto ' + project_dict_new[name][1] + ' ' + project_dict_old[name][1] + ' ' + 'myrebase'
            print 'git push -f aosp myrebase:marvell-android-4.3-ot-dev' 
            #rebase_project_list.append((project_dict_new[name][0], project_dict_new[name][1], project_dict_old[name][1]) )
    
    for name in name_set_only_new:
        print '+', 'project', project_dict_new[name][0], '-', project_dict_new[name][1]
    
    for name in name_set_only_old:
        print '-', 'project', project_dict_old[name][0], '-', project_dict_old[name][1]

if __name__ == '__main__':
    main() 