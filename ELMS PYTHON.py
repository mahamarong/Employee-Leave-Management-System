#HR LOGIN#
def hrlogin():
 
 while True :
    print (' ')
    print ('=============== ')
    print ('***HR MENU***')
    print ('===============')
    print (' ')
    print ('1. REGISTRATION')
    print (' ')
    print ('2. Modify')
    print (' ') 
    print ('3. DELETE')
    print (' ')
    print ('4. VIEW REPORT OF LECTURER')
    print (' ')
    print ('5. CHECK STATUS OF LECTURER')
    print (' ')
    print ('6. UPLOAD YEARLY LEAVES')
    print (' ')
    print ('7. UPLOAD PUBLIC AND UNIVERSITY HOLIDAYS')
    print (' ')
    print ('8. FAQS AND UNIVERSITY LEAVE POLICIES')
    print (' ')
    print ('9. EXIT')
    print (' ')
    
    choice = input ('ENTER YOUR CHOICE AMONG THE OPTIONS ABOVE: ')
    Z = int (choice)

    if Z == 1 :
        register()
        
    elif Z == 2 :
        update()
        
    elif Z == 3 :
        delete()
        
    elif Z == 4 :
        report()
        
    elif Z == 5 :
        global data
        AHA = False
        data[:]= []
        username = input ('\n ENTER FIRST NAME:')
        password = input ('\n  ENTER LAST NAME:')
        print('\n    VARIFYIING DETAILS...')
        time.sleep(3)
        myfile = open("lecturerrecords.txt")
        thelines = myfile.readlines()
        myfile.close()
        for line in thelines:
            lecturer = line.split()
            data.append(lecturer)
            (len(data))
            (len(lecturer))
        for C in range(len(data)):
            if (username == data[C][1] and password == data[C][2]):
                
                
                AHA = True
                print ('YOU ARE VIEWING THE APPLICATION OF: ',data[C][1],data[C][2])
                print (' ')
                print ('                APPLICATION STATUS IS', data[C][0])
                print (' ')
                break
                    
                print ('\n _________________________________________________________________________________________________________________________________________________________________________')
        if AHA == False :
            print ('\n   >>>SORRY DETAILS DOES NOT MATCH OUR RECORDS')


    elif Z == 6 :
        print("Each lecturer is applicable to take 20 leaves per year")
                
    elif Z == 7 :
        print("21 jan 2018 is a public holiday")
        print("6 March 2018 is a University holiday")
        print("13 March 2018 is a public holiday")
        print("14 April 2018 is a University holiday")
        
    elif Z == 8 :
        print("No smoking in the campus")
        print ("Apply one week before going for leave")
        print("Donot spend another day after your leave is done")
    
    elif Z == 9 :
        print('    SYSTEM IS LOGGING OFF...')
        time.sleep(2)
        print('    GOODBYE...')
        break
        
        
          
    else :
        print('   >>>SORRY!, INVALID CHOICE')
        print('   PLEASE CHOOSE FROM THE OPTIONS ABOVE (1 - 8) ')


#ACADEMIC LECTURER LOGIN#
def ACADEMICLOGIN():
    print (' ')
    print ('                       ==================================')
    print ('\n                     ***WELCOME TO ACADEMIC LEADER***')
    print ('                       ==================================')
    
    global data
    AHA = False
    data[:]= []
    username = input ('\n ENTER USERNAME:')
    password = input ('\n ENTER PASSWORD:')
    print('\n    VARIFYIING LOGIN DETAILS...')
    time.sleep(3)
    myfile = open("academicrecords.txt")
    thelines = myfile.readlines()
    myfile.close()
    for line in thelines:
        lecturer = line.split()
        data.append(lecturer)
        (len(data))
        (len(lecturer))
    for C in range(len(data)):
        if (username == data[C][0] and password == data[C][4]):
            AHA = True
            print (' ')
            print ('=======================================')
            print ('***WELCOME TO ACADEMIC LEADER MENU***')
            print ('=======================================')
            print ('YOU ARE LOGGGED IN AS',data[C][0],data[C][1])
            academicmenu()
            break
            
            
            print ('\n _________________________________________________________________________________________________________________________________________________________________________')
        else:
            print ('\n   >>>SORRY INCORRECT USERNAME OR PASSWORD')
            break
            
   
        
#ACADEMIC MENU#
def academicmenu():
    while True:
        
        print (' ')
        print ('1. VIEW LECTUERERS LEAVE APPLICATION STATUS')
        print (' ')
        print ('2. APPROVE LECTURER LEAVE')
        print (' ')
        print ('3. REJECT LECTURER LEAVE')
        print (' ')
        print ('4. PUBLIC AND UNIVERSITY HOLIDAYS')
        print (' ')
        print ('5. UNIVESITY LEAVE POLICIES')
        print (' ')
        print ('6. EXIT')
        print (' ')
            
        choice = input ('ENTER YOUR CHOICE AMONG THE OPTIONS ABOVE: ')
        Z = int (choice)

        #VIEW LECTUERERS LEAVE APPLICATION#    
        if Z == 1 :
            global data
            AHA = False
            data[:]= []
            username = input ('\n ENTER FIRST NAME:')
            password = input ('\n  ENTER LAST NAME:')
            print('\n    VARIFYIING DETAILS...')
            time.sleep(3)
            myfile = open("lecturerrecords.txt")
            thelines = myfile.readlines()
            myfile.close()
            for line in thelines:
                lecturer = line.split()
                data.append(lecturer)
                (len(data))
                (len(lecturer))
            for C in range(len(data)):
                if (username == data[C][1] and password == data[C][2]):
                    AHA = True
                    print ('YOU ARE VIEWING THE APPLICATION OF: ',data[C][1],data[C][2])
                    print (' ')
                    print ('                APPLICATION STATUS IS', data[C][0])
                    print (' ')
                    break
                    
                    print ('\n _________________________________________________________________________________________________________________________________________________________________________')
            if AHA == False :
                print ('\n   >>>SORRY DETAILS DOES NOT MATCH OUR RECORDS')

        #APPROVE LECTURER LEAVE#        
        elif Z == 2 :
            
            
                AHA = False
                status = "APPROVED"
                applied="PROCESSING"
                data[:]= []
                FIRSTNAME = input ('\n PLEASE ENTER LECTURER FIRST NAME:')
                LASTNAME = input ('\n PLEASE ENTER LECTURER LAST NAME:')
                print('\n    VARIFYIING DETAILS...')
                time.sleep(3)
                myfile = open("lecturerrecords.txt", 'r+')
                thelines = myfile.readlines()
                myfile.close()
                for line in thelines:
                    lecturer = line.split()
                    data.append(lecturer)
                    (len(data))
                    (len(lecturer))
                for C in range(len(data)):
                    if (FIRSTNAME == data[C][1] and LASTNAME ==data[C][2]):
                        if(applied == data[C][0]):
                            
                            AHA = True
                            ('DETAILS AVAILABLE AT',C,0)
                            data[C][0] = status
                            print ('\n    APPROVING LEAVE..')
                            time.sleep(3)
                            print ('LEAVE SUCCESSFULLY APPROVED FOR: ',data[C][1],data[C][2])
                            print ('                  +---------------------+')
                            print ('\n _________________________________________________________________________________________________________________________________________________________________________')
                if AHA == False :
                    print ('\n   >>>SORRY! INCORRECT DETAILS OR LECTURER HAS NOT APPLIED FOR LEAVE OR LECTURER IS CURRENTLY ON LEAVE')
                    
                        
                        
                        

                updateddoc = open('lecturerrecords.txt', 'w+')
                for C in range(len(data)):
                    for D in range (len(lecturer)):
                        updateddoc.write(data[C][D] + ' ')
                    updateddoc.write('\n')
                updateddoc.close()

            
                    
                    

       #REJECT LECTURER LEAVE                   
        elif Z == 3:
            AHA = False
            
            status = "REJECTED"
            applied="PROCESSING"
            data[:]= []
            FIRSTNAME = input ('\n PLEASE ENTER LECTURER FIRST NAME:')
            LASTNAME = input ('\n PLEASE ENTER LECTURER LAST NAME:')
            print('\n    VARIFYIING DETAILS...')
            time.sleep(3)
            myfile = open("lecturerrecords.txt", 'r+')
            thelines = myfile.readlines()
            myfile.close()
            for line in thelines:
                lecturer = line.split()
                
                data.append(lecturer)
                (len(data))
                (len(lecturer))
            for C in range(len(data)):
                if (FIRSTNAME == data[C][1] and LASTNAME ==data[C][2]):
                    if(applied == data[C][0]):
                            
                        AHA = True
                        ('DETAILS AVAILABLE AT',C,0)
                        data[C][0] = status
                        print ('\n    REJECTING LEAVE..')
                        time.sleep(3)
                        print ('LEAVE SUCCESSFULLY REJECTED FOR: ',data[C][1],data[C][2])
                        print ('                  +---------------------+')
                        print ('\n _________________________________________________________________________________________________________________________________________________________________________')
            if AHA == False :
                print ('\n   >>>SORRY! INCORRECT DETAILS OR LECTURER HAS NOT APPLIED FOR LEAVE OR LECTURER IS CURRENTLY ON LEAVE')
                    
                        
                        
                        

            updateddoc = open('lecturerrecords.txt', 'w+')
            for C in range(len(data)):
                for D in range (len(lecturer)):
                    updateddoc.write(data[C][D] + ' ')
                updateddoc.write('\n')
            updateddoc.close()


        elif Z == 4 :
                print (' 21 jan 2018 is a public holiday')
                print("6 March 2018 is a University holiday")
                print("13 March 2018 is a public holiday")
                print("14 April 2018 is a University holiday")

        elif Z == 5 :
            print("No smoking in the campus")
            print ("Apply one week before going for leave")
            print("Donot spend another day after your leave is done")


        elif Z == 6:
            break

        else:
            print('   >>>SORRY!, INVALID CHOICE')
            print('   PLEASE CHOOSE FROM THE OPTIONS ABOVE (1 - 6) ')


            
            
            
                                            
  #LECTURER LOGIN#                  
def LECTURERLOGIN():
    
    print (' ')
    print ('                       ==================================')
    print ('\n                     ***WELCOME TO LECTURER LOGIN***')
    print ('                       ==================================')
    
    global data
    AHA = False
    data[:]= []
    username = input ('\n ENTER USERNAME:')
    password = input ('\n ENTER PASSWORD:')
    print('\n    VARIFYIING LOGIN DETAILS...')
    time.sleep(3)
    myfile = open("lecturerrecords.txt")
    thelines = myfile.readlines()
    myfile.close()
    for line in thelines:
        lecturer = line.split()
        data.append(lecturer)
        (len(data))
        (len(lecturer))
    for C in range(len(data)):
        if (username == data[C][1] and password == data[C][5]):
            AHA = True
            print (' ')
            print ('=======================================')
            print ('***WELCOME TO LECTUERER MENU***')
            print ('=======================================')
            print ('YOU ARE LOGGGED IN AS',data[C][0],data[C][1])
            lecturermenu()
            
            break
            
            print ('\n _________________________________________________________________________________________________________________________________________________________________________')
            
    if AHA == False :
        print ('\n   >>>SORRY INCORRECT USERNAME OR PASSWORD')                      
                
#LECTURER MENU
def lecturermenu():
    while True:
        
        
        global data
        status = 'PROCESSING'
        AHA = False
        data[:]= []
                
        
        print (' ')
        print ('1. APPLY FOR LEAVE')
        print (' ')
        print ('2. CHECK LEAVE STATUS')
        print (' ')
        print ('3. VIEW HOLIDAYS')
        print (' ')
        print ('4. UNIVERSITY LEAVE POLICIES')
        print (' ')
        print ('5. GO BACK')
        print (' ')
                
        choice = input ('ENTER YOUR CHOICE AMONG THE OPTIONS ABOVE: ')
        Z = int (choice)
        
        #APPLY FOR LEAVE       
        if Z == 1 :
                
                AHA = False
                status = "PROCESSING"
                data[:]= []
                login = input ('\n PLEASE ENTER YOUR PASSWORD AGAIN:')
                print('\n    VARIFYIING PASSWORD...')
                time.sleep(3)
                myfile = open("lecturerrecords.txt", 'r+')
                thelines = myfile.readlines()
                myfile.close()
                for line in thelines:
                    lecturer = line.split()
                    data.append(lecturer)
                    (len(data))
                    (len(lecturer))
                for C in range(len(data)):
                    if (login == data[C][5]):
                        AHA = True
                        ('DETAILS AVAILABLE AT',C,0)
                        data[C][0] = status
                        print ('\n    SAVING YOUR CHANGES..')
                        time.sleep(3)
                        print ('\n                ***LEAVE APPLIED SUCCESSFUL***')
                        print ('                  +---------------------+')
                        print ('\n _________________________________________________________________________________________________________________________________________________________________________')
                if AHA == False :
                    print ('\n   >>>SORRY! WRONG PASSWORD')
        
                updateddoc = open('lecturerrecords.txt', 'w+')
                for C in range(len(data)):
                    for D in range (len(lecturer)):
                        updateddoc.write(data[C][D] + ' ')
                    updateddoc.write('\n')
                updateddoc.close()

            
     #CHECK LEAVE STATUS
        if Z == 2 :
 
                AHA = False
                data[:]= []
                password = input ('\n  ENTER PASSWORD AGAIN:')
                print('\n    VARIFYIING DETAILS...')
                time.sleep(3)
                myfile = open("lecturerrecords.txt")
                thelines = myfile.readlines()
                myfile.close()
                for line in thelines:
                    lecturer = line.split()
                    data.append(lecturer)
                    (len(data))
                    (len(lecturer))
                    for C in range(len(data)):
                        if (password == data[C][5]):
                            AHA = True
                            print ('YOU ARE VIEWING THE APPLICATION OF: ',data[C][1],data[C][2])
                            print (' ')
                            print ('                APPLICATION STATUS IS', data[C][0])
                            print (' ')
                            break
                            
                            print ('\n _________________________________________________________________________________________________________________________________________________________________________')
                if AHA == False :
                    
                            
                    print ('\n   >>>SORRY INCORRECT PASSWORD')

        if Z == 3:
                
                print (' 21 jan 2018 is a public holiday')
                print("6 March 2018 is a University holiday")
                print("13 March 2018 is a public holiday")
                print("14 April 2018 is a University holiday")
                
        if Z == 4:
            print("No smoking in the campus")
            print ("Apply one week before going for leave")
            print("Donot spend another day after your leave is done")
            

        if Z == 5:
            break
            
    else:
        
            
        print('   >>>SORRY!, INVALID CHOICE')
        print('   PLEASE CHOOSE FROM THE OPTIONS ABOVE (1 - 4) ')

                
                
        
    
            
            
    


#FUNCTION 1 (REGISTRATION)#
def register():
    while True:
    
        print (' ')
        print ('                   =============================')
        print ('                   ***WELCOME TO REGISTRATION***')
        print ('                   =============================')
        print ('\nCHOOSE WHO TO REGISTER ')
        print (' ')
        print ('1. ACADEMIC LECTURER')
        print (' ')
        print ('2. LECTURER')
        print (' ')
        print ('3. GO BACK')
        print (' ')
            
        choice = input ('ENTER YOUR CHOICE AMONG THE OPTIONS ABOVE: ')
        Z = int (choice)
             
        if Z == 1 :
            print ('                   =========================================')
            print ('                   ***REGISTER AN ACADEMIC LEADER BELOW***')
            print ('                   =========================================')
            print (' ')
            print ('             ENTER DETAILS BELOW')
            print (' ')
            firstname = input (' FIRST NAME:')
            lastname = input (' LAST NAME:')
            email = input (' EMAIL ADDRESS:')
            contact = input (' CONTACT NUMBER:')
            password = input (' PASSWORD:')
            confirmpassword = input (' RE-TYPE PASSWORD:')
            regdate = date.today()
            print ('\n     PROCESSING...')
            time.sleep (3)
            if (password==confirmpassword):
                
                print ('     SAVING YOUR DETAILS...')
                time.sleep(2)
                print ('\n              ***REGISTRATION SUCCESSFUL***')
                print ('\n                 REGISTERED ON: '+str(regdate))
                print ('            +-----------------------------------+')
                print ('\n _____________________________________________________________________________________________________________________________________________________________________________')
                myfile = open ('academicrecords.txt' , 'a')
                myfile.write(firstname+' ')
                myfile.write(lastname+' ')
                myfile.write(email+' ')
                myfile.write(contact+' ')
                myfile.write(password+' ')
                myfile.write(confirmpassword+'\n')
                myfile.close()
               
                
            else :
                 print('   >>>SORRY!, PASSOWRD AND CONFIRM PASSWORD DOES NOT MATCH')
                 register()

            
        elif Z == 2 :
            print ('                   =========================================')
            print ('                   ***REGISTER A LECTURER BELOW***')
            print ('                   =========================================')
            print (' ')
            print ('             ENTER DETAILS BELOW')
            print (' ')
            firstname = input (' FIRST NAME:')
            lastname = input (' LAST NAME:')
            email = input (' EMAIL ADDRESS:')
            contact = input (' CONTACT NUMBER:')
            password = input (' PASSWORD:')
            confirmpassword = input (' RE-TYPE PASSWORD:')
            regdate = date.today()
            applicationstatus =('NULL')
            print ('\n     PROCESSING...')
            time.sleep (3)
            if (password==confirmpassword):
                
                print ('     SAVING YOUR DETAILS...')
                time.sleep(2)
                print ('\n              ***REGISTRATION SUCCESSFUL***')
                print ('\n                 REGISTERED ON: '+str(regdate))
                print ('            +-----------------------------------+')
                print ('\n _____________________________________________________________________________________________________________________________________________________________________________')
                myfile = open ('lecturerrecords.txt' , 'a')
                myfile.write(applicationstatus+' ')
                myfile.write(firstname+' ')
                myfile.write(lastname+' ')
                myfile.write(email+' ')
                myfile.write(contact+' ')
                myfile.write(password+' ')
                myfile.write(confirmpassword+'\n')
                myfile.close()
                
            else :
                 print('   >>>SORRY!, PASSOWRD AND CONFIRM PASSWORD DOES NOT MATCH')
                 register()
        elif Z == 3 :
            hrlogin()
                    
        else :
             print('   >>>SORRY!, INVALID CHOICE')
             print('   PLEASE CHOOSE FROM THE OPTIONS ABOVE (1 - 3) ')
   
##FUNCTION 2 (UPDATE)#
def update():
    print (' ')
    print ('                       =======================')
    print ('\n                     ***WELCOME TO MODIFY***')
    print ('                       =======================')
    print ('\n YOU CAN CHANGE A LECTURER`S DETAILS HERE')
    global data
    AHA = False
    data[:]= []
    login = input ('\n PLEASE ENTER LECTURER NAME YOU WISH TO UPDATE:')
    password = input ('\n PLEASE ENTER LECTURER PASSWORD YOU WISH TO UPDATE:')
    print('\n    VARIFYIING DETAILS...')
    time.sleep(3)
    myfile = open("lecturerrecords.txt", 'r+')
    thelines = myfile.readlines()
    myfile.close()
    for line in thelines:
        lecturer = line.split()
        data.append(lecturer)
        (len(data))
        (len(lecturer))
    for C in range(len(data)):
        if (login == data[C][1] and password == data[C][5]):
            AHA = True
            ('DETAILS AVAILABLE AT',C,0)
            new_contact = input ('PLEASE ENTER NEW CONTACT NUMBER:')
            data[C][4] = new_contact
            print ('\n    SAVING YOUR CHANGES..')
            time.sleep(3)
            print ('\n                ***UPDATE SUCCESSFUL***')
            print ('                  +---------------------+')
            print ('\n _________________________________________________________________________________________________________________________________________________________________________')
    if AHA == False :
        print ('\n   >>>SORRY!DETAILS IS NOT IN THE SYSTEM')
        
            
            
            

    updateddoc = open('lecturerrecords.txt', 'w+')
    for C in range(len(data)):
        for D in range (len(lecturer)):
            updateddoc.write(data[C][D] + ' ')
        updateddoc.write('\n')
    updateddoc.close()

#FUNCTION 3(DELETE)#    
def delete():
    while True:
  
        print (' ')
        print ('                   =============================')
        print ('                   ***WELCOME TO DELETE***')
        print ('                   =============================')
        print ('\nCHOOSE WHO TO DELETE ')
        print (' ')
        print ('1. DELETE ACADEMIC LECTURER')
        print (' ')
        print ('2. DELETE LECTURER')
        print (' ')
        print ('3. GO BACK')
        print (' ')
            
        choice = input ('ENTER YOUR CHOICE AMONG THE OPTIONS ABOVE: ')
        Z = int (choice)
             
        if Z == 1 :
  
            print (' ')
            print ('                           =======================')  
            print ('                           ***WELCOME TO DELETE***')
            print ('                           =======================')
            print ('\n YOU CAN DELETE A REGSITERED ACADEMIC LEADER HERE')
            global data
            AHA = False
            index_to_del = -1;
            C = 0
            data[:]= []
            FIRSTNAME = input ('\n PLEASE ENTER FIRST NAME OF USER YOU WISH TO DELETE:')
            LASTNAME = input ('\n PLEASE ENTER LAST NAME OF USER YOU WISH TO DELETE:')
            myfile = open("academicrecords.txt", 'r+')
            thelines = myfile.readlines()
            myfile.close()
            for line in thelines:
                lecturer = line.split()
                data.append(lecturer)
                (len(data))
                (len(lecturer))
            for C in range(len(data)):
                  index_to_del + 1
                  if (FIRSTNAME == data[C][0] and LASTNAME == data[C][1]):
                      AHA = True
                      ('DETAILS AVAILABLE AT',C,0)
                      break
                      
            if AHA == False :
                
                print ('\n   >>>SORRY! DETAILS IS WRONG ')
                    
                        
            if AHA == True :
                
                del data[index_to_del]
                print ('\n   DELETING...')
                time.sleep(3)
                print ('\n                ***ACADEMIC LEADER HAS BEEN DELETED SUCCESSFULLY***')
                print ('                 +-----------------------+')
                print ('\n__________________________________________________________________________________________________________________________________________________________________________________')
                        

            updateddoc = open('academicrecords.txt', 'w+')
            for C in range(len(data)):
                for D in range (len(lecturer)):
                    updateddoc.write(data[C][D] + ' ')
                updateddoc.write('\n')
            updateddoc.close()

        elif Z == 2 :
            
  
            print (' ')
            print ('                           =======================')  
            print ('                           ***WELCOME TO DELETE***')
            print ('                           =======================')
            print ('\n YOU CAN DELETE A REGSITERED LECTURER HERE')
            AHA = False
            index_to_del = -1;
            C = 0
            data[:]= []
            FIRSTNAME = input ('\n PLEASE ENTER FIRST NAME OF USER YOU WISH TO DELETE:')
            LASTNAME = input ('\n PLEASE ENTER LASTNAME OF USER YOU WISH TO DELETE:')
            myfile = open("lecturerrecords.txt", 'r+')
            thelines = myfile.readlines()
            myfile.close()
            for line in thelines:
                lecturer = line.split()
                data.append(lecturer)
                (len(data))
                (len(lecturer))
            for C in range(len(data)):
                  index_to_del + 1
                  if (FIRSTNAME == data[C][1] and LASTNAME == data[C][2]):
                      AHA = True
                      ('DETAILS AVAILABLE AT',C,0)
                      break
                      
            if AHA == False :
                
                print ('\n   >>>SORRY! DETAILS IS WRONG ')
                    
                        
            if AHA == True :
                
                del data[index_to_del]
                print ('\n   DELETING...')
                time.sleep(3)
                print ('\n                ***LECTURER HAS BEEN DELETED SUCCESSFULLY***')
                print ('                 +-----------------------+')
                print ('\n__________________________________________________________________________________________________________________________________________________________________________________')
                        

            updateddoc = open('lecturerrecords.txt', 'w+')
            for C in range(len(data)):
                for D in range (len(lecturer)):
                    updateddoc.write(data[C][D] + ' ')
                updateddoc.write('\n')
            updateddoc.close()

    

        elif Z == 3 :
            break
        else :
            
            print('   >>>SORRY!, INVALID CHOICE')
            print('   PLEASE CHOOSE FROM THE OPTIONS ABOVE (1 - 3) ')

            


#FUNCTION 4(REPORT)#        
def report():
  print (' ')
  print ('                      =================================')
  print ('                      ****WELCOME TO REPORT DISPLAY****')
  print ('                      =================================')
  print (' ')
  print ('YOU CAN DISLPAY REGISTERED LECTURER`S RECORD HERE')
  
        
  global data
  AHA = False
  index_to_del = -1;
  C = 0
  data[:]= []
  login = input ('\n PLEASE ENTER LECTURERS USERNAME:')
  password = input ('\n PLEASE ENTER LECTURERS PASSWORD:')
  myfile = open("lecturerrecords.txt", 'r+')
  thelines = myfile.readlines()
  myfile.close()
  for line in thelines:
      lecturer = line.split()
      data.append(lecturer)
      (len(data))
      (len(lecturer))
  for C in range(len(data)):
      index_to_del + 1
      if (login == data[C][1] and password == data [C][5]):
          AHA = True
          ('DETAILS AVAILABLE AT',C,0)
          break
          
  if AHA == False :
     print ('\n   >>>SORRY! USERNAME IS NOT IN THE SYSTEM')
        
            
  if AHA == True :
     mydata = data[index_to_del]
     print (' ')
     print ('               **LECTURER`S FULL DETAILS AS IN SYSTEM** ') 
     print ('           +--------------------------------------------+')
     print('                       FIRST NAME: ', mydata[1])
     print('                        LAST NAME: ', mydata[2])
     print('                        EMAIL    : ', mydata[3])
     print('                   CONTACT NUMBER: ', mydata[4])
     print ('           +--------------------------------------------+')
     print ('\n________________________________________________________________________________________________________________________________________________________________________________')

  updateddoc = open('lecturerrecords.txt', 'w+')
  for C in range(len(data)):
      for D in range (len(lecturer)):
          updateddoc.write(data[C][D] + ' ')
      updateddoc.write('\n')
  updateddoc.close()


    


	
print ("======================================================")    
print ("**** PLEASE KINDLY ENTER YOUR LOGIN DETAILS BELOW ****")
print ("======================================================")
        
A='muhammad'
B='marong'
import time
from datetime import timedelta
from datetime import date
import os.path
from os import path
data = []
import os

while True :
    
    print (' ')
    print ('1. HR')
    print (' ')
    print ('2. ACADEMIC LECTURER')
    print (' ')
    print ('3. LECTURER')
    print (' ')
    print ('4. EXIT')
    print (' ')
        
    choice = input ('ENTER YOUR CHOICE AMONG THE OPTIONS ABOVE: ')
    Z = int (choice)

    if Z == 1 :
     username = input ('\n ENTER USERNAME:')
     password = input (' ENTER PASSWORD:')
     if(username == A and password == B):
        hrlogin()
        break
     elif(username==A and password!=B):
        print (' ')
        print ('   >>>SORRY! INCORRECT PASSWORD')
        print (' ')
        os.system('cls')
     elif (username!=A and password==B):
        print (' ')
        print ('   >>>SORRY! INCORRECT USERNAME')
        print (' ')
     elif (username!=A and password!=B):
        print (' ')
        print ('   >>>SORRY! INCORRECT USERNAME AND PASSWORD')
        print (' ')
        
    elif Z == 2 :
        ACADEMICLOGIN()
    elif Z == 3 :
        LECTURERLOGIN()
    elif Z == 4 :
        print('    SYSTEM IS LOGGING OFF...')
        time.sleep(2)
        print('    GOODBYE...')
        break
    else :
         print('   >>>SORRY!, INVALID CHOICE')
         print('   PLEASE CHOOSE FROM THE OPTIONS ABOVE (1 - 4) ')



              
