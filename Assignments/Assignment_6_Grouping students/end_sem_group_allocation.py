import csv
import re
import os
import operator
import shutil

def group_allocation(filename, number_of_groups):
    if os.path.exists(os.getcwd() + '\\Groups'):
        shutil.rmtree(os.getcwd() + '\\Groups')
    #task1
    with open ('./'+filename,'r') as file:
        students=csv.reader(file)
        branch_strength={}
        list_of_list=[]
        for student in students:
            if student[0]=='Roll':
                continue
            if student[0][4:6] in branch_strength:
                branch_strength[student[0][4:6]]+=1
            else:
                branch_strength[student[0][4:6]]=1
            list_of_list.append(student)
        branch_strength = dict( sorted(branch_strength.items(), key=operator.itemgetter(1),reverse=True))
        path=os.getcwd()+'\\'+'Groups'
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path+'\\'+'branch_strength.csv','a',newline='') as mwrite:
            writer=csv.writer(mwrite)
            writer.writerow(['BRANCH_CODE','STRENGTH'])
        for branch_code in branch_strength:
                with open(path+'\\'+'branch_strength.csv','a',newline='') as mwrite:
                    writer=csv.writer(mwrite)
                    writer.writerow([branch_code,branch_strength[branch_code]])
    #task2
    list_of_list.sort()
    for student in list_of_list:
        if not os.path.exists(os.getcwd()+'\\'+'Groups'+'\\'+student[0][4:6]+'.csv'):
            with open(os.getcwd()+'\\'+'Groups'+'\\'+student[0][4:6]+'.csv','a',newline='') as mwrite:
                writer=csv.writer(mwrite)
                writer.writerow(['Roll','Name','Email'])
        with open(os.getcwd()+'\\'+'Groups'+'\\'+student[0][4:6]+'.csv','a',newline='') as mwrite:
                writer=csv.writer(mwrite)
                writer.writerow(student)
    #task3
    count_matrix={}
    left_out={}
    for branch in branch_strength:
        a1=branch_strength[branch]//number_of_groups
        a2=branch_strength[branch]%number_of_groups
        left_out[branch]=a2
        temp_list=[a1]*number_of_groups
        count_matrix[branch]=temp_list
    curr_group=1
    for key in left_out:
        while(left_out[key]>0):
            count_matrix[key][curr_group-1]+= 1
            curr_group = (curr_group + 1)%number_of_groups
            if(curr_group == 0):
                curr_group=number_of_groups
            left_out[key]-= 1
    for branch in branch_strength:
        with open(os.getcwd()+'\\'+'Groups'+'\\'+branch+'.csv','r') as rfile:
            students_branchwise=csv.reader(rfile)
            curr_group=1
            count=0
            header = next(students_branchwise)
            for z in range(branch_strength[branch]):
                if count==count_matrix[branch][curr_group-1]:
                    count=0
                    curr_group=curr_group+1
                if count_matrix[branch][curr_group-1] == 0:
                    continue
                str_group=str(curr_group)
                if len(str_group)==1:
                    str_group='0'+str_group
                if not os.path.exists(os.getcwd()+'\\'+'Groups'+'\\'+'Group_G'+str_group+'.csv'):
                    with open(os.getcwd()+'\\'+'Groups'+'\\'+'Group_G'+str_group+'.csv','a',newline='') as mwrite:
                        writer=csv.writer(mwrite)
                        writer.writerow(['Roll','Name','Email'])
                with open(os.getcwd()+'\\'+'Groups'+'\\'+'Group_G'+str_group+'.csv','a',newline='') as mwrite:
                    writer=csv.writer(mwrite)
                    writer.writerow(next(students_branchwise))
                count+=1
    #task4
    with open(os.getcwd()+'\\'+'Groups'+'\\'+'stats_grouping.csv','a',newline='') as mwrite:
        writer=csv.writer(mwrite)
        writer.writerow(['group','total','EE','ME','CS','CE','CB','MM'])
        for i in range(1,number_of_groups+1):
            group=str(i)
            if(len(group)==1):
                group='0'+group
            total=0
            templist=[]
            for key in count_matrix:
                total+=count_matrix[key][i-1]
                templist.append(count_matrix[key][i-1])
            writer.writerow(['Group_G'+group,total]+templist)

filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)