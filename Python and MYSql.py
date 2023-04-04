#Python and MySql Create Read and delete program
#Here we have already created a table(bhavesh) manually in Database with Xampp


import mysql.connector as bhavesh
conn = bhavesh.connect(host = "localhost",user="root",passwd="",database="bhavesh")
cursor=conn.cursor()
def menu():
    print("select any option\n1.Inster\n2.read\n3.Update\n4.Delete")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        insert()
    elif(ch==2):
        read()
    elif(ch==3):
        update()
    elif(ch==4):
        delete()
    else:
        print("Wrong option choosen")
        menu()

def insert():
    name=input("Enter your name:")
    phone=input("Enter your phone number:")
    sql="insert into bhavesh(name,phone) values(%s,%s)"
    val= (name,phone)
    try:
        cursor.execute(sql,val)
        conn.commit()
        print("Inserted successfully")
        menu()
    except Exception as e:
        print(e)
        menu()

def read():
    sql="select*from bhavesh"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for x in data:
            print(x)
        print("successful")
    except:
        print("Error occured")
    menu()

def delete():
    ch=input("Do you have row id?(y/n):").lower()
    if(ch=="y"):
        idd=input("Enter your row id:")
        sql="delete from bhavesh where id=%s"
        val=(idd,)
        try:
            cursor.execute(sql,val)
            conn.commit()
            print("Deleted successfully")
            menu()
        except:
            print("Error")
            menu()
    else:
        print("Go to read section and get your id")
        menu()
def update():
    ch=input("Do you have row id?(y/n):").lower()
    if(ch=="y"):
        idd=input("Enter your row id:")
        sql="select*from bhavesh where id=%s"
        val=(idd,)
        try:
           cursor.execute(sql,val)
           data=cursor.fetchall()
           for x in data:
               name=x[1]
               phone=x[2]
               print("1.Update name\n2.Update phone")
               ch=int(input("Enter your choice:"))
               if(ch==1):
                   name=input("Enter the new name you want:")
               elif(ch==2):
                   phone=input("Enter the new number you want:")
               else:
                   print("wrong input")
                   menu()
               sql="update bhavesh set name=%s,phone=%s where id=%s"
               val=(name,phone,idd)
               try:
                   cursor.execute(sql,val)
                   conn.commit()
                   print("Updated Successfully")
                   menu()
               except Exception as e:
                   print("error")
                   menu()
        except Exception as e:
            print("error")
            menu()
menu()