from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class pharmacy:
    def __init__(self,root):
        self.root=root
        self.root.title('Pharmacy Management System')
        self.root.geometry('1510x800+0+0')
        
        #side variable
        
        self.refno=StringVar()
        self.medname=StringVar()
        
        #main variables
        self.refno_var=StringVar()
        self.companyname_var=StringVar()
        self.typesofmedicine_var=StringVar()
        self.medicinename_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffect_var=StringVar()
        self.warnning_var=StringVar()
        self.dosage_var=StringVar()
        self.tibletprice_var=StringVar()
        self.prodictqt_var=StringVar()
        
        
        #lable title
        label_title=Label(self.root,text="Pharmacy Management System",bd=15,relief=RIDGE,fg='darkgreen',bg='white',font=('times new roman',43,'bold'),padx=2,pady=2)
        label_title.pack(side=TOP,fill=X)
        
        img=Image.open('ps.jpg')
        img=img.resize((70,57),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)
        btn_1=Button(self.root,image=self.photo,borderwidth=0.15)
        btn_1.place(x=200,y=17)
        
        #main frame
        main_frame=Frame(self.root,bd=10,relief=RIDGE)
        main_frame.place(x=0,y=84,width=1510,height=390)
        
        #left frame--------------------------------------
        
        left_frame=LabelFrame(main_frame,bd=15,relief=RIDGE,font=('arial',12,'bold'),text="Medicine Information",fg='green',padx=10)
        left_frame.place(x=0,y=0,width=830,height=365)
        
        lbl_refrenceno=Label(left_frame,font=('arial',12,'bold'),text="Refrence No",padx=2)
        lbl_refrenceno.grid(row=0,column=0,sticky=W)
        
        conn=mysql.connector.connect(host='localhost',username="root",password='R1234',database='student')
        my_cursor=conn.cursor()
        my_cursor.execute("select refno from pharm")
        data1=my_cursor.fetchall()
        
        ref_com=ttk.Combobox(left_frame,width=22,textvariable=self.refno_var,font=('arial',12,'bold'),state='readonly')
        ref_com['values']=data1
        ref_com.grid(row=0,column=1)
        ref_com.current(0)
        
        lbl_comname=Label(left_frame,font=('arial',12,'bold'),text="Company Name",padx=2,pady=6)
        lbl_comname.grid(row=1,column=0,sticky=W)
        txt_comname=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.companyname_var,font=('arial',12,'bold'))
        txt_comname.grid(row=1,column=1)
        
        lbl_typeofmedicine=Label(left_frame,font=('arial',12,'bold'),text="Types Of Medicine",padx=2,pady=4)
        lbl_typeofmedicine.grid(row=2,column=0,sticky=W)
        
        typeofmedicine_com=ttk.Combobox(left_frame,width=22,textvariable=self.typesofmedicine_var,font=('arial',12,'bold'),state='readonly')
        typeofmedicine_com['values']=('Tablet','Liquid','Capsules','Topical Medicines','Drops','Inhales','Injection')
        typeofmedicine_com.grid(row=2,column=1)
        typeofmedicine_com.current(0)
        
        lbl_medicinename=Label(left_frame,font=('arial',12,'bold'),text="Medicine Name",padx=2,pady=6)
        lbl_medicinename.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host='localhost',username="root",password='R1234',database='student')
        my_cursor=conn.cursor()
        my_cursor.execute("select medname from pharm")
        data2=my_cursor.fetchall()
        
        medicinename_com=ttk.Combobox(left_frame,width=22,textvariable=self.medicinename_var,font=('arial',12,'bold'),state='readonly')
        medicinename_com['values']=data2
        medicinename_com.grid(row=3,column=1)
        medicinename_com.current(0)
        
        lbl_lotno=Label(left_frame,font=('arial',12,'bold'),text="Lot No",padx=2,pady=6)
        lbl_lotno.grid(row=4,column=0,sticky=W)
        txt_lotno=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.lot_var,font=('arial',12,'bold'))
        txt_lotno.grid(row=4,column=1)
        
        lbl_issuedate=Label(left_frame,font=('arial',12,'bold'),text="Issue Date",padx=2,pady=6)
        lbl_issuedate.grid(row=5,column=0,sticky=W)
        txt_issuedate=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.issuedate_var,font=('arial',12,'bold'))
        txt_issuedate.grid(row=5,column=1)
        
        lbl_Expdate=Label(left_frame,font=('arial',12,'bold'),text="Exp Date",padx=2,pady=6)
        lbl_Expdate.grid(row=6,column=0,sticky=W)
        txt_Expdate=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.expdate_var,font=('arial',12,'bold'))
        txt_Expdate.grid(row=6,column=1)
        
        lbl_uses=Label(left_frame,font=('arial',12,'bold'),text="Uses",padx=2,pady=6)
        lbl_uses.grid(row=7,column=0,sticky=W)
        txt_uses=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.uses_var,font=('arial',12,'bold'))
        txt_uses.grid(row=7,column=1)
        
        lbl_sideffect=Label(left_frame,font=('arial',12,'bold'),text="Side Effect",padx=2,pady=6)
        lbl_sideffect.grid(row=8,column=0,sticky=W)
        txt_sideffect=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.sideeffect_var,font=('arial',12,'bold'))
        txt_sideffect.grid(row=8,column=1)
        
        lbl_warnning=Label(left_frame,font=('arial',12,'bold'),text="Warnning",padx=10,pady=6)
        lbl_warnning.grid(row=0,column=2,sticky=W)
        txt_warnning=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.warnning_var,font=('arial',12,'bold'))
        txt_warnning.grid(row=0,column=3)
        
        lbl_dosage=Label(left_frame,font=('arial',12,'bold'),text="Dosage",padx=10,pady=6)
        lbl_dosage.grid(row=1,column=2,sticky=W)
        txt_dosage=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.dosage_var,font=('arial',12,'bold'))
        txt_dosage.grid(row=1,column=3)
        
                
        lbl_tabletprice=Label(left_frame,font=('arial',12,'bold'),text="Tiblet Price",padx=10,pady=6)
        lbl_tabletprice.grid(row=2,column=2,sticky=W)
        txt_tabletprice=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.tibletprice_var,font=('arial',12,'bold'))
        txt_tabletprice.grid(row=2,column=3)
        
        lbl_productqt=Label(left_frame,font=('arial',12,'bold'),text="Product QT",padx=10,pady=6)
        lbl_productqt.grid(row=3,column=2,sticky=W)
        txt_productqt=Entry(left_frame,relief=RIDGE,width=24,textvariable=self.prodictqt_var,font=('arial',12,'bold'))
        txt_productqt.grid(row=3,column=3)
        
        lbl_message=Label(left_frame,font=('arial',10,'bold'),text="Take Care",padx=2,pady=6,fg='blue')
        lbl_message.place(x=480,y=135)
        
        img1=Image.open("images.jpg")
        img1=img1.resize((300,150),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        btn_2=Button(left_frame,image=self.photo1,borderwidth=0,cursor="hand2")
        btn_2.place(x=400,y=170)
        
        
        
              
        #right frame--------------------------------------
        right_frame=LabelFrame(main_frame,bd=15,relief=RIDGE,font=('arial',12,'bold'),text='New Medicine Add Deparment',fg='green',padx=10)
        right_frame.place(x=842,y=0,width=500,height=365)
        
        img2=Image.open("1.jpg")
        img2=img2.resize((448,140),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        btn_3=Button(right_frame,image=self.photo2,borderwidth=0,cursor="hand2")
        btn_3.place(x=0,y=0)
        
        lbl_refno=Label(right_frame,font=('arial',12,'bold'),text="Refrence No",padx=2)
        lbl_refno.place(x=0,y=144)
        txt_refno=Entry(right_frame,relief=RIDGE,width=22,textvariable=self.refno,font=('arial',12,'bold'))
        txt_refno.place(x=132,y=144)
        
        lbl_medname=Label(right_frame,font=('arial',12,'bold'),text="Medicine Name",padx=2)
        lbl_medname.place(x=0,y=170)
        txt_medname=Entry(right_frame,relief=RIDGE,width=22,textvariable=self.medname,font=('arial',12,'bold'))
        txt_medname.place(x=132,y=170)
        
        #__________________________side frame____________________
        side_frame=Frame(right_frame,bd=4,relief=RIDGE,bg='white')
        side_frame.place(x=0,y=200,width=290,height=127)
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL) 
        sc_y.pack(side=RIGHT,fill=Y)   
        
        self.Medicine_table=ttk.Treeview(side_frame,columns=('RefNo','MedName'),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.Medicine_table.xview)
        sc_y.config(command=self.Medicine_table.yview)   
        
        self.Medicine_table.heading("RefNo",text="Refrence NO")
        self.Medicine_table.heading('MedName',text='Medicine Name')
        self.Medicine_table['show']='headings'
        
        self.Medicine_table.column('RefNo',width=100)
        self.Medicine_table.column('MedName',width=100)
        
        self.Medicine_table.pack(fill=BOTH,expand=1)
        self.fetch()
        self.Medicine_table.bind("<ButtonRelease>",self.cursor)
        
        #_______________________________side buthon frame-------------------------
        
        sidebuthonframe=Frame(right_frame,bd=4,relief=RIDGE,bg='white')
        sidebuthonframe.place(x=300,y=200,width=100,height=127)
         
        btnadd=Button(sidebuthonframe,text='Add',command=self.add,font=('aril',10,'bold'),width=11,padx=2,pady=2,bg='green',fg='white')
        btnadd.grid(row=0,column=0)
        
        btnup=Button(sidebuthonframe,text='Update',command=self.update,font=('aril',10,'bold'),width=11,padx=2,pady=2,bg='green',fg='white')
        btnup.grid(row=1,column=0)
        
        btndel=Button(sidebuthonframe,text='Delete',command=self.delete,font=('aril',10,'bold'),width=11,padx=2,pady=2,bg='green',fg='white')
        btndel.grid(row=2,column=0)
        
        btncl=Button(sidebuthonframe,text='Clear',command=self.clear,font=('aril',10,'bold'),width=11,padx=2,pady=3,bg='green',fg='white')
        btncl.grid(row=3,column=0)

        
        
        #button frame-----------------------------------
        btn_frame=Frame(self.root,bd=15,relief=RIDGE)
        btn_frame.place(x=0,y=475,width=1510,height=62)
        
        btnaddmedicine=Button(btn_frame,text='Medicine Add',command=self.add_get,font=('aril',12,'bold'),width=12,padx=2,pady=3,bg='darkgreen',fg='white')
        btnaddmedicine.grid(row=0,column=0)
        
        btnupdatemed=Button(btn_frame,text='Update',command=self.update_get,font=('aril',12,'bold'),width=12,padx=2,pady=3,bg='darkgreen',fg='white')
        btnupdatemed.grid(row=0,column=1)
        
        btndeletemed=Button(btn_frame,text='Delete',command=self.delete_get,font=('aril',12,'bold'),width=12,padx=2,pady=3,bg='darkgreen',fg='white')
        btndeletemed.grid(row=0,column=2)
        
        btnresetmed=Button(btn_frame,text='Reset',command=self.reset_get,font=('aril',12,'bold'),width=12,padx=2,pady=3,bg='darkgreen',fg='white')
        btnresetmed.grid(row=0,column=3)
        
        btnexit=Button(btn_frame,text='Exit',command=self.exit_get,font=('aril',12,'bold'),width=12,padx=2,pady=3,bg='darkgreen',fg='white')
        btnexit.grid(row=0,column=4)
        
        #label search by
        lbl_searchby=Label(btn_frame,font=('arial',17,'bold'),text="Search By",width=8,padx=1,bg='red',fg='white')
        lbl_searchby.grid(row=0,column=5)
        
        #varaibles of search and showall
        self.serch_var=StringVar()
        self.serchtxt_var=StringVar()
        
        search_com=ttk.Combobox(btn_frame,width=16,textvariable=self.serch_var,font=('arial',16,'bold'),state='readonly')
        search_com['values']=('Refrence','Medicine','Lot')
        search_com.grid(row=0,column=6)
        search_com.current(0)
        
        txtsearchby=Entry(btn_frame,bd=3,relief=RIDGE,width=12,textvariable=self.serchtxt_var,font=('arial',16,'bold'))
        txtsearchby.grid(row=0,column=7)
        
        btnsearch=Button(btn_frame,text='Search',command=self.search_data,font=('aril',12,'bold'),width=8,padx=1,pady=3,bg='darkgreen',fg='white')
        btnsearch.grid(row=0,column=8)
        
        btnshowall=Button(btn_frame,text='Show All',command=self.fetch_get,font=('aril',12,'bold'),width=10,padx=2,pady=3,bg='darkgreen',fg='white')
        btnshowall.grid(row=0,column=9)
    
        
        #details frame-------------------------------------------------
        details_frame=Frame(self.root,bd=15,relief=RIDGE,bg='light green')
        details_frame.place(x=0,y=532,width=1510,height=170)
        
        #tabel frame==============
        
        table_frame=Frame(details_frame,bd=10,relief=RIDGE)
        table_frame.place(x=20,y=0,width=1300,height=145)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL) 
        
        
        self.pharmacy_table=ttk.Treeview(table_frame,columns=("reg",'companyname','ttype','tabletname','lotno','issuedate',
                                                                   "expdate",'uses','sideeffect','warning','dosage','price','productqt'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table.heading("reg",text="Refrence Number")
        self.pharmacy_table.heading('companyname',text='Company Name')
        self.pharmacy_table.heading('ttype',text='Tablet Type')
        self.pharmacy_table.heading('tabletname',text='Tablet Name')
        self.pharmacy_table.heading('lotno',text='Lot No')
        self.pharmacy_table.heading('issuedate',text='Issue Date')
        self.pharmacy_table.heading('expdate',text='Exp Date')
        self.pharmacy_table.heading('uses',text='Uses')
        self.pharmacy_table.heading('sideeffect',text='Side Effect')
        self.pharmacy_table.heading('warning',text='Warning')
        self.pharmacy_table.heading('dosage',text='Dosage')
        self.pharmacy_table.heading('price',text='Price')
        self.pharmacy_table.heading('productqt',text='Product QT')
        
        self.pharmacy_table['show']='headings'
        
        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column('companyname',width=100)
        self.pharmacy_table.column('ttype',width=100)
        self.pharmacy_table.column('tabletname',width=100)
        self.pharmacy_table.column('lotno',width=100)
        self.pharmacy_table.column('issuedate',width=100)
        self.pharmacy_table.column('expdate',width=100)
        self.pharmacy_table.column('uses',width=100)
        self.pharmacy_table.column('sideeffect',width=100)
        self.pharmacy_table.column('warning',width=100)
        self.pharmacy_table.column('dosage',width=100)
        self.pharmacy_table.column('price',width=100)
        self.pharmacy_table.column('productqt',width=100) 
        
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        self.pharmacy_table.bind("<ButtonRelease>",self.cursor_get)
        self.fetch_get()
        
        
    #crete pharam database and use in side frame_____________________
    def add(self):
        if self.refno.get()=="" or self.medname.get()=='':
            messagebox.showerror('Error',"All Fields are required ")
        else:
          conn=mysql.connector.connect(host='localhost',username="root",password='R1234',database='student')
          my_cursor=conn.cursor()
          my_cursor.execute('insert into pharm values(%s,%s)',(
            
                                                        self.refno.get(),
                                                        self.medname.get()
              
                                                           ))
          conn.commit()
          self.fetch()
          conn.close()
          messagebox.showinfo("Success","Medicine Added")
        
    #fetch data
    def fetch(self):
        conn=mysql.connector.connect(host='localhost',username="root",password='R1234',database='student')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharm")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.Medicine_table.delete(*self.Medicine_table.get_children())
            for i in row:
                self.Medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #cursor
    def cursor(self,dontmiss=''):
        cursor_data=self.Medicine_table.focus()
        data_continue=self.Medicine_table.item(cursor_data)
        data3=data_continue['values']
        
        self.refno.set(data3[0])
        self.medname.set(data3[1])
        
    #delete
    def delete(self):
        if self.refno.get()=="" or self.medname.get()=='':
            messagebox.showerror('Error',"All Fields are required ")
        else:
          conn=mysql.connector.connect(host='localhost',username="root",password='R1234',database='student')
          my_cursor=conn.cursor()
          my_cursor.execute('delete from pharm where refno=%s',(self.refno.get(),))
          conn.commit()
          conn.close()
          messagebox.showinfo('Delete','Delete Data Succesfully')
        
    #update
    def update(self):
        if self.refno.get()=="" or self.medname.get()=='':
            messagebox.showerror('Error',"All Fields are required ")
        else:
            conn=mysql.connector.connect(host='localhost',username="root",password='R1234',database='student')
            my_cursor=conn.cursor()
            my_cursor.execute('update pharm set medname=%s where refno=%s',(
            
                                                
                                                self.medname.get(),
                                                self.refno.get()
            
                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Data Updated')
            
    #clear
    def clear(self):
        self.refno.set('')
        self.medname.set('')
        
        
        
        
    #-----------------------------side close----------------------------
    
    
    #_________________________-----main frame-----------________________________
    
    
    #add
    def add_get(self):
        if self.refno_var.get()=='' or self.companyname_var.get()=='':
            messagebox.showerror('Error','All Fildes Are Required')
        else:   
            conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='student')
            my_cursor=conn.cursor()
            my_cursor.execute('insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
            
                                                        
                                                                self.refno_var.get(),
                                                                self.companyname_var.get(),
                                                                self.typesofmedicine_var.get(),
                                                                self.medicinename_var.get(),
                                                                self.lot_var.get(),
                                                                self.issuedate_var.get(),
                                                                self.expdate_var.get(),
                                                                self.uses_var.get(),
                                                                self.sideeffect_var.get(),
                                                                self.warnning_var.get(),
                                                                self.dosage_var.get(),
                                                                self.tibletprice_var.get(),
                                                                self.prodictqt_var.get()
                                                                    
            
                                              ))
            conn.commit()
            self.fetch_get()
            conn.close()
            messagebox.showinfo('Success',"Data Inserted")
            
            
    #fetch data
    def fetch_get(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='student')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from pharmacy')
        wor=my_cursor.fetchall()
        if len(wor)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in wor:
                self.pharmacy_table.insert('',END,values=i)
            conn.commit()
        conn.close()
        
    #get cursoer
    def cursor_get(self,event=''):
        phtable=self.pharmacy_table.focus()
        ph_continue=self.pharmacy_table.item(phtable)
        ph=ph_continue['values']
        
        self.refno_var.set(ph[0])
        self.companyname_var.set(ph[1])
        self.typesofmedicine_var.set(ph[2])
        self.medicinename_var.set(ph[3])
        self.lot_var.set(ph[4])
        self.issuedate_var.set(ph[5])
        self.expdate_var.set(ph[6])
        self.uses_var.set(ph[7])
        self.sideeffect_var.set(ph[8])
        self.warnning_var.set(ph[9])
        self.dosage_var.set(ph[10])
        self.tibletprice_var.set(ph[11])
        self.prodictqt_var.set(ph[12])
        
    #reset
    def reset_get(self):
        self.refno_var.set('')
        self.companyname_var.set('')
        self.typesofmedicine_var.set('')
        self.medicinename_var.set('')
        self.lot_var.set('')
        self.issuedate_var.set('')
        self.expdate_var.set('')
        self.uses_var.set('')
        self.sideeffect_var.set('')
        self.warnning_var.set('')
        self.dosage_var.set('')
        self.tibletprice_var.set('')
        self.prodictqt_var.set('')
    
    
    #update data
    def update_get(self):
        if self.refno_var.get()=='' or self.companyname_var.get()=='':
            messagebox.showerror('Error','All Fildes Are Required')
        else:   
            conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='student')
            my_cursor=conn.cursor()
            my_cursor.execute('update pharmacy set comname=%s,typeofname=%s,Medicine=%s,Lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warnning=%s,dosage=%s,tibletprice=%s,productqt=%s where Refrence=%s',(
                
                                                                                                                                                                
                                                                                                    self.companyname_var.get(),
                                                                                                    self.typesofmedicine_var.get(),
                                                                                                    self.medicinename_var.get(),
                                                                                                    self.lot_var.get(),
                                                                                                    self.issuedate_var.get(),
                                                                                                    self.expdate_var.get(),
                                                                                                    self.uses_var.get(),
                                                                                                    self.sideeffect_var.get(),
                                                                                                    self.warnning_var.get(),
                                                                                                    self.dosage_var.get(),
                                                                                                    self.tibletprice_var.get(),
                                                                                                    self.prodictqt_var.get(),
                                                                                                    self.refno_var.get()
                                                                                                                                                                                               
                                                                                                                                                                                               
                                                                                                                                                                                               ))
            conn.commit()
            self.fetch_get()
            conn.close()
            messagebox.showinfo('Success','Data Updated')
            
    #delete data
    def delete_get(self):
        if self.refno_var.get()=='' or self.companyname_var.get()=='':
            messagebox.showerror('Error','All Fildes Are Required')
        else:   
            conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='student')
            my_cursor=conn.cursor()
            my_cursor.execute("delete from pharmacy where Refrence=%s",(self.refno_var.get(),))
            conn.commit()
            self.fetch_get()
            conn.close()
            messagebox.showinfo("Delete","Data Deleted")
            
            
    #exit data
    def exit_get(self):
        op=messagebox.askyesno('Pharmacy Management System','Are You Sure To Exit Windows')
        if op>0:
            root.destroy()
            return
        
    
    #search data
    def search_data(self):
        
           
            conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='student')
            my_cursor=conn.cursor()
            my_cursor.execute('select * from pharmacy where ' +str(self.serch_var.get())+" LIKE '%"+str(self.serchtxt_var.get())+"%'")
            wor1=my_cursor.fetchall()
            if len(wor1)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in wor1:
                    self.pharmacy_table.insert('',END,values=i)
                conn.commit()
            conn.close()
                
        
    
            
        
        
        
        
           
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
if __name__=='__main__':
    root=Tk()
    obj=pharmacy(root)
    root.mainloop()
