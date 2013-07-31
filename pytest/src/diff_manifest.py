#!/usr/bin/python
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


def main():
    if len(sys.argv) != 3:
        print 'Please input 2 xml file path!!'
        sys.exit()
        return
    else:
        try:
            project_dict_new, name_set_new = read_xml(sys.argv[1])
            project_dict_old, name_set_old = read_xml(sys.argv[2])
        except:
            print 'Error when parse xml!'
            sys.exit()
            return
    name_set_only_new = name_set_new.difference(name_set_old)
    name_set_only_old = name_set_old.difference(name_set_new)
    name_set_both = name_set_new.intersection(name_set_old)
    
    for name in name_set_both:
        if project_dict_new[name][1] != project_dict_old[name][1]:
            print 'project', project_dict_new[name][0],'-', project_dict_new[name][1]
    
    for name in name_set_only_new:
        print '+', 'project', project_dict_new[name][0], '-', project_dict_new[name][1]
    
    for name in name_set_only_old:
        print '-', 'project', project_dict_old[name][0], '-', project_dict_old[name][1]

if __name__ == '__main__':
    main() 