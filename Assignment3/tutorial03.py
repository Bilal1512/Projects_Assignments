import csv
import os
import shutil

def valid_roll(roll_number):
    for i in range(0,4):
        if not 48<=ord(roll_number[i])<=57:
            return False
    for i in range(4,6):
        if not 97<=ord(roll_number[i])<=122:
            return False
    for i in range(6,8):
        if not 48<=ord(roll_number[i])<=57:
            return False
    return True

def del_create_analytics_folder():
    path=os.getcwd()+'\\'+'analytics'
    if os.path.exists(path):
        shutil.rmtree(path)

def course():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            roll_number=i[0];
            roll_number=roll_number.lower()
            if valid_roll(roll_number):
                year=roll_number[0:2]
                branch_code=roll_number[4:6]
                degree=roll_number[2:4]
                if degree=='01':
                    degree='btec'
                elif degree=='11':
                    degree='mtec'
                elif degree=='12':
                    degree='msc'
                elif degree=='21':
                    degree='phd'
                path=os.getcwd()+'\\'+'analytics'+'\\'+'course'+'\\'+branch_code+'\\'+degree
                if not os.path.exists(path):
                    os.makedirs(path)
                if not os.path.exists(path+'\\'+year+'_'+branch_code+'_'+degree+'.csv'):
                    with open(path+'\\'+year+'_'+branch_code+'_'+degree+'.csv', 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
                with open(path+'\\'+year+'_'+branch_code+'_'+degree+'.csv', 'a',newline='') as fill:
                    writer=csv.writer(fill)
                    writer.writerow(i)
            else:
                if not os.path.exists(os.getcwd()+'\\'+'analytics'+'\\'+'course'):
                    os.makedirs(os.getcwd()+'\\'+'analytics'+'\\'+'course')
                with open(os.getcwd() + '\\' +'analytics'+'\\'+'course'+'\\'+'misc'+'.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(i)
    pass

def country():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[0]=='id':
                continue
            country_name=i[2]
            path=os.getcwd()+'\\'+'analytics'+'\\'+'country'
            if not os.path.exists(path):
                os.makedirs(path)
            path+='\\'+country_name+'.csv'
            if not os.path.exists(path):
                    with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
            with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(i)
    pass