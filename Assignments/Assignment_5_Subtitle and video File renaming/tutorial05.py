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

def rename_Game_of_Thrones(folder_name):
	    # rename Logic  
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			info = filename.split('-')
			season_number=re.findall(r'\d+',info[1])[0]
			episode_number=re.findall(r'\d+',info[1])[1]
			extension = (re.split(r'\.',filename)[-1]).strip()
			name = (re.split(r'\.',info[2])[0]).strip()
			if(len(season_number) < int(season_number_padding)):
				season_number = '0'*(int(season_number_padding)-len(season_number)) + season_number
			if(len(episode_number) < int(episode_number_padding)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number)) + episode_number
			path=os.path.join(os.getcwd(),path)      
			os.chdir(path)
			os.rename(filename,'Game of Thrones - Season '+ season_number +' Episode ' + episode_number + ' - ' + name + '.' + extension)  
		except:
			os.remove(filename)  

def rename_How_I_Met_Your_Mother(folder_name):
        # rename Logic  
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			info = filename.split('-')
			season_number=re.findall(r'\d+',info[1])[0]
			episode_number=re.findall(r'\d+',info[1])[1]
			extension = (re.split(r'\.',filename)[-1]).strip()
			name = (re.split(r'\.',info[2])[0]).strip()
			if(len(season_number) < int(season_number_padding)):
				season_number = '0'*(int(season_number_padding)-len(season_number)) + season_number
			if(len(episode_number) < int(episode_number_padding)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number)) + episode_number
			path=os.path.join(os.getcwd(),path)      
			os.chdir(path)
			os.rename(filename,'How I Met Your Mother - Season '+ season_number + ' Episode ' + episode_number + ' - ' + name + '.' + extension) 
		except:
			os.remove(filename)

def rename_Sherlock(folder_name):
    	# rename Logic  
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			info = filename.split('.')
			lis=re.findall(r'\d+',info[1])
			if len(lis) is 1:               			
			    season_number=lis[0]
			    episode_number=re.findall(r'\d+',info[2])[0]
			else:
				season_number=lis[0]
				episode_number=lis[1]
			extension = (re.split(r'\.',filename)[-1]).strip()
			if(len(season_number) < int(season_number_padding)):
				season_number = '0'*(int(season_number_padding)-len(season_number)) + season_number
			if(len(episode_number) < int(episode_number_padding)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number)) + episode_number
			path=os.path.join(os.getcwd(),path)      
			os.chdir(path)
			os.rename(filename,'Sherlock - Season '+ season_number +' Episode ' + episode_number + '.' + extension)  
		except:
			os.remove(filename)

def rename_Suits(folder_name):
        #rename logic
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			info = filename.split('-')
			season_number=re.findall(r'\d+',info[1])[0]
			episode_number=re.findall(r'\d+',info[1])[1]
			extension = (re.split(r'\.',filename)[-1]).strip()
			name = (re.split(r'\.',info[2])[0]).strip()
			if(len(season_number) < int(season_number_padding)):
				season_number = '0'*(int(season_number_padding)-len(season_number)) + season_number
			if(len(episode_number) < int(episode_number_padding)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number)) + episode_number
			path=os.path.join(os.getcwd(),path)      
			os.chdir(path)
			os.rename(filename,'Suits - Season '+ season_number+ ' Episode ' + episode_number+ ' - ' + name + '.' + extension)    
		except:
			os.remove(filename)    


#input
web_series_name = int(input("Enter the number corresponding to the title of web series :\n1.FIR\n2.Game of Thrones\n3.How I Met Your Mother\n4.Sherlock\n5.Suits\nEnter a number corresponding to season:\n"))
season_number_padding = input("Enter season number padding - ")
episode_number_padding = input("Enter episode number padding - ")
season_dict = {1:'FIR',2:'Game of Thrones',3:'How I Met Your Mother',4:'Sherlock',5:'Suits'}
if web_series_name == 1:
	rename_FIR(season_dict[1])
elif web_series_name == 2:
	rename_Game_of_Thrones(season_dict[2])
elif web_series_name == 3:
	rename_How_I_Met_Your_Mother(season_dict[3])
elif web_series_name == 4:
	rename_Sherlock(season_dict[4])
elif web_series_name == 5:
	rename_Suits(season_dict[5])