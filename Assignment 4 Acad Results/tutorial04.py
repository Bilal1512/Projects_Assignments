import csv
import os
import re
import shutil
numeric_grade={"AA": 10,"AB": 9,"BB": 8,"BC": 7,"CC": 6,"CD": 5,"DD": 4,"F": 0,"I": 0}
#for deleting the pre-existing folder "grade"
if(os.path.exists(os.getcwd()+'\\'+'grades')):
    shutil.rmtree(os.getcwd()+'\\'+'grades')
os.makedirs(os.getcwd()+'\\'+'grades')
#handling misc data
roll_pattern=re.compile(r'[0-9]{4}[A-Za-z]{2}[0-9]{2}')
not_valid={}
with open('./acad_res_stud_grades.csv','r') as file:
    reader= csv.reader(file)
    for row in reader:
        if row[0]=='sl':
                    continue
        if not row[6] in numeric_grade or not int(row[5])>0 or not re.fullmatch(roll_pattern,row[1]):
            if not row[1] in not_valid:
                with open(os.getcwd()+'\\'+'grades'+'\\'+'misc.csv','a',newline='') as mwrite:
                    writer=csv.writer(mwrite)
                    writer.writerow(['Roll: '+row[1]])
                    writer.writerow(['Semester wise details'])
                    writer.writerow(['Subject','Credits','Type','Grade','Sem'])
                    writer.writerow([row[4],row[5],row[8],row[6],row[2]])
                    not_valid[row[1]]=True
            else:
                with open(os.getcwd()+'\\'+'grades'+'\\'+'misc.csv','a',newline='') as mwrite:
                    writer=csv.writer(mwrite)
                    writer.writerow([row[4],row[5],row[8],row[6],row[2]])

def creating_overall_file(total_sem,credits_per_sem,obtained_weightage_per_sem,credits_not_cleared_per_sem,curr_student):
    with open(os.getcwd()+'\\'+'grades'+'\\'+curr_student+'_'+'overall.csv','a',newline='') as append:
                    writer=csv.writer(append)
                    writer.writerow(['Roll: '+curr_student])
                    writer.writerow(['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI'])
                    total_credits=0
                    total_cleared_credits=0
                    cpi=0
                    for sem in range(1,total_sem+1):
                        if credits_per_sem[sem-1]!=0:
                            spi=obtained_weightage_per_sem[sem-1]/credits_per_sem[sem-1]
                        if total_credits+credits_per_sem[sem-1]!=0:
                            cpi=((cpi*total_credits)+(spi*credits_per_sem[sem-1]))/(total_credits+credits_per_sem[sem-1])
                        total_credits+=credits_per_sem[sem-1]
                        total_cleared_credits+=(credits_per_sem[sem-1]-credits_not_cleared_per_sem[sem-1])
                        if credits_per_sem[sem-1]!=0:
                            writer.writerow([sem,credits_per_sem[sem-1],credits_per_sem[sem-1],round(spi,2),total_credits,total_cleared_credits,round(cpi,2)])

with open('acad_res_stud_grades.csv','r') as file:
    reader= csv.reader(file)
    curr_student=''
    credits_per_sem=[0]*10
    obtained_weightage_per_sem=[0]*10 #summation of credits*grade
    credits_not_cleared_per_sem=[0]*10
    total_sem=0 
    for row in reader:
        if row[1] in not_valid or row[0]=='sl':
            continue
        if row[1]==curr_student:
            credits_per_sem[int(row[2])-1]+=int(row[5])
            obtained_weightage_per_sem[int(row[2])-1]+=numeric_grade[row[6]]*int(row[5])
            if numeric_grade[row[6]]==0:
                credits_not_cleared_per_sem[int(row[2])-1]+=int(row[5])
            total_sem=max(total_sem,int(row[2]))
            path=os.getcwd()+'\\'+'grades'
            with open(path+'\\'+curr_student+'_'+'individual.csv','a',newline='') as append:
                writer=csv.writer(append)
                writer.writerow([row[4],row[5],row[8],row[6],row[2]])
        else:
            if not curr_student=='':
                creating_overall_file(total_sem,credits_per_sem,obtained_weightage_per_sem,credits_not_cleared_per_sem,curr_student)
            #for new student set them to default
            curr_student=row[1]
            total_sem=0 
            credits_per_sem=[0]*10
            obtained_weightage_per_sem=[0]*10 #summation of (credits*grade)
            credits_not_cleared_per_sem=[0]*10 
            credits_per_sem[int(row[2])-1]+=int(row[5])
            obtained_weightage_per_sem[int(row[2])-1]+=numeric_grade[row[6]]*int(row[5])
            if numeric_grade[row[6]]==0:
                credits_not_cleared_per_sem[int(row[2])-1]+=int(row[5])
            total_sem=max(total_sem,int(row[2]))
            path=os.getcwd()+'\\'+'grades'
            with open(path+'\\'+curr_student+'_'+'individual.csv','a',newline='') as append:
                writer=csv.writer(append)
                writer.writerow(['Roll: '+curr_student])
                writer.writerow(['Semester wise details'])
                writer.writerow(['Subject','Credits','Type','Grade','Sem'])
                writer.writerow([row[4],row[5],row[8],row[6],row[2]])
    creating_overall_file(total_sem,credits_per_sem,obtained_weightage_per_sem,credits_not_cleared_per_sem,curr_student)