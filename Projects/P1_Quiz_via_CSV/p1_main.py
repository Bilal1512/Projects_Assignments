import sqlite3
import os
import csv
import time
import sys
import threading
import keyboard
from threading import *


responses = {1:"q1",
            2:"q2",
            3:"q3"   
        }

t = -1
conn=sqlite3.connect("Project1_Quiz_cs384.db")
c=conn.cursor()
#basic structure of database
c.execute(
'''
CREATE TABLE IF NOT EXISTS Project1_registration(
name VARCHAR(20) NOT NULL,
roll_number VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL,
whatsapp_num INT NOT NULL);
'''
)

c.execute(
'''
CREATE TABLE IF NOT EXISTS Project1_marks(
roll_num VARCHAR(20) NOT NULL,
quiz_num INT NOT NULL,
total_marks INT NOT NULL);
'''
)

conn.commit()


def countdown(): 
    global t
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('\nTime Up!! Your responses have been saved \nEnter any valid key to exit')
def register():
    found=0
    print('\n'*4+'*'*25+'REGISTRATION PORTAL'+'*'*25)
    while found==0:
        roll_number=input("Please enter your roll number: ")
        find_user=("SELECT * FROM Project1_registration WHERE roll_number=?")
        c.execute(find_user,[(roll_number)])
        if c.fetchall():
            print("Your account is already exists please log in")
            return
        else:
            found=1
    name=input("Please enter your name: ")
    password=input("Please enter your password: ")
    whatsapp_num=input("Please enter your whatsapp number: ")
    insertData='''INSERT INTO Project1_registration(name,roll_number,password,whatsapp_num)
    VALUES(?,?,?,?)'''
    c.execute(insertData,[(name),(roll_number),(password),(whatsapp_num)])
    conn.commit()

def login():
    while True:
        print('\n'*4+'*'*25+'LOGIN PORTAL'+'*'*25)
        username=input("Please enter your username: ")
        password=input("Please enter your password: ")
        find_user=("SELECT * FROM Project1_registration WHERE roll_number=? AND password=?")
        c.execute(find_user,[(username),(password)])
        results=c.fetchall()
        if results:
            for i in results:
                  multi_quiz([i[0],i[1],i[2],i[3]])
                  return
        else:
            print("username or password incorrect,try again")
            
def quiz(info):
    global t
    print('\n'*4+'*'*25+'WELCOME'+'*'*25)
    quiz_num=input("please choose a quiz which you want to attempt(Please enter quiz number) \n1.Quiz1\n2.Quiz2\n3.Quiz3\n")
    path=os.getcwd()+'\\'+'quiz_wise_questions'
    curpath = os.getcwd()
    os.chdir(path)
    filename = responses[int(quiz_num)] + '.csv'
    f = open(filename, 'r')
    with f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'ques_no':
                temp = row[10]
                t = temp[5:-1]
    os.chdir(curpath)
    t = int(t)
    t1 = Thread(target = countdown)
    t1.start()
    response=[]
    correct_questions=0
    attempted_questions=0
    total_marks_obtained=0
    wrong_choices=0
    unattempted=[1,2,3,4,5,6,7,8,9,10]
    print('\n'*4+'*'*25+'QUIZ STARTS'+'*'*25)
    with open(path+'\\'+'q'+quiz_num+'.csv','r') as file:
        questions=csv.reader(file)
        for question in questions:
            if t == 0:
                break
            if question[0]=='ques_no':
                continue
            print("Question"+question[0]+": "+question[1])
            print("Option "+'1'+") "+question[2])
            print("Option "+'2'+") "+question[3])
            print("Option "+'3'+") "+question[4])
            print("Option "+'4'+") "+question[5])
            print("Credits if correct option: "+question[7])
            print("Negative Marking: "+question[8])
            print("Is compulsory: "+question[9])
            print("Timer: "+str(t)+'\n'+"Roll Number: "+info[1]+'\n'+"Name: "+info[0]+'\n')
            valid_response=['1','2','3','4','S','s']
            while True:
                choice=input("\nEnter Choice 1, 2, 3, 4, S(S is to skip question): \n")
                if choice in valid_response:
                    break
                else:
                    print("please enter valid choice")
            if t == 0:
                break
            #keyboard.add_hotkey("ctrl+alt+U", lambda : print("Unattempted Questions are:",unattempted))
            response.append(choice)
            if choice.lower()=='s':
                if question[9].lower()=='y':
                    total_marks_obtained+=int(question[8])
            else:
                unattempted.remove(int(question[0]))
                attempted_questions+=1
                if question[6]==choice:
                    correct_questions+=1
                    total_marks_obtained+=int(question[7])
                else:
                    wrong_choices+=1
                    total_marks_obtained+=int(question[8])
            print('\n'*2)
    total_marks=0
    with open(path+'\\'+'q'+quiz_num+'.csv','r') as file:
        questions=csv.reader(file)
        for question in questions:
            if question[0]=='ques_no':
                continue
            if int(question[0]) in unattempted and question[9].lower()=='y':
                total_marks_obtained+=int(question[8])
            total_marks+=int(question[7])
    with open(path+'\\'+'q'+quiz_num+'.csv','r') as file:
        questions=csv.reader(file)
        itr=0
        response=response+['s']*(10-len(response))
        for question in questions:
            with open(os.getcwd()+'\\'+'individual_responses'+'\\'+'q'+quiz_num+'_'+info[1]+'.csv','a',newline='') as wfile:
                writer=csv.writer(wfile)
                if question[0]=='ques_no':
                    writer.writerow(question+['marked_choice','Total','Legend'])
                    continue
                if itr==0:
                    writer.writerow(question+[response[itr],correct_questions,'Correct Choices'])
                elif itr==1:
                    writer.writerow(question+[response[itr],wrong_choices,'Wrong Choices'])
                elif itr==2:
                    writer.writerow(question+[response[itr],len(unattempted),'Unattempted'])
                elif itr==3:
                    writer.writerow(question+[response[itr],total_marks_obtained,'Marks Obtained'])
                elif itr==4:
                    writer.writerow(question+[response[itr],total_marks,'Total Quiz Marks'])
                else:
                    writer.writerow(question+[response[itr],'',''])
                itr+=1
    total_quiz_questions=len(response)
    print('''Total Quiz Questions:{}
Total Quiz Questions Attempted:{}
Total Correct Question:{}
Total Wrong Questions:{}
Total Marks: {}/{}'''.format(total_quiz_questions,attempted_questions,correct_questions,wrong_choices,total_marks_obtained,total_marks))
    
    quiz_num=int(quiz_num)
    find_user=("SELECT * FROM Project1_marks WHERE roll_num=? AND quiz_num=?")
    c.execute(find_user,[(info[1]),(quiz_num)])
    results=c.fetchall()
    if results:
        c.execute('DELETE FROM Project1_marks WHERE roll_num=? AND quiz_num=?',(info[1],quiz_num))
    insertData='''INSERT INTO Project1_marks(roll_num,quiz_num,total_marks)
    VALUES(?,?,?)'''
    c.execute(insertData,[(info[1]),(quiz_num),(total_marks_obtained)])
    conn.commit()

def multi_quiz(info):
    while True:
        quiz(info)
        res=input("would you like to attempt one more quiz:(Y/N) ")
        if res.lower()=='n':
            break

if __name__ == '__main__':
    new=input("Do you have an account(y/n)  ")
    if(new.lower()=='n'):
        register()
    login()