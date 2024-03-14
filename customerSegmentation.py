import mysql.connector
import matplotlib.pyplot as plt
from tkinter import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_project"
)
total=0
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customer_detail")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  total=total+1

print("*************************************************************************************")
print("\n")
#print (total)



def switch():
    
    
    print("Enter 1 for Segementation of customers on basis of their  Gender \nEnter 2 for Segementation of customers on basis of their Age \nEnter 3 for Segementation of customers on basis of their Interest \n")

    option = int(input("your option : "))


    if option == 1:
        male=0        
        print("\nList of all the Male customers are given below:-\n")
        sql = "SELECT * FROM customer_detail WHERE Gender ='Male'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
         print(x)
         male=male+1
          

        print (male)
        print("\nList of all the Female customers are given below:-\n")
        sql = "SELECT * FROM customer_detail WHERE Gender ='Female'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
         print(x)


        per=(male*100)/total
        #print (per)
        perf=100-per
        #print (perf)
        #subject='male','female'
        #graph1=[per,perf]
        #explode=(0,0)
        #plt.pie(graph1,explode=explode,labels=subject,autopct='%1.2f%%',shadow=True)
        #plt.axis('equal')
        #plt.show()
        def run():
         subject='male','female'
         graph1=[per,perf]
         explode=(0,0)
         plt.pie(graph1,explode=explode,labels=subject,autopct='%1.2f%%',shadow=True)
         plt.axis('equal')
         plt.show()
   #function to be performed
        screen=Tk()
        screen.title("Welcome to customer segmentation System")
        screen.geometry("500x500")
        welcome_text=Label(text="Segmentation on basis of gender",fg="white",bg="blue")
        welcome_text.pack()
        click_me=Button(text="click for Pie graph",fg="White",bg="Black",height=3,width=18,command=run)
        click_me.place(x=10,y=20)
        screen.mainloop()
 

    elif option == 2:

         #print("\nEnter 1 for below 18\nEnter 2 for 18-60\nEnter 3 for above 60\n")
         #c = int(input("Enter your choice : "))
           
         #if c == 1:
            age1=0
            age2=0
            age3=0
            sql = "SELECT * FROM customer_detail WHERE Age <18"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
 
            for x in myresult:
              print(x)
              age1=age1+1
         #if c == 2:
            print("_______________________")
            sql = "SELECT * FROM customer_detail WHERE Age >=18 and Age<=60"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            for x in myresult:
              print(x)
              age2=age2+1   
         #if c == 3: 
            print("_____________________________")
            sql = "SELECT * FROM customer_detail WHERE Age >60" 
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            for x in myresult:
              print(x)
              age3=age3+1
         
            age1=(age1*100)/total
            age2=(age2*100)/total
            age3=(age3*100)/total
            #subject='age less than 18','age between 18 to 60','age greater than 60'   
            #graph2=[age1,age2,age3]
            #explode=(0,0,0)
            #plt.pie(graph2,explode=explode,labels=subject,autopct='%1.2f%%',shadow=True)
            #plt.axis('equal')
            #plt.show()   
            def run():
              subject='age less than 18','age between 18 to 60','age greater than 60'   
              graph2=[age1,age2,age3]
              explode=(0,0,0)
              plt.pie(graph2,explode=explode,labels=subject,autopct='%1.2f%%',shadow=True)
              plt.axis('equal')
              plt.show()   


              #function to be performed
            screen2=Tk()
            screen2.title("Welcome to customer segmentation System")
            screen2.geometry("500x500")
            welcome_text=Label(text="Segmentation on basis of age",fg="white",bg="blue")
            welcome_text.pack()
            click_me2=Button(text="click for Pie graph",fg="White",bg="Black",height=3,width=18,command=run)
            click_me2.place(x=10,y=20)
            screen2.mainloop()
            






































    elif option == 3:
        
        i1=0
        i2=0
        i3=0
        i4=0
        i5=0
        print("We have only 5 options of interest in our database")
        #print("\nEnter 1 for listing customers whose Interest is Books \nEnter 2 for listing customers whose Interest is Sports\nEnter 3 listing customers whose Interest is for Musical Instruments\nEnter 4 for listing customers whose Interest is Dance\nEnter 5 for listing customers whose Interest is Home decor\n")
        #d = int(input("Enter your choice : "))

        #if d == 1:
        sql = "SELECT * FROM customer_detail WHERE Interest='Books'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
         print(x)
         i1=i1+1
        #if d == 2:
        print("_____________________________________________________________________________________")  
        sql = "SELECT * FROM customer_detail WHERE Interest='Sports'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
         print(x)
         i2=i2+1 
               

        #if d == 3:
        print("_____________________________________________________________________________________")
        sql = "SELECT * FROM customer_detail WHERE Interest='Musical Instruments'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
         print(x)
         i3=i3+1

        #if d == 4:
        print("_____________________________________________________________________________________")
        sql = "SELECT * FROM customer_detail WHERE Interest='Dance'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
         print(x)
         i4=i4+1
        #if d == 5:
        print("_____________________________________________________________________________________")
        sql = "SELECT * FROM customer_detail WHERE Interest='Home Decor'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
         print(x)               
         i5=i5+1


        i1=(i1*100)/total
        i2=(i2*100)/total
        i3=(i3*100)/total
        i4=(i4*100)/total
        i5=(i5*100)/total
        #subject='Books','Sports','Musical Instruments','Dance','Decor'   
        #graph3=[i1,i2,i3,i4,i5]
        #explode=(0,0,0,0,0)
        #plt.pie(graph3,explode=explode,labels=subject,autopct='%1.2f%%',shadow=True)
        #plt.axis('equal')
        #plt.show()   
        def run():
          subject='Books','Sports','Musical Instruments','Dance','Decor'   
          graph3=[i1,i2,i3,i4,i5]
          explode=(0,0,0,0,0)
          plt.pie(graph3,explode=explode,labels=subject,autopct='%1.2f%%',shadow=True)
          plt.axis('equal')
          plt.show()   

#function to be performed
        screen=Tk()
        screen.title("Welcome to customer segmentation system")
        screen.geometry("500x500")
        welcome_text=Label(text="segmentation on the basis of interest",fg="white",bg="blue")
        welcome_text.pack()
        click_me=Button(text="click for Pie graph",fg="White",bg="Black",height=3,width=18,command=run)
        click_me.place(x=10,y=20)
        screen.mainloop()

 
    else:
      print("You entered an invalid option,Please enter valid option only!")

switch()
print("***************************************************************************")