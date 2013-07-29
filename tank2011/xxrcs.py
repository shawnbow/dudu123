#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import glob

def write_cfg(p,dic):
	if isinstance(dic,dict) == False:
		raise TypeError,"not a dict"

	f = open(p,"wb+")
	s = str(dic)
	f.write(s)
	f.close()

def read_cfg(p):
	f = open(p,"rb")
	txt = "".join(f.readlines())
	f.close()
	dic = eval(txt)
	
	if isinstance(dic,dict) == False:
		raise TypeError,"not a dict"
	return dic


#~ files[0].find(".py")
#~ files[1].find(".py")

def pop_all():
	"""通过配置文件，获取所有项目"""
	dic = read_cfg("xxrcs.cfg")
	for item in dic["files"]:
		cmd = "co -l " + item
		os.system(cmd)
	
	pass
	
	
def get_files():
	p = os.getcwd()
	files = glob.glob(p + os.path.sep + "*")
	for f  in files:
		if os.path.isdir(f):
			files.remove(f)
			continue
	return files
	
def push_all():
	"""将当前文件夹中的所有文件都写到配置中"""	
	p = os.getcwd()
#	r,d,f = os.walk(p)
	tmp_files = get_files()
	files = []
	
#	print tmp_files
	
	for f in tmp_files:
		if f.find("xxrcs.py") != -1 or f.find("xxrcs.cfg") != -1 or f.find("pyc") != -1:
			tmp_files.remove(f)
			continue
#		print p+"/"+f
		files.append(f)
	dic = {"files":files}
	write_cfg("xxrcs.cfg",dic)
	print dic
	
	cmd = ""
	for f in files:
		cmd = "ci " + f
		
		print cmd
		os.system(cmd)
	

def menu(i=None):
	if platform.system() != "Windows":
		os.system("clear")
	else:
		os.system("cls")

	print "请选择要执行的操作:"
	print "1.将文件写入rcs"
	print "2.将文件从rcs取出"
	
	return [1,2]
		
		
def main():
	menu_id = menu()

	funcs = (push_all,pop_all)

	done = False

	while not done:
		select_id = int(raw_input("请输入序号:"))
		if select_id not in menu_id:
			continue
	#		funcs = (push_all,pop_all)
		else:
			funcs[select_id-1]()
			done = True	

	return 0

if __name__ == '__main__':
	main()
