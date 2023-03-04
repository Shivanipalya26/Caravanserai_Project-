import os
import pickle
import getpass
import mysql.connector as c
    
def admin():
    for i in range(3):
        print('PASSWORD WILL NOT BE SHOWN DUE TO SAFETY-PRECAUTIONS')
        s=getpass.getpass("Enter password:=")
        if s=='a':
            print('Now you can access data')
            #input()
            os.system("cls")
            while True:
                print(" "*48,"--DETAILS--")
                print(" "*16,"1.ROOMS","\n"," "*15,"2.RESTAURANT","\n"," "*15,"3.SECURITY","\n"," "*15,"4.CHECK-IN DETAILS","\n"," "*15,"5.EXIT")
                b=int(input("enter the choice for accessing further:: ")) 
                os.system("cls")
                if b==1:
                    print("---------------------ROOMS---------------------")
                    print(" "*16,"1.SHOW DATA","\n"," "*15,"2.INSERT NEW DATA","\n"," "*15,"3.UPDATE DATA","\n"," "*15,"4.DELETE RECORD","\n"," "*15,"5.EXIT")
                    c=int(input("enter the choice: "))
                    if c==1:
                        s="select * from rooms"
                        p.execute(s)
                        print("ROOM NO.   ROOM TYPE   STATUS   EXTRA FACILITY   PRICE")
                        for i in p:
                            print(i[0],' '*4,i[1],' '*4,i[2],' '*4,i[3],' '*4,' '*4,i[4])
                        input()
                        os.system("cls")
                    elif c==2:
                        s="insert into rooms values(%s,%s,%s,%s,%s)"
                        a=int(input("ENTER ROOM NO.::"))
                        b=input("ENTER ROOM TYPE::")
                        c=input("ENTER STATUS::")
                        d=input("ENTER EXTRA FACILITY(AC/NON AC)::")
                        e=input("ENTER PRICE::")
                        k=[a,b,c,d,e]
                        p.execute(s,k)
                        db.commit()
                        print("Record inserted")
                        input()
                        os.system("cls")
                    elif c==3:
                        room_no=int(input("Enter Room no. for updating records="))
                        s="select * from rooms"
                        p.execute(s)
                        k=p.fetchall()
                        for i in k:
                            if i[0]==room_no:
                                m="update rooms set Room_type=%s,Status=%s,Extra_facility=%s,Price=%s where Room_no=%s"
                                Room_type=input("enter Room_type:")
                                Status=input("enter Status:")
                                Extra_facility=input("enter Extra_facility:")
                                Price=input("enter Price:")
                                q=[Room_type,Status,Extra_facility,Price,room_no]
                                p.execute(m,q)
                                db.commit()
                                print("RECORD UPDATED")
                        input()
                        os.system("cls")
                    elif c==4:
                        room_no=int(input("ENTER ROOM_NO YOU WANT TO DELETE::"))
                        s="delete from rooms where room_no=%s"
                        de=[room_no]
                        p.execute(s,de)
                        db.commit()
                        print("RECORD DELETED")
                        input()
                        os.system("cls")
                os.system("cls")
                if b==2:
                    print("---------------------RESTAURANT---------------------")
                    print(" "*16,"1.SHOW DATA","\n"," "*15,"2.INSERT NEW DATA","\n"," "*15,"3.UPDATE DATA","\n"," "*15,"4.DELETE RECORD","\n"," "*15,"5.EXIT")
                    c=int(input("enter the choice: "))
                    if c==1:
                        s="select * from foods"
                        p.execute(s)
                        print("CODE NO.   FOOD NAME   PRICE   AVAILIABLITY")
                        for i in p:
                            print(i[0],' '*4,i[1],' '*4,i[2],' '*4,i[3],' '*4)
                        input()
                        os.system("cls")
                    elif c==2:
                        s="insert into foods values(%s,%s,%s,%s)"
                        a=int(input("ENTER CODE NO.::"))
                        b=input("ENTER FOOD NAME::")
                        c=input("ENTER PRICE::")
                        d=input("ENTER AVAILABILITY::")
                        k=[a,b,c,d]
                        p.execute(s,k)
                        db.commit()
                        print("Record inserted")
                        input()
                        os.system("cls")
                    elif c==3:
                        Code_no=int(input("Enter Code no. for updating records="))
                        s="select * from foods"
                        p.execute(s)
                        k=p.fetchall()
                        for i in k:
                            if i[0]==Code_no:
                                m="update foods set Food_name=%s,Price=%s,Availability=%s where Code_no=%s"
                                Food_name=input("enter Food_name:")
                                Price=int(input("enter Price:"))
                                Availability=input("enter Availability:")
                                q=[Food_name,Price,Availability,Code_no]
                                p.execute(m,q)
                                db.commit()
                                print("RECORD UPDATED")
                        
                        input()
                        os.system("cls")
                    elif c==4:
                        Code_no=int(input("ENTER CODE_NO YOU WANT TO DELETE::"))
                        s="delete from foods where Code_no=%s"
                        we=[Code_no]
                        p.execute(s,we)
                        db.commit()
                        print("RECORD DELETED")
                        input()
                        os.system("cls")
                os.system("cls")
                if b==3:
                    print("---------------------SECURITY---------------------")
                    print('''->PARKING SPACE
->24-HOUR RECEPTION
->FREE WIFI IN THE ENTIRE HOTEL
->LOUNGE WITH OPEN FIRE
->COFFEE AND TEA FACILITY IN ALL ROOMS
->LOUNDARY AND DRY CLEANING SERVICES
->ROOM SERVICES
->RESTAURANT OPEN 24-HOURS
->FITNESS CENTRE
->BIKE AND CAR RENTAL
->SPECIAL OFFERS FOR WEEKEND
->PARTY ZONE AVAILABLE''')
                input()
                os.system("cls")
                if b==4:
                    s="select * from check_in"
                    p.execute(s)
                    print("CID   ROOM NO  NAME         ADDRESS       AGE     NATIONALITY   PHONE NO       ROOM TYPE")
                    for i in p:
                        print(i[0],' '*2,i[1],' '*2,i[2],' '*2,i[3],' '*2,i[4],' '*2,i[5],' '*2,i[6],' '*2,i[7])
                    input()
                    os.system("cls")
                if b==5:
                    print("████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗")
                    print("╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║")
                    print("░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║")
                    print("░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║")
                    print("░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝")
                    print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░ ")
                    break
            input()
            break
                
        else:
            print("Invalid password")
            input()
            os.system("cls")
            
        
def user():
    while True:
        display()
        print("IF YOU WANT TO CHECK-IN IN OUR HOTEL PRESS 'Y'")
        print("IF YOU WANT TO CHECK-OUT FROM THE HOTEL PRESS 'X'")
        print("PRESS 'E' FOR EXIT")
        opt=input("ENTER YOUR CHOICE::")
        os.system("cls")
        if opt=='Y' or opt=='y':
            cid=int(input("ENTER CUSTOMER ID:"))
            name=input("ENTER NAME:")
            address=input("ENTER YOUR ADDRESS:")
            age=input("ENTER AGE:")
            nationality=input("ENTER NATIONALITY:")
            phone_no=input("ENTER PHONE NO.=")
            room_type=input("ENTER ROOM TYPE=")
            rn="select * from rooms"
            p.execute(rn)
            k=p.fetchall();
            print("ROOMS AVAILABLE UNDER THE FOLLOWING CATEGORY:-")
            for i in k:
                if i[1]==room_type:
                    if i[2]=='available':
                        print(i[0])
                        room_no=int(input("ENTER YOUR ROOM NO::"))
                        s="insert into check_in values(%s,%s,%s,%s,%s,%s,%s,%s)"
                        l=[cid,room_no,name,address,age,nationality,phone_no,room_type]
                        p.execute(s,l)
                        db.commit()
                        up="update rooms set status='unavailable' where room_no=%s "
                        o=[room_no]
                        p.execute(up,o)
                        db.commit()
                        print('''SUCCESSFULLY ACCOUNT CREATED
HOPE YOU ENJOY VISTING TO OUR HOTEL PAGE''')
                        input()
                        os.system('cls')
                        break
                    else:
                        print('''----------SORRY-----------
NO ROOM AVAILABLE OF YOUR CHOICE''')
                        break
            break
        elif opt=='X' or opt=='x':
            no=int(input("ENTER YOUR ROOM NO::"))
            Op="update rooms set Status='available' where room_no=%s "
            o=[no]
            p.execute(Op,o)
            db.commit()
            print('''THANK YOU FOR VISTING TO YOUR HOTEL
HOPE YOU COME AGAIN!!!! ''')
            input()
            os.system('cls')
            break
            
        elif opt=="E" or opt=='e':
            print("THANK YOU FOR VISTING")
            break
        else:
            print("INVALID ENTRY")
            


def display():
    while True:
        print(" "*48,"--DETAILS--")
        print(" "*16,"1.ROOMS","\n"," "*15,"2.RESTAURANT","\n"," "*15,"3.SECURITY","\n"," "*15,"4.EXIT")
        ch=int(input("enter the choice:: ")) 
        os.system("cls")
        if ch==1:
            s="select * from rooms"
            p.execute(s)
            for i in p:
                print(i)
            input()
            os.system("cls")
        elif ch==2:
            s="select * from foods"
            p.execute(s)
            for i in p:
                print(i)
            input()
            os.system("cls")
        elif ch==3:
            print('''->PARKING SPACE
->24-HOUR RECEPTION
->FREE WIFI IN THE ENTIRE HOTEL
->LOUNGE WITH OPEN FIRE
->COFFEE AND TEA FACILITY IN ALL ROOMS
->LOUNDARY AND DRY CLEANING SERVICES
->ROOM SERVICES
->RESTAURANT OPEN 24-HOURS
->FITNESS CENTRE
->BIKE AND CAR RENTAL
->SPECIAL OFFERS FOR WEEKEND
->PARTY ZONE AVAILABLE''')
            input()
            os.system("cls")
        elif ch==4:
            break

        
print('* '* 105)
print('* '*105)               
print(' '*40,' ████████████████████████████████████████████████████████████████████████████████▀█████████████████')
print(' '*40,' █▄─█─▄██▀▄─██▄─▀█▀─▄█▄─▄████▀▄─████▄─▀█▄─▄█▄─▄▄─█─█─█▄─▄▄▀█▄─██─▄███─█─█▄─▄█─▄▄▄▄█─█─█▄─▄▄─█▄─▄▄▀█')
print(' '*40,' ██─▄▀███─▀─███─█▄█─███─██▀██─▀─█████─█▄▀─███─▄█▀█─▄─██─▄─▄██─██─████─▄─██─██─██▄─█─▄─██─▄█▀██─▄─▄█')
print(' '*40,' ▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▀▄▀▄▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀')
print(' '*40,' ██████████████████████████████████████████████████████████████████████████████████████████')
print(' '*40,' █─▄▄▄▄█▄─▄▄─█─▄▄▄─█─▄▄─█▄─▀█▄─▄█▄─▄▄▀██▀▄─██▄─▄▄▀█▄─█─▄███─▄▄▄▄█─▄▄▄─█─█─█─▄▄─█─▄▄─█▄─▄███')
print(' '*40,' █▄▄▄▄─██─▄█▀█─███▀█─██─██─█▄▀─███─██─██─▀─███─▄─▄██▄─▄████▄▄▄▄─█─███▀█─▄─█─██─█─██─██─██▀█')
print(' '*40,' ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀')
print('\n')
print('-'*211)
print(' '*63,'█▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   ▀█▀ █▀█ █▀█ █ █▀▀ ▄▄')
print(' '*63,'█▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   ░█░ █▄█ █▀▀ █ █▄▄ ░░')
print('\n')
print(' '*53,'█░█ █▀█ ▀█▀ █▀▀ █░░   █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀')
print(' '*53,'█▀█ █▄█ ░█░ ██▄ █▄▄   █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █░▀░█ ██▄ █░▀█ ░█░')
print('\n')
print('\n')
print('\n')
print(' '*65,'█▀▀ █── █▀▀█ █▀▀ █▀▀ ── ▀▄░▄▀ ▀█▀ ▀█▀')
print(' '*65,'█── █── █▄▄█ ▀▀█ ▀▀█ ▀▀ ─░█── ░█─ ░█─') 
print(' '*65,'▀▀▀ ▀▀▀ ▀──▀ ▀▀▀ ▀▀▀ ── ▄▀░▀▄ ▄█▄ ▄█▄')
print('\n')
print('\n')
print(' '*38,'█▀▀ █──█ █▀▀▄ ──▀ █▀▀ █▀▀ ▀▀█▀▀ ── █▀▀ █▀▀█ █▀▄▀█ █▀▀█ █──█ ▀▀█▀▀ █▀▀ █▀▀█    █▀▀ █▀▀ ─▀─ █▀▀ █▀▀▄ █▀▀ █▀▀') 
print(' '*38,'▀▀█ █──█ █▀▀▄ ──█ █▀▀ █── ──█── ▀▀ █── █──█ █─▀─█ █──█ █──█ ──█── █▀▀ █▄▄▀    ▀▀█ █── ▀█▀ █▀▀ █──█ █── █▀▀')
print(' '*38,'▀▀▀ ─▀▀▀ ▀▀▀─ █▄█ ▀▀▀ ▀▀▀ ──▀── ── ▀▀▀ ▀▀▀▀ ▀───▀ █▀▀▀ ─▀▀▀ ──▀── ▀▀▀ ▀─▀▀    ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀ ▀▀▀')
print('\n')
print(' '*55,'█▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █▀▀█ █▀▄▀█ ── █▀▀ █▀▀ ─▀─ █▀▀ █▀▀▄ █▀▀ █▀▀ ')             
print(' '*55,'▀▀█ ──█── █▄▄▀ █▀▀ █▄▄█ █─▀─█ ▀▀ ▀▀█ █── ▀█▀ █▀▀ █──█ █── █▀▀ ')
print(' '*55,'▀▀▀ ──▀── ▀─▀▀ ▀▀▀ ▀──▀ ▀───▀ ── ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀ ▀▀▀ ')
print('\n','\n','\n','\n',' '*40,'SUBMITTED TO-',' '*50,'DESIGNED AND MAINTAINED BY-')
print(' '*40,'SHANI VISHWAKARMA',' '*50,'SARTHAK WANKHEDE')
print(' '*109,'MANSI BIST')
print(' '*109,'SHIVANI PALYA')
print('* '*105)
print('* '*105)
input()
os.system("cls")
print('* '* 105)
print('* '* 105)
print(' '*60,'╭╮╭╮╭┳━━━┳╮╱╱╭━━━┳━━━┳━╮╭━┳━━━╮╭━━━━┳━━━╮╭━━━┳╮╱╭┳━━━╮╭╮╱╭┳━━━┳━━━━┳━━━┳╮')
print(' '*60,'┃┃┃┃┃┃╭━━┫┃╱╱┃╭━╮┃╭━╮┃┃╰╯┃┃╭━━╯┃╭╮╭╮┃╭━╮┃┃╭━╮┃┃╱┃┃╭━╮┃┃┃╱┃┃╭━╮┃╭╮╭╮┃╭━━┫┃')
print(' '*60,'┃┃┃┃┃┃╰━━┫┃╱╱┃┃╱╰┫┃╱┃┃╭╮╭╮┃╰━━╮╰╯┃┃╰┫┃╱┃┃┃┃╱┃┃┃╱┃┃╰━╯┃┃╰━╯┃┃╱┃┣╯┃┃╰┫╰━━┫┃')
print(' '*60,'┃╰╯╰╯┃╭━━┫┃╱╭┫┃╱╭┫┃╱┃┃┃┃┃┃┃╭━━╯╱╱┃┃╱┃┃╱┃┃┃┃╱┃┃┃╱┃┃╭╮╭╯┃╭━╮┃┃╱┃┃╱┃┃╱┃╭━━┫┃╱╭╮')
print(' '*60,'╰╮╭╮╭┫╰━━┫╰━╯┃╰━╯┃╰━╯┃┃┃┃┃┃╰━━╮╱╱┃┃╱┃╰━╯┃┃╰━╯┃╰━╯┃┃┃╰╮┃┃╱┃┃╰━╯┃╱┃┃╱┃╰━━┫╰━╯┃')
print(' '*60,'╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━┻╯╰╯╰┻━━━╯╱╱╰╯╱╰━━━╯╰━━━┻━━━┻╯╰━╯╰╯╱╰┻━━━╯╱╰╯╱╰━━━┻━━━╯')
print('\n')
print('\n')
print(' '*58,'▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
print(' '*58,'██░██░██░▄▄▄░█▄▄░▄▄██░▄▄▄██░███████░▀██░█▄░▄██░▄▄▄░█░▄▄▀██░▄▄▀██░▄▄░█░▄▄▀█░▄▄▀██░██░')
print(' '*58,'██░▄▄░██░███░███░████░▄▄▄██░███████░█░█░██░███▄▄▄▀▀█░▀▀░██░▀▀▄██░█▀▀█░▀▀░█░▀▀░██░▄▄░')
print(' '*58,'██░██░██░▀▀▀░███░████░▀▀▀██░▀▀░████░██▄░█▀░▀██░▀▀▀░█░██░██░██░██░▀▀▄█░██░█░██░██░██░')
print(' '*58,'▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
print('\n')
print('\n')
print(' '*65,'# '*31,'\n')
print(' '*62,'# '*35)
print(' '*68,'# ','MODERN 5-STAR LUXURY IN HISTORICAL CASTLE WALLS','#')
print(' '*68,'# ','SPACE FOR UPTO 320 PERSONS',' '*20,'#')
print(' '*68,'# ','9 DAYLIT CONFERENCE ROOMS',' '*21,'#')
print(' '*68,'# ','PERSONAL EVENT SUPPORT',' '*24,'#')
print(' '*68,'# ','INTERNET TERMINAL AVAILABLE',' '*18,'#')
print(' '*68,'# ','FREE FITNESS AND RELAXATION AREA',' '*14,'#')
print(' '*68,'# ','ELEGANT FUNCTION ROOMS',' '*24,'#')
print(' '*62,'# '*35,'\n')
print(' '*65,'# '*31)
print('\n'*2)
print(' '*65,'!!!HAVE A WONDERFULLY RELAXED HOLIDAY WITH OUR WELCOME SPECIALS!!!')
print('\n'*3)
print('^^ALL PATHS LEAD TO THE HOTEL^^','\n'*2,'ADDRESS:','\n','CONTACT NO.: +4995170000','\n','E-mail:welcomehotel123@gmail.com')
print(' '*85,'!WE SUPPORT YOU')
print(' '*85,'PLANNING YOUR EVENT!')
print('* '* 105)
print('* '*105)
input()
os.system("cls")

db=c.connect(host="localhost",user="root",passwd="123456",database="hotelmanagement")
p=db.cursor()
print(" "*28,"1.ADMIN","\n"," "*27,"2.USER")
a=int(input("ENTER WHO YOU ARE FROM ABOVE OPTION::"))
if a==1:
    admin()
elif a==2:
    user()
else:
    print("INVALID OPTION")
