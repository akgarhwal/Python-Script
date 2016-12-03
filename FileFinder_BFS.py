import os
import sys
import time

#import Queue acc to pyhton version

def main():
	start = time.time()

	ispy3 = sys.version[0] == '3'

	if ispy3:
	    import queue as queue
	else:
	    import Queue as queue

	#root = '/home/akgarhwal/LPU'
	root = os.getcwd()
	print("Default Root Folder : ",root,"\nEnter root folder path[Enter for Skip] : ")
	temp = input()

	if(temp.__len__()>0):
		root=temp
	path=''
	q=queue.Queue(maxsize=0)
	q.put(root)

	print("Enter Name/Extension of File : ")
	ext =''
	if ispy3:
		ext = input()
	else:
		ext = raw_input()
	LEN = ext.__len__()

	print("START SCANNING...\n")

	while((q.empty())==False):
		path = q.get()
		#print(path)
		file = os.listdir(path)
		len = (file.__len__())
		for i in range(0,len):

			if(file[i][0]!='.'):
				Entry =path+'/'+file[i]

				if(file[i].find(ext)!=-1):
						print(Entry)

				if((os.path.isdir(Entry))):
					#print('  '+file[i])
					q.put(Entry)
				#else:
				#	if(file[i].find(ext)!=-1):
				#		print('\t\t'+file[i])

	print("FINISHED.\nTotal Time : ",time.time()-start)


main()