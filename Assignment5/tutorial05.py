import re
import os
import csv

def rename_FIR(folder_name):
	    # rename Logic 
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			extension = (re.split(r'\.',filename)[-1]).strip()
			all_num = re.findall(r'\d+',filename)
			episode_number = all_num[0]
			if(int(episode_number_padding)>len(episode_number)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number))+ episode_number
			path =os.path.join(os.getcwd(),path)        
			os.chdir(path)
			os.rename(filename,'FIR -' + ' Episode ' + episode_number+ '.' + extension) 
		except:
			os.remove(filename)  
