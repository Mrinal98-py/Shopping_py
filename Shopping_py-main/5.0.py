#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~D_I_G_I_T_A_L~~~~~~~~~M_A_L_L~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import Image, ImageTk

global userid
global grandtotal
global values


#___________________________________________________________________________________MAIN_WINDOW___________________________________________________________________________________________________


root = Tk()


photo_cust = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/cu.png")
photo_shopk = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/sp.png")
photo_bg_mart = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/MART.png")


def main_window():

    main = tk.Canvas(root, width = 1000, height = 750, bg='Beige' ,relief='raised')
    main.pack(expand = YES, fill = BOTH)

    button_bg = tk.Button(root,image=photo_bg_mart, bg='white', fg='black', font=('chiller', 10 , 'bold'),relief = 'flat', command=logincust)
    main.create_window(500, 365, window=button_bg )

    button_cu = tk.Button(image=photo_cust, bg='white', fg='black', font=('chiller', 10 , 'bold'),relief = 'flat', command=logincust)
    main.create_window(250, 730, window=button_cu)

    button_sp = tk.Button(root,image=photo_shopk, bg='white', fg='black', font=('chiller', 10, 'bold'),relief = 'flat', command=loginsp)
    main.create_window(750, 730, window=button_sp)




#___________________________________________________________________________M_A_I_N_T_A_I_N_____S_T_O_C_K_S________________________________________________________________________________________

photo_bg_SP_sp = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/user (5).png")
photo_INSERT = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/INSERT.png")

def spmanatin():

    #___________I_N_S_E_R_T___________
    def insert():
    # info :/
        proid= pro_id1.get()
        name = name1.get()
        qty = qty1.get()
        price = price1.get()
        category = category1.get()
        
        if(name=="" or qty=="" or price=="" or  category=="" ):
            MessageBox.showinfo("Status","All Fields are required");
        else:
           global conn
           mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
           cursor = mydb.cursor();
           cursor.execute("insert into products(`Product_name`,`Product_qty`,`Product_price`,`Category`) values('"+name+"','"+qty+"','"+price+"','"+category+"')");
           cursor.execute("commit");
           name1.delete(0,'end')
           qty1.delete(0,'end')
           price1.delete(0,'end')
           category1.delete(0,'end')
           
           show()
           
           MessageBox.showinfo("Status","Inserted");
           mydb.close()



    #______D_E_L_E_T_E_______

    def delete():
        proid= pro_id1.get()
        name = name1.get()
        qty = qty1.get()
        price = price1.get()
        category = category1.get()
        if(proid==""):
            MessageBox.showinfo("Status","""Error !!!
    Sno is compolsary for delete""")
        else:
            mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
            cursor = mydb.cursor()
            cursor.execute("delete from products where product_id='"+proid+"'")
            cursor.execute("commit")
            
            pro_id1.delete(0,'end')

            show()
            MessageBox.showinfo("Status","Deleted");
            mydb.close()
            


    #_____U_P_D_A_T_E___________

    def update():
        proid= pro_id1.get()
        name = name1.get()
        qty = qty1.get()
        price = price1.get()
        category = category1.get()
        
        if(proid==""):
         MessageBox.showinfo("Update Info","give name")
        else:
         mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
         cursor = mydb.cursor()
         cursor.execute("update products set product_name='"+name+"',product_Qty='"+qty+"',product_price='"+price+"' where product_id='"+proid+"'",)
         cursor.execute("commit")
         pro_id1.delete(0,'end')
         name1.delete(0,'end')
         qty1.delete(0,'end')
         price1.delete(0,'end')
         category1.delete(0,'end')


         show()
         
         MessageBox.showinfo("Update Info","done")
         mydb.close()
         


    #______G_E_T_______


    def get():
        proid= pro_id1.get()
        name = name1.get()
        qty = qty1.get()
        price = price1.get()
        category = category1.get()
        
        mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
        cursor = mydb.cursor()
        cursor.execute("select *  from products where product_id='"+proid+"'")
        
        rows = cursor.fetchall()
        
        name1.delete(0,'end')
        qty1.delete(0,'end')
        price1.delete(0,'end')
        category1.delete(0,'end')
        
        for row in rows:
            name1.insert(0,row[1])
            qty1.insert(0,row[2])
            price1.insert(0,row[3])
            category1.insert(0,row[4])
    #______S_H_O_W______________
    def show():
        top_SHOW=Toplevel()
        mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
        cursor = mydb.cursor()
        cursor.execute("select * from products")
        
        rows = cursor.fetchall()
        print(rows)
        ae1 = Label(top_SHOW,text='PRODUCT ID',font=("bold",10))
        ae2 = Label(top_SHOW,text='PRODUCT NAME',font=("bold",10))
        ae3 = Label(top_SHOW,text='QUANTITY',font=("bold",10))
        ae4 = Label(top_SHOW,text='PRICE',font=("bold",10))
        ae5 = Label(top_SHOW,text='CREATED',font=("bold",10))
        ae6 = Label(top_SHOW,text='CATEGORY',font=("bold",10))


        ae1.grid(row=0, column=0)
        ae2.grid(row=0, column=1)
        ae3.grid(row=0, column=2)
        ae4.grid(row=0, column=3)
        ae5.grid(row=0, column=5)
        ae6.grid(row=0, column=4)
    


        
        i=1
        for row in rows:     
            for j in range(0,len(row)):
                e =Entry(top_SHOW,width=20) 
                e.grid(row=i, column=j) 
                e.insert(END, row[j])
            i=i+1
            
        mydb.close()
        

            

    top2=Toplevel()
       
    canvas_mart1 = tk.Canvas(top2, width = 700, height = 350, bg='white' ,relief='raised')
    canvas_mart1.pack()

    bg = tk.Button(canvas_mart1,image = photo_bg_SP_sp,relief = 'flat')
    canvas_mart1.create_window(0, 0, window=bg, anchor = NW )

    pro_id1 =Entry(top2)
    pro_id1.place(x=225,y=33);  
     
    name1 = Entry(top2)
    name1.place(x=225,y=61); 

    qty1 = Entry(top2)
    qty1.place(x=225,y=91); 

    price1 = Entry(top2)
    price1.place(x=225,y=120);

    category1 = Entry(top2)
    category1.place(x=225,y=149);
    

    insert = Button(top2,text="Insert" ,command=insert)
    insert.place(x=20,y=270)

    delete = Button(top2,text="Delete",command=delete)
    delete.place(x=100,y=270);

    update= Button(top2,text="Update",command=update)
    update.place(x=180,y=270)

    get = Button(top2,text="Get",command=get)
    get.place(x=260,y=270)

    show()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#_______________________________________________________________________________LOGIN_TO_SHOPKEEPER_____________________________________________________________________________________________________

photo_cust2= PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/2.png")
    
def loginsp(): 
    top = Toplevel(root)


    def info_check(event):
        conn = mysql.connect(user='root', password='1234', host='localhost', database='demo')
        cursor= conn.cursor()
        sql = ("SELECT * from SHOP where NAME='"+entry1.get()+"'and PASSWORD='"+entry2.get()+"'and SP_ID='"+entry3.get()+"'");
        cursor.execute(sql)
        result = cursor.fetchall();
        conn.close()
        if result==[]:
           MessageBox.showinfo("Update Info","NO RECORDS")
        else:
           root.deiconify()
           top.destroy()
           spmanatin()



    def command2():
        top.destroy()


    canvas_mart = tk.Canvas(top, width = 500, height = 500, bg='white' ,relief='raised')
    canvas_mart.pack()

    bg = tk.Button(canvas_mart,image = photo_cust2,relief = 'flat')
    canvas_mart.create_window(0, 0, window=bg, anchor = NW )

    lbl3 = Label(top, text =' SP ID:' ,background='light grey', font=('Helvetica' , 10))
    canvas_mart.create_window(250, 100, window=lbl3 )

    entry3 = Entry(top)
    canvas_mart.create_window(250, 130, window=entry3)

    lbl1 = Label(top, text =' USERNAME:' ,background='light grey', font=('Helvetica' , 10))
    canvas_mart.create_window(250, 160, window=lbl1)
    
    entry1 = Entry(top)
    canvas_mart.create_window(250, 190, window=entry1)
    
    lbl2 = Label(top, text =' PASSWORD:' ,background='light grey', font=('Helvetica' , 10))
    canvas_mart.create_window(250, 220, window=lbl2 )
    
    entry2=Entry(top , show="*")
    canvas_mart.create_window(250, 250, window=entry2 )
    
    button2=Button(top, text ='Cancel' , command = lambda:command2())
    canvas_mart.create_window(250, 280, window=button2 ) 

    entry2.bind('<Return>' , info_check)
        
    
   

#_________________________________________________________________________________LOGIN_CUSTOMER__________________________________________________________________________________________________

photo_cust1 = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/1.png")

def logincust():
    top1 = Toplevel()


    
    def info_check(event):
        
        global userid
        conn = mysql.connect(user='root', password='1234', host='localhost', database='demo')
        cursor= conn.cursor()
        sql = ("SELECT * from user where user_name='"+entry1.get()+"'or user_password='"+entry2.get()+"'");
        cursor.execute(sql)
        result = cursor.fetchall();
        print(type(result[0][1]))
        conn.close()
        if result==[]:
           MessageBox.showinfo("Update Info","NO RECORDS")
        elif result[0][1]== entry1.get() and result[0][6] != entry2.get() :
            MessageBox.showinfo("Update Info","WRONG PASSWORD")
        elif result[0][1] != entry1.get() and result[0][6] == entry2.get() :
            MessageBox.showinfo("Update Info","NO RECORDS")
        else:
            userid = result[0][0]
            print(userid)
            root.deiconify()
            top1.destroy()
            main_mart()


           
    def command2():
        top1.destroy()

    canvas_mart = tk.Canvas(top1, width = 500, height = 500, bg='white' ,relief='raised')
    canvas_mart.pack()

    bg_sp = tk.Button(canvas_mart,image = photo_cust1,relief = 'flat')
    canvas_mart.create_window(0, 0, window=bg_sp, anchor = NW )


    lbl1 = Label(top1, text =' Username:' , font=('Helvetica' , 10))
    canvas_mart.create_window(250, 20, window=lbl1)
    
    entry1 = Entry(top1)
    canvas_mart.create_window(250, 50, window=entry1)
    
    lbl2 = Label(top1, text =' Password:' , font=('Helvetica' , 10))
    canvas_mart.create_window(250, 80, window=lbl2 )
    
    entry2=Entry(top1 , show="*")
    canvas_mart.create_window(250, 110, window=entry2 )
    
    button2=Button(top1, text ='Cancel' , command = lambda:command2())
    canvas_mart.create_window(250, 140, window=button2 ) 

    button3 = Button(top1, text ='Create New ID' , command = new_user)
    canvas_mart.create_window(250, 170, window=button3 )
    entry2.bind('<Return>' ,info_check)


#______________________________________________________________________N_E_W_____U_S_E_R____________________________________________________________________________________________________
photo_cust_sp= PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/user (6).png")
def  new_user():

    top_new_user = Toplevel()
   
    def insert_values():
      user_name1=username_entry.get()
      user_email=user_email_entry.get()
      user_phone=user_phone_entry.get()
      user_address=user_address_entry.get()
      user_password=user_password_entry.get()

      
      conn = mysql.connect(user='root', password='1234', host='localhost', database='demo')
      cursor= conn.cursor()
      sql = ("SELECT * from user ");
      cursor.execute(sql)
      result = cursor.fetchall();

      
      if (username_entry.get()=="" or user_password_entry.get()=="" ):
         MessageBox.showinfo("<ERROR!>","All Fields are required");
      else:
         mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
         cursor = mydb.cursor();
         cursor.execute("insert into user(user_name,User_email,User_phone,User_address,user_password) values('"+user_name1+"','"+user_email+"','"+user_phone+"','"+user_address+"','"+user_password+"')");
         cursor.execute("commit");
         MessageBox.showinfo("Status","Inserted");
         top_new_user.destroy()
         mydb.close()

         logincust()

    canvas_mart1 = tk.Canvas(top_new_user, width = 700, height = 350, bg='white' ,relief='raised')
    canvas_mart1.pack()

    bg = tk.Button(canvas_mart1,image = photo_cust_sp,relief = 'flat')
    canvas_mart1.create_window(0, 0, window=bg, anchor = NW )



    username_entry = Entry(top_new_user)
    username_entry.place(x=150,y=50);

    user_email_entry = Entry(top_new_user)
    user_email_entry.place(x=150,y=80);

    user_phone_entry = Entry(top_new_user)
    user_phone_entry.place(x=150,y=110);

    user_address_entry = Entry(top_new_user)
    user_address_entry.place(x=150,y=140);

    user_password_entry = Entry(top_new_user,show="*")
    user_password_entry.place(x=150,y=170);


    button_enter=Button(top_new_user, text ='DONE' ,command=insert_values)
    button_enter.place(x=150,y=195)



#______________________________________________________________________C_H_E_C_K___O_U_T____________________________________________________________________________________________________

def check_out():
    global userid
    global values
    global grandtotal
   
    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")

   
    cursor = mydb.cursor();
    cursor_table1 = mydb.cursor();

    cursor.execute("select sum(total) from cart");
    grandtotal = cursor.fetchall()
   
       
    cursor.execute("insert into orders(user_id,grand_total) values('"+str(userid)+"','"+str(int(grandtotal[0][0]))+"')");
    orderid = cursor.lastrowid
    cursor.execute("commit");
   

   
    cursor_table1.execute('SELECT Product_id, mrp, quantity from cart')
    for row in cursor_table1.fetchall():
        cursor.execute("INSERT INTO order_item(order_id , product_id , User_id , quantity ) VALUES ('"+str(orderid)+"','"+str(row[0])+"','"+str(userid)+"','"+str(row[2])+"')");
       
        ## below minus the stock in product table
        cursor.execute("select Product_qty from products where product_id = '"+str(row[0])+"'");
        oldvalue = cursor.fetchall()[0][0];
       
        newvalue = int(oldvalue)-int(row[2])
        cursor.execute("update products set Product_qty = '"+str(newvalue)+"' where product_id = '"+str(row[0])+"'");

    cursor.execute("select * from cart");
    values = cursor.fetchall();
    print(values)
    cursor.execute("commit");
    cursor.execute("TRUNCATE cart");
   
    mydb.close()
    final_bill()
 
def My_account():
    
    global userid
    global values
    global grandtotal
    
    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo") 
    cursor = mydb.cursor();
    cursor.execute("select * from oder_item where='"+str(userid)+"'");
    oldvalue = cursor.fetchall();
    print(oldvalue)
    
    my = Toplevel()
    
    ae1 = Label(my,text='S_NO',font=("bold",10))
    ae2 = Label(my,text='MRP',font=("bold",10))
    ae3 = Label(my,text='QUANTITY',font=("bold",10))
    ae4 = Label(my,text='TOTAL',font=("bold",10))

    
    ae1.grid(row=0, column=0)
    ae2.grid(row=0, column=1)
    ae3.grid(row=0, column=2)
    ae4.grid(row=0, column=3)

    c=0
    i=1
    for row in values:
        a = Label(my,text=i,font=("bold",10))
        a.grid(row=i, column=0)
        
        for j in range(1,len(row)):
            e = Entry(my, width=10) 
            e.grid(row=i, column=j) 
            e.insert(END, row[j])
        i=i+1
    c=0+i
    print(c)
    ae5 =  Label(my,text='Grand Total = ',font=("bold",10))
    ae6 =  Label(my,text= grandtotal[0][0],background='White',font=("bold",10))


    ae5.grid(row=c, column=2)
    ae6.grid(row=c, column=3)

        
    my_w.mainloop()
    
    
#______________________________________________________________________F_I_N_A_L____B_I_L_L____________________________________________________________________________________________________

def final_bill():
    
    global values
    global grandtotal
   
    my_w = Toplevel()
    my_w.geometry("300x750")
   
    ae1 = Label(my_w,text='S_NO',font=("bold",10))
    ae2 = Label(my_w,text='MRP',font=("bold",10))
    ae3 = Label(my_w,text='QUANTITY',font=("bold",10))
    ae4 = Label(my_w,text='TOTAL',font=("bold",10))

   
    ae1.grid(row=0, column=0)
    ae2.grid(row=0, column=1)
    ae3.grid(row=0, column=2)
    ae4.grid(row=0, column=3)

    c=0
    i=1
    for row in values:
        a = Label(my_w,text=i,font=("bold",10))
        a.grid(row=i, column=0)
       
        for j in range(1,len(row)):
            e = Entry(my_w, width=10)
            e.grid(row=i, column=j)
            e.insert(END, row[j])
        i=i+1
    c=0+i
    print(c)
    ae5 =  Label(my_w,text='Grand Total = ',font=("bold",10))
    ae6 =  Label(my_w,text= grandtotal[0][0],background='White',font=("bold",10))


    ae5.grid(row=c, column=2)
    ae6.grid(row=c, column=3)

       
    my_w.mainloop()


    

    


#______________________________________________________________________M_A_I_N____M_A_R_T____________________________________________________________________________________________________


photo_fruit= PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/2(1).png") 
photo_milk = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/4.png")
photo_stationary = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/5.png")
photo_vegetable = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/3.png")
photo_bg_main_mart = PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/Untitled design (5).png")
photo_check_out= PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/check out (1).png")
photo_sikkim= PhotoImage(file = r"C:/Py/program XII project/ITEMS/sp/SIKKIM (2).png")



def main_mart():
    top_mart = Toplevel()
    canvas_mart = tk.Canvas(top_mart, width = 825, height = 800, bg='white' ,relief='raised')
    canvas_mart.pack()

    bg = tk.Button(canvas_mart,image = photo_bg_main_mart,relief = 'flat')
    canvas_mart.create_window(0, 0, window=bg, anchor = NW )
    
    fruit = tk.Button(canvas_mart,image = photo_fruit,relief = 'flat' , command = fruits)
    canvas_mart.create_window(190, 130, window=fruit )

    milk = tk.Button(canvas_mart,image = photo_milk, relief = 'flat', command = dairys )
    canvas_mart.create_window(640, 130, window=milk)

    sta = tk.Button(canvas_mart,image = photo_stationary, relief = 'flat', command = stationary)
    canvas_mart.create_window(190, 622, window=sta)

    veg = tk.Button(canvas_mart,image = photo_vegetable, relief = 'flat', command = vegetable)
    canvas_mart.create_window(640, 622, window=veg)
    
    sikki = tk.Button(canvas_mart,image=photo_sikkim, relief = 'flat', command = sikkim)
    canvas_mart.create_window(413, 376, window=sikki)



    check_out1 = tk.Button(canvas_mart,image=photo_check_out, relief = 'flat', command = check_out)
    canvas_mart.create_window(413, 780, window=check_out1)





photo_cart = PhotoImage(file = r"C:/Py/program XII project/ITEMS/Untitled design (2).png")
photo_bg_fruit = PhotoImage(file = r"C:/Py/program XII project/ITEMS/2.png")
#______________________________________________________________________A_D_D___T_O____C_A_R_T________________________________________________________________________________________________

def addtocart(a,proid,price,qty):
    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
    cursor = mydb.cursor();
    cursor.execute("select * from products where product_id='"+str(proid)+"'");
    Qty = cursor.fetchall()
    
    a.delete(0,'end')
    
    if Qty[0][2]<=0: 
        MessageBox.showinfo("Status","Product Out Of Stock");
        mydb.close()

    elif int(qty) > Qty[0][2]:
        MessageBox.showinfo("Status","Only '"+str(Qty[0][2])+"' ! in Stock");
        mydb.close()
        

    else:

        cursor.execute("select Product_id from cart where Product_id='"+str(proid)+"'");
        records = cursor.fetchall()

        total =  int(price) * int(qty)
        print (total)
        if(len(records)==0):
            cursor.execute("insert into cart values('"+str(proid)+"','"+str(price)+"','"+str(qty)+"','"+str(total)+"')");
            cursor.execute("commit");
            MessageBox.showinfo("Status","Product Added to Cart");
            mydb.close()


        else:
            cursor.execute("update cart set quantity = '"+str(qty)+"', total = '"+str(total)+"'  where Product_id = '"+str(proid)+"'");
            cursor.execute("commit");
            MessageBox.showinfo("Status","Product Updated in Cart");
            mydb.close()

#______________________________________________________________________SIKKIM____________________________________________________________________________________________________
def sikkim():
    top_1 = Toplevel()
    
    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
    cursor = mydb.cursor();
    cursor.execute("select Product_id,Product_name,Product_price from products where category= 'sikkim'");
    fruitslist = cursor.fetchall() 
    mydb.close()
    
    top_1.configure(background='white')
    top_1.columnconfigure(0, weight=1)
    

    ae1 = Label(top_1,text=fruitslist[0][1],background='white',font=("bold",10))
    ae2 = Label(top_1,text=fruitslist[0][2],background='white',font=("bold",10))
    ae3 = Entry(top_1)
    ae4 = Button(top_1,image = photo_cart,command=lambda: addtocart(ae3,fruitslist[0][0],fruitslist[0][2],ae3.get()))

   
    ae1.grid(row=0, column=0)
    ae2.grid(row=0, column=1)
    ae3.grid(row=0, column=2)
    ae4.grid(row=0, column=3)


    be1 = Label(top_1,text=fruitslist[1][1],background='white',font=("bold",10))
    be2 = Label(top_1,text=fruitslist[1][2],background='white',font=("bold",10))
    be3 = Entry(top_1)
    be4 = Button(top_1,image = photo_cart,command=lambda: addtocart(be3,fruitslist[1][0],fruitslist[1][2],be3.get()))
   
    be1.grid(row=1, column=0)
    be2.grid(row=1, column=1)
    be3.grid(row=1, column=2)
    be4.grid(row=1, column=3)

    ce1 = Label(top_1,text=fruitslist[2][1],background='white',font=("bold",10))
    ce2 = Label(top_1,text=fruitslist[2][2],background='white',font=("bold",10))
    ce3 = Entry(top_1)
    ce4 = Button(top_1,image = photo_cart,command=lambda: addtocart(ce3,fruitslist[2][0],fruitslist[2][2],ce3.get()))
   
    ce1.grid(row=2, column=0)
    ce2.grid(row=2, column=1)
    ce3.grid(row=2, column=2)
    ce4.grid(row=2, column=3)

    de1 = Label(top_1,text=fruitslist[3][1],background='white',font=("bold",10))
    de2 = Label(top_1,text=fruitslist[3][2],background='white',font=("bold",10))
    de3 = Entry(top_1)
    de4 = Button(top_1,image = photo_cart,command=lambda: addtocart(de3,fruitslist[3][0],fruitslist[3][2],de3.get()))
   
    de1.grid(row=3, column=0)
    de2.grid(row=3, column=1)
    de3.grid(row=3, column=2)
    de4.grid(row=3, column=3)

    ee1 = Label(top_1,text=fruitslist[4][1],background='white',font=("bold",10))
    ee2 = Label(top_1,text="Rs."+str(fruitslist[4][2]),background='white',font=("bold",10))
    ee3 = Entry(top_1)
    ee4 = Button(top_1,image = photo_cart,command=lambda: addtocart(ee3,fruitslist[4][0],fruitslist[4][2],ee3.get()))
   
    ee1.grid(row=4, column=0)
    ee2.grid(row=4, column=1)
    ee3.grid(row=4, column=2)
    ee4.grid(row=4, column=3)

    fe1 = Label(top_1,text=fruitslist[5][1],background='white',font=("bold",10))
    fe2 = Label(top_1,text=fruitslist[5][2],background='white',font=("bold",10))
    fe3 = Entry(top_1)
    fe4 = Button(top_1,image = photo_cart,command=lambda: addtocart(fe3,fruitslist[5][0],fruitslist[5][2],fe3.get()))
   
    fe1.grid(row=5, column=0)
    fe2.grid(row=5, column=1)
    fe3.grid(row=5, column=2)
    fe4.grid(row=5, column=3)

    

#______________________________________________________________________F_R_U_I_T____M_A_R_T____________________________________________________________________________________________________
def fruits():
    top_fruits = Toplevel()

    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
    cursor = mydb.cursor();
    cursor.execute("select Product_id,Product_name,Product_price from products where category= 'fruits'");
    fruitslist = cursor.fetchall() 
    mydb.close()
    top_fruits.configure(background='white')
    top_fruits.columnconfigure(0, weight=1)
    
##    image = Image.open(r"C:/Users/Anurag/Desktop/Project/Untitled design/1.png")
##    photo = ImageTk.PhotoImage(image)
##    ae5 = Label(top_fruits, image = photo)
##    ae5.image = photo
         
    ae1 = Label(top_fruits,text=fruitslist[0][1],background='white',font=("bold",10))
    ae2 = Label(top_fruits,text="Rs."+str(fruitslist[0][2]),background='white',font=("bold",10))
    ae3 = Entry(top_fruits)
    ae4 = Button(top_fruits,image = photo_cart,command=lambda: addtocart(ae3,fruitslist[0][0],fruitslist[0][2],ae3.get()))

   
    ae1.grid(row=0, column=0)
    ae2.grid(row=0, column=1)
    ae3.grid(row=0, column=2)
    ae4.grid(row=0, column=3)
##    ae5.grid(row=0, column=0)
    

    be1 = Label(top_fruits,text=fruitslist[1][1],background='white',font=("bold",10))
    be2 = Label(top_fruits,text="Rs."+str(fruitslist[1][2]),background='white',font=("bold",10))
    be3 = Entry(top_fruits)
    be4 = Button(top_fruits,image = photo_cart,command=lambda: addtocart(be3,fruitslist[1][0],fruitslist[1][2],be3.get()))
   
    be1.grid(row=1, column=0)
    be2.grid(row=1, column=1)
    be3.grid(row=1, column=2)
    be4.grid(row=1, column=3)

    ce1 = Label(top_fruits,text=fruitslist[2][1],background='white',font=("bold",10))
    ce2 = Label(top_fruits,text="Rs."+str(fruitslist[2][2]),background='white',font=("bold",10))
    ce3 = Entry(top_fruits)
    ce4 = Button(top_fruits,image = photo_cart,command=lambda: addtocart(ce3,fruitslist[2][0],fruitslist[2][2],ce3.get()))
   
    ce1.grid(row=2, column=0)
    ce2.grid(row=2, column=1)
    ce3.grid(row=2, column=2)
    ce4.grid(row=2, column=3)

    de1 = Label(top_fruits,text=fruitslist[3][1],background='white',font=("bold",10))
    de2 = Label(top_fruits,text="Rs."+str(fruitslist[3][2]),background='white',font=("bold",10))
    de3 = Entry(top_fruits)
    de4 = Button(top_fruits,image = photo_cart,command=lambda: addtocart(de3,fruitslist[3][0],fruitslist[3][2],de3.get()))
   
    de1.grid(row=3, column=0)
    de2.grid(row=3, column=1)
    de3.grid(row=3, column=2)
    de4.grid(row=3, column=3)

    ee1 = Label(top_fruits,text=fruitslist[4][1],background='white',font=("bold",10))
    ee2 = Label(top_fruits,text="Rs."+str(fruitslist[4][2]),background='white',font=("bold",10))
    ee3 = Entry(top_fruits)
    ee4 = Button(top_fruits,image = photo_cart,command=lambda: addtocart(ee3,fruitslist[4][0],fruitslist[4][2],ee3.get()))
   
    ee1.grid(row=4, column=0)
    ee2.grid(row=4, column=1)
    ee3.grid(row=4, column=2)
    ee4.grid(row=4, column=3)

    fe1 = Label(top_fruits,text=fruitslist[5][1],background='white',font=("bold",10))
    fe2 = Label(top_fruits,text="Rs."+str(fruitslist[5][2]),background='white',font=("bold",10))
    fe3 = Entry(top_fruits)
    fe4 = Button(top_fruits,image = photo_cart,command=lambda: addtocart(fe3,fruitslist[5][0],fruitslist[5][2],fe3.get()))
   
    fe1.grid(row=5, column=0)
    fe2.grid(row=5, column=1)
    fe3.grid(row=5, column=2)
    fe4.grid(row=5, column=3)
    
 

#_______________________________________________________________________________D_A_R_I_Y_____________________________________________________________________________________________________
photo_d = PhotoImage(file = r"C:/Py/program XII project/ITEMS/3.png") 
def dairys():
    
    top_dairy = Toplevel()
    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
    cursor = mydb.cursor();
    cursor.execute("select Product_id,Product_name,Product_price from products where category= 'dairy'");
    fruitslist = cursor.fetchall() 
    mydb.close()
    top_dairy.configure(background='white')
    top_dairy.columnconfigure(0, weight=1)
    

    ae1 = Label(top_dairy,text=fruitslist[0][1],background='white',font=("bold",10))
    ae2 = Label(top_dairy,text="Rs."+str(fruitslist[0][2]),background='white',font=("bold",10))
    ae3 = Entry(top_dairy)
    ae4 = Button(top_dairy,image = photo_cart,command=lambda: addtocart(ae3,fruitslist[0][0],fruitslist[0][2],ae3.get()))

   
    ae1.grid(row=0, column=0)
    ae2.grid(row=0, column=1)
    ae3.grid(row=0, column=2)
    ae4.grid(row=0, column=3)
    

    be1 = Label(top_dairy,text=fruitslist[1][1],background='white',font=("bold",10))
    be2 = Label(top_dairy,text="Rs."+str(fruitslist[1][2]),background='white',font=("bold",10))
    be3 = Entry(top_dairy)
    be4 = Button(top_dairy,image = photo_cart,command=lambda: addtocart(be3,fruitslist[1][0],fruitslist[1][2],be3.get()))
   
    be1.grid(row=1, column=0)
    be2.grid(row=1, column=1)
    be3.grid(row=1, column=2)
    be4.grid(row=1, column=3)

    ce1 = Label(top_dairy,text=fruitslist[2][1],background='white',font=("bold",10))
    ce2 = Label(top_dairy,text="Rs."+str(fruitslist[2][2]),background='white',font=("bold",10))
    ce3 = Entry(top_dairy)
    ce4 = Button(top_dairy,image = photo_cart,command=lambda: addtocart(ce3,fruitslist[2][0],fruitslist[2][2],ce3.get()))
   
    ce1.grid(row=2, column=0)
    ce2.grid(row=2, column=1)
    ce3.grid(row=2, column=2)
    ce4.grid(row=2, column=3)
    
    de1 = Label(top_dairy,text=fruitslist[3][1],background='white',font=("bold",10))
    de2 = Label(top_dairy,text="Rs."+str(fruitslist[3][2]),background='white',font=("bold",10))
    de3 = Entry(top_dairy)
    de4 = Button(top_dairy,image = photo_cart,command=lambda: addtocart(de3,fruitslist[3][0],fruitslist[3][2],de3.get()))
   
    de1.grid(row=3, column=0)
    de2.grid(row=3, column=1)
    de3.grid(row=3, column=2)
    de4.grid(row=3, column=3)

    ee1 = Label(top_dairy,text=fruitslist[4][1],background='white',font=("bold",10))
    ee2 = Label(top_dairy,text="Rs."+str(fruitslist[4][2]),background='white',font=("bold",10))
    ee3 = Entry(top_dairy)
    ee4 = Button(top_dairy,image = photo_cart,command=lambda: addtocart(ee3,fruitslist[4][0],fruitslist[4][2],ee3.get()))
   
    ee1.grid(row=4, column=0)
    ee2.grid(row=4, column=1)
    ee3.grid(row=4, column=2)
    ee4.grid(row=4, column=3)

    fe1 = Label(top_dairy,text=fruitslist[5][1],background='white',font=("bold",10))
    fe2 = Label(top_dairy,text="Rs."+str(fruitslist[5][2]),background='white',font=("bold",10))
    fe3 = Entry(top_dairy)
    fe4 = Button(top_dairy,image = photo_cart,command=lambda: addtocart(fe3,fruitslist[5][0],fruitslist[5][2],fe3.get()))
   
    fe1.grid(row=5, column=0)
    fe2.grid(row=5, column=1)
    fe3.grid(row=5, column=2)
    fe4.grid(row=5, column=3)
    

#______________________________________________________________________S_T_A_T_I_O_N_A_R_Y____________________________________________________________________________________________________

def stationary():
    top_stationary = Toplevel()
    
    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
    cursor = mydb.cursor();
    cursor.execute("select Product_id,Product_name,Product_price from products where category= 'stationary'");
    fruitslist = cursor.fetchall() 
    mydb.close()
    top_stationary.configure(background='white')
    top_stationary.columnconfigure(0, weight=1)
    

         
    ae1 = Label( top_stationary,text=fruitslist[0][1],background='white',font=("bold",10))
    ae2 = Label( top_stationary,text="Rs."+str(fruitslist[0][2]),background='white',font=("bold",10))
    ae3 = Entry( top_stationary)
    ae4 = Button( top_stationary,image = photo_cart,command=lambda: addtocart(ae3,fruitslist[0][0],fruitslist[0][2],ae3.get()))

   
    ae1.grid(row=0, column=0)
    ae2.grid(row=0, column=1)
    ae3.grid(row=0, column=2)
    ae4.grid(row=0, column=3)
    

    be1 = Label( top_stationary,text=fruitslist[1][1],background='white',font=("bold",10))
    be2 = Label( top_stationary,text="Rs."+str(fruitslist[1][2]),background='white',font=("bold",10))
    be3 = Entry( top_stationary)
    be4 = Button(top_stationary,image = photo_cart,command=lambda: addtocart(be3,fruitslist[1][0],fruitslist[1][2],be3.get()))
   
    be1.grid(row=1, column=0)
    be2.grid(row=1, column=1)
    be3.grid(row=1, column=2)
    be4.grid(row=1, column=3)

    ce1 = Label( top_stationary,text=fruitslist[2][1],background='white',font=("bold",10))
    ce2 = Label( top_stationary,text="Rs."+str(fruitslist[2][2]),background='white',font=("bold",10))
    ce3 = Entry( top_stationary)
    ce4 = Button( top_stationary,image = photo_cart,command=lambda: addtocart(ce3,fruitslist[2][0],fruitslist[2][2],ce3.get()))
   
    ce1.grid(row=2, column=0)
    ce2.grid(row=2, column=1)
    ce3.grid(row=2, column=2)
    ce4.grid(row=2, column=3)

    de1 = Label( top_stationary,text=fruitslist[3][1],background='white',font=("bold",10))
    de2 = Label( top_stationary,text="Rs."+str(fruitslist[3][2]),background='white',font=("bold",10))
    de3 = Entry( top_stationary)
    de4 = Button( top_stationary,image = photo_cart,command=lambda: addtocart(de3,fruitslist[3][0],fruitslist[3][2],de3.get()))
   
    de1.grid(row=3, column=0)
    de2.grid(row=3, column=1)
    de3.grid(row=3, column=2)
    de4.grid(row=3, column=3)

    ee1 = Label( top_stationary,text=fruitslist[4][1],background='white',font=("bold",10))
    ee2 = Label( top_stationary,text="Rs."+str(fruitslist[4][2]),background='white',font=("bold",10))
    ee3 = Entry( top_stationary)
    ee4 = Button( top_stationary,image = photo_cart,command=lambda: addtocart(ee3,fruitslist[4][0],fruitslist[4][2],ee3.get()))
   
    ee1.grid(row=4, column=0)
    ee2.grid(row=4, column=1)
    ee3.grid(row=4, column=2)
    ee4.grid(row=4, column=3)

    fe1 = Label( top_stationary,text=fruitslist[5][1],background='white',font=("bold",10))
    fe2 = Label( top_stationary,text="Rs."+str(fruitslist[5][2]),background='white',font=("bold",10))
    fe3 = Entry( top_stationary)
    fe4 = Button( top_stationary,image = photo_cart,command=lambda: addtocart(fe3,fruitslist[5][0],fruitslist[5][2],fe3.get()))
   
    fe1.grid(row=5, column=0)
    fe2.grid(row=5, column=1)
    fe3.grid(row=5, column=2)
    fe4.grid(row=5, column=3)
    

#______________________________________________________________________V_E_G_E_T_A_B_L_E_____________________________________________________________________________________________________

def vegetable():
    top_vegetable = Toplevel()
    mydb = mysql.connect(host="localhost",user="root",password="1234",database="demo")
    cursor = mydb.cursor();
    cursor.execute("select Product_id,Product_name,Product_price from products where category= 'vegetables'");
    fruitslist = cursor.fetchall() 
    mydb.close()
    top_vegetable.configure(background='white')
    top_vegetable.columnconfigure(0, weight=1)
    

         
    ae1 = Label(top_vegetable,text=fruitslist[0][1],background='white',font=("bold",10))
    ae2 = Label(top_vegetable,text="Rs."+str(fruitslist[0][2]),background='white',font=("bold",10))
    ae3 = Entry(top_vegetable)
    ae4 = Button(top_vegetable,image = photo_cart,command=lambda: addtocart(ae3,fruitslist[0][0],fruitslist[0][2],ae3.get()))

   
    ae1.grid(row=0, column=0)
    ae2.grid(row=0, column=1)
    ae3.grid(row=0, column=2)
    ae4.grid(row=0, column=3)
    

    be1 = Label(top_vegetable,text=fruitslist[1][1],background='white',font=("bold",10))
    be2 = Label(top_vegetable,text="Rs."+str(fruitslist[1][2]),background='white',font=("bold",10))
    be3 = Entry(top_vegetable)
    be4 = Button(top_vegetable,image = photo_cart,command=lambda: addtocart(be3,fruitslist[1][0],fruitslist[1][2],be3.get()))
   
    be1.grid(row=1, column=0)
    be2.grid(row=1, column=1)
    be3.grid(row=1, column=2)
    be4.grid(row=1, column=3)

    ce1 = Label(top_vegetable,text=fruitslist[2][1],background='white',font=("bold",10))
    ce2 = Label(top_vegetable,text="Rs."+str(fruitslist[2][2]),background='white',font=("bold",10))
    ce3 = Entry(top_vegetable)
    ce4 = Button(top_vegetable,image = photo_cart,command=lambda: addtocart(ce3,fruitslist[2][0],fruitslist[2][2],ce3.get()))
   
    ce1.grid(row=2, column=0)
    ce2.grid(row=2, column=1)
    ce3.grid(row=2, column=2)
    ce4.grid(row=2, column=3)

    de1 = Label(top_vegetable,text=fruitslist[3][1],background='white',font=("bold",10))
    de2 = Label(top_vegetable,text="Rs."+str(fruitslist[3][2]),background='white',font=("bold",10))
    de3 = Entry(top_vegetable)
    de4 = Button(top_vegetable,image = photo_cart,command=lambda: addtocart(de3,fruitslist[3][0],fruitslist[3][2],de3.get()))
   
    de1.grid(row=3, column=0)
    de2.grid(row=3, column=1)
    de3.grid(row=3, column=2)
    de4.grid(row=3, column=3)

    ee1 = Label(top_vegetable,text=fruitslist[4][1],background='white',font=("bold",10))
    ee2 = Label(top_vegetable,text="Rs."+str(fruitslist[4][2]),background='white',font=("bold",10))
    ee3 = Entry(top_vegetable)
    ee4 = Button(top_vegetable,image = photo_cart,command=lambda: addtocart(ee3,fruitslist[4][0],fruitslist[4][2],ee3.get()))
   
    ee1.grid(row=4, column=0)
    ee2.grid(row=4, column=1)
    ee3.grid(row=4, column=2)
    ee4.grid(row=4, column=3)

    fe1 = Label(top_vegetable,text=fruitslist[5][1],background='white',font=("bold",10))
    fe2 = Label(top_vegetable,text=f"Rs."+str(fruitslist[5][2]),background='white',font=("bold",10))
    fe3 = Entry(top_vegetable)
    fe4 = Button(top_vegetable,image = photo_cart,command=lambda: addtocart(fe3,fruitslist[5][0],fruitslist[5][2],fe3.get()))
   
    fe1.grid(row=5, column=0)
    fe2.grid(row=5, column=1)
    fe3.grid(row=5, column=2)
    fe4.grid(row=5, column=3)
    
    






main_window()
