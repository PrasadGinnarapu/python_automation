"""importing required modules  os, shutil"""
import os
import shutil
path = r'C:\Users\pg21258\Desktop\auto'
list_ = os.listdir(path)


def sortingfiles(list_):
	"""function start"""

	for file_ in list_:
		name, ext = os.path.splitext(file_)
		ext = ext[1:]
		if ext == '':
			continue
		if os.path.exists(path+'/'+ext):
			shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
		else:
			os.makedirs(path+'/'+ext)
			shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)


sortingfiles(list_)

