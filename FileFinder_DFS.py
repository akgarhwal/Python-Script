#Do not search for files that start with '.'
#using DFS

import os
import sys
import time
ispy3 = sys.version[0] == '3'


def DFS( root,tr,ind,level):
	#print("\033[1;32;40m",ind+'>'+root)
	try :
		file = os.listdir(root)
	except :
		print("We Don't have permission to access : ",root)
	else:
		len = (file.__len__())
		for i in range(0,len):

			if(file[i][0]!='.'):
				Entry =root+'/'+file[i]

				if((os.path.isdir(Entry))):
					if(file[i].find(ext)!=-1):
						print("\033[0;45;40m",level,tr+'\t'+file[i])
					DFS(Entry,(tr+'\t'),ind+'--------',level+1)
				else:
					if(file[i].find(ext)!=-1):
						print("\033[0;45;40m",level,tr+'\t'+file[i])
						#print(level,tr+'\t'+file[i])

root = os.getcwd()
print("Default Root Folder : ",root,"\nEnter root folder path[Enter for Skip] : ")
if ispy3:
	temp = input()
else:
	temp = raw_input()

if(temp.__len__()>0):
	root=temp

print("Enter Name/Extension of File : ")
ext =''
if ispy3:
	ext = input()
else:
	ext = raw_input()

start = time.time()
ind=''
print("Start Scanning....\n")

DFS(root,'',ind,0)

print("FINISHED.\nTotal Time : ",time.time()-start)
