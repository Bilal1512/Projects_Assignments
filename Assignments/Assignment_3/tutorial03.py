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


def email_domain_extract():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[0]=='id':
                continue
            email=i[3]
            domain=""
            start=0
            for j in email:
                if j=='.' and start==1:
                    break
                elif j=='@':
                    start=1;
                elif start==1:
                    domain+=j
            path=os.getcwd()+'\\'+'analytics'+'\\'+'domain'
            if not os.path.exists(path):
                os.makedirs(path)
            path+='\\'+domain+'.csv'
            if not os.path.exists(path):
                    with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
            with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(i)
    pass


def gender():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[0]=='id':
                continue
            gender_=i[4]
            gender_=gender_.lower()
            path=os.getcwd()+'\\'+'analytics'+'\\'+'gender'
            if not os.path.exists(path):
                os.makedirs(path)
            path+='\\'+gender_+'.csv'
            if not os.path.exists(path):
                    with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
            with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(i)
    pass


def dob():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[0]=='id':
                continue
            bday=i[5]
            year=bday[-4:]
            year=int(year)
            if not 1995<=year<=2020 :
                if not os.path.exists(os.getcwd()+'\\'+'analytics'+'\\'+'dob'):
                    os.makedirs(os.getcwd()+'\\'+'analytics'+'\\'+'dob')
                with open(os.getcwd() + '\\' +'analytics'+'\\'+'dob'+'\\'+'misc'+'.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(i)
            else:
                temp=int(year/5)
                start=temp*5
                end=(temp*5)+4
                if start==2020 or start==2015:
                    start=2015
                    end=2020
                if not os.path.exists(os.getcwd()+'\\'+'analytics'+'\\'+'dob'):
                    os.makedirs(os.getcwd()+'\\'+'analytics'+'\\'+'dob')
                with open(os.getcwd() + '\\' +'analytics'+'\\'+'dob'+'\\'+'bday'+'_'+str(start)+'_'+str(end)+'.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(i)
    pass



def state():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[0]=='id':
                continue
            state=i[7]
            state=state.lower()
            path=os.getcwd()+'\\'+'analytics'+'\\'+'state'
            if not os.path.exists(path):
                os.makedirs(path)
            path+='\\'+state+'.csv'
            if not os.path.exists(path):
                    with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
            with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(i)
    pass




def blood_group():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[0]=='id':
                continue
            bloodgroup=i[6]
            bloodgroup=bloodgroup.lower()
            path=os.getcwd()+'\\'+'analytics'+'\\'+'blood_group'
            if not os.path.exists(path):
                os.makedirs(path)
            path+='\\'+bloodgroup+'.csv'
            if not os.path.exists(path):
                    with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
            with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(i)
    pass


def new_file_sort():
    with open('./studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[0]=='id':
                continue
            name=i[1]
            for j in range(len(name)):
                if name[j]==' ':
                    break;
            first_name=name[:j]
            last_name=name[j+1:]
            path=os.getcwd()+'\\'+'analytics'
            if not os.path.exists(path):
                os.makedirs(path)
            path+='\\'+'studentinfo_cs384_names_split'+'.csv'
            if not os.path.exists(path):
                    with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow(['id','first_name','last_name','country','email','gender','dob','blood_group','state'])
            with open(path, 'a',newline='') as fill:
                        writer=csv.writer(fill)
                        writer.writerow([i[0],first_name,last_name,i[2],i[3],i[4],i[5],i[6],i[7]])
    with open (os.getcwd()+'\\'+'analytics'+ '\\' + 'studentinfo_cs384_names_split.csv', 'r') as file:
        reader = csv.reader(file)
        stud_list = []
        for i in reader:
            if not os.path.exists(os.getcwd()+'\\'+'analytics'+ '\\' + 'studentinfo_cs384_names_split_sorted_first_name.csv') or i[0]=='id':
                with open(os.getcwd()+'\\'+'analytics'+ '\\' + 'studentinfo_cs384_names_split_sorted_first_name.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(i)
            stud_list.append([i[1],i[2],i[0],i[3],i[4],i[5],i[6],i[7],i[8]])
        stud_list.sort()
        for student in stud_list:
            with open(os.getcwd()+'\\'+'analytics' + '\\' + 'studentinfo_cs384_names_split_sorted_first_name.csv', 'a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([student[2],student[0],student[1],student[3],student[4],student[5],student[6],student[7],student[8]])
    pass