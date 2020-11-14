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
