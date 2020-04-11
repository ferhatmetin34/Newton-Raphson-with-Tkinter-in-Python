# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:12:39 2020

@author: ASUS
"""

    
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from scipy import poly1d
import matplotlib.pyplot as plt
import numpy as np




root=tk.Tk()
root.title("YÖNEYLEM ARAŞTIRMASI ÖDEVİ - FERHAT METİN B150102047")
root.configure(background="lightsteelblue") #lightsteelblue
root.geometry('950x550')





label_1=tk.Label(root,text="Kaçıncı Dereceden Denklem?",fg="blue",font="times").grid(row=0)
Entry_1=tk.Entry(root,textvariable=IntVar())
Entry_1.grid(row=0, column=1,sticky=W)

label_2=tk.Label(root,text="XO Değerini Giriniz :",fg="blue",font="times").grid(row=1)
Entry_2=tk.Entry(root,textvariable=IntVar())
Entry_2.grid(row=1,column=1,stick=W)
            
label_3=tk.Label(root,text="İterasyon Sayısı:",fg="blue",font="times").grid(row=2)
Entry_3=tk.Entry(root,textvariable=IntVar())
Entry_3.grid(row=2,column=1,stick=W)
         
ourMessage ="Denklemin Kaçıncı Dereceden Olduğunu Rakam Kullanarak Yazınız,Ondalık İfadeler İçin '.' Kullanınız,Daha Sonra 'KATSAYI GİR' Butonuna Tıklayınız!Yeni Bir Denklem İçin de Aynı Butonu Kullanınız ­­"
messageVar = Message(root, text = ourMessage) 
messageVar.config(bg='lightgreen') 
messageVar.grid(row=0,column=20) 

katsayilar=[]  
X=[]    
entries=[] 
labels=[] 
labell=[]


x_k=[]
ilk_turev_sonuc=[]
ikinci_turev_sonuc=[]
ilk_bolu_ikinci_sonuc=[]



def exit_window():
   if tk.messagebox.askyesno("UYARI!","Çıkmak İstediğinize Emin Misiniz?"):         
        root.destroy()   
        exit()
        
def entry_uret(): 
    messageVar.destroy()
    
      
    boyut=Entry_1.get()
    boyut=int(boyut) 
    
    for i in entries:
        i.destroy()
    for k in labels:
        k.destroy()
    for p in labell:
        p.destroy()
        
    for i in labelframe_labels:
        i.destroy()
    for i in xk_labelframe_labels:
        i.destroy()
    for i in birinci_turev_labels:
        i.destroy()
    for i in ikinci_turev_labels:
        i.destroy()
    for i in ilk_bolu_ikinci_labels:
        i.destroy()
    for i in ite_list_labels:
        i.destroy()
    X.clear()
    katsayilar.clear()
    entries.clear()
    x_k.clear()
    ilk_turev_sonuc.clear()
    ikinci_turev_sonuc.clear()
    ilk_bolu_ikinci_sonuc.clear()
    

    
    
    for i in range(boyut+1):
           
            
            curr_label=Label(root,text=str(i+1)+".Katsayı :")
            curr_label.grid(row=i,column=3)
            
            curr_entry=Entry(root,textvariable=IntVar())
            curr_entry.grid(row=i,column=4)
            
            entries.append(curr_entry)
            labels.append(curr_label)
            
            label=Label(root,text="x^"+str(boyut-i))
            label.grid(row=i,column=5)
            labell.append(label)
   
    mesaj ="Denklemin Katsayılarını,X0 Değerini ve İterasyon Sayısını Rakam Kullanarak Belirtiniz! Ondalık İfadeler İçin '.' Kullanınız!­­"
    mesajvar = Message(root, text = mesaj) 
    mesajvar.config(bg='lightgreen') 
    mesajvar.grid(row=0,column=20)                  
    

labelframe=tk.LabelFrame(root,text="X(k+1)",width=100,height=300,fg="red")
labelframe.grid(row=10,column=6)
labelframe_labels=[]

xk_labelframe=tk.LabelFrame(root,text="Xk",width=100,height=300,fg="red")
xk_labelframe.grid(row=10,column=2)
xk_labelframe_labels=[]

birinci_turev_labelframe=tk.LabelFrame(root,text="f '(Xk)",width=100,height=300,fg= "red")
birinci_turev_labelframe.grid(row=10,column=3)
birinci_turev_labels=[]

ikinci_turev_labelframe=tk.LabelFrame(root,text="f ''(Xk)",width=100,height=300,fg="red")
ikinci_turev_labelframe.grid(row=10,column=4)
ikinci_turev_labels=[]

ilk_bolu_ikinci_labelframe=tk.LabelFrame(root,text=" f'(Xk) / f''(Xk)",width=100,height=300,fg="red")
ilk_bolu_ikinci_labelframe.grid(row=10,column=5)
ilk_bolu_ikinci_labels=[]

ite_list_labelframe=tk.LabelFrame(root,text="k",width=100,height=300,fg="red")
ite_list_labelframe.grid(row=10,column=1)
ite_list_labels=[]
def newton_rhapsody():
    katsayilar.clear()
    X.clear()
    x_k.clear()
    ilk_turev_sonuc.clear()
    ikinci_turev_sonuc.clear()
    ilk_bolu_ikinci_sonuc.clear()
    
    
    for i in labelframe_labels:
        i.destroy()
    for i in xk_labelframe_labels:
        i.destroy()
    for i in birinci_turev_labels:
        i.destroy()
    for i in ikinci_turev_labels:
        i.destroy()
    for i in ilk_bolu_ikinci_labels:
        i.destroy()
    for i in ite_list_labels:
        i.destroy()
   
    
    if Entry_1.get()=="0" or Entry_1.get()=="" or Entry_3.get()=="0" or Entry_3.get()=="":
        messagebox.showwarning("UYARI!","Lütfen Boş Alanları Doldurduğunuzdan ve Nümerik Değer Girdiğinizden Emin Olunuz!")
    elif Entry_1.get().isalpha()==True or Entry_2.get().isalpha()==True or Entry_3.get().isalpha():
        messagebox.showwarning("UYARI!","Lütfen Nümerik Değerler Giriniz!")

    for entry in entries:
        if entry.get()=="":
            messagebox.showwarning("UYARI!","Katsayı Girişi Boş Bırakılamaz!0 Olan Değerler için 0 Giriniz!")
            break;
        elif entry.get().isalpha()==True:
            messagebox.showwarning("UYARI!","Lütfen NÜMERİK Değerler Giriniz!")
            break;
        
                         
    for entry in entries:
        katsayilar.append(float(entry.get()))
        
    polinom=poly1d(katsayilar)
    
    
    birinci_turev=polinom.deriv()
    ikinci_turev=birinci_turev.deriv()
    
    X0=Entry_2.get()
    X0=float(X0)
    iterasyon_sayisi=Entry_3.get()
    iterasyon_sayisi=int(iterasyon_sayisi)
    ite_list=list(np.arange(0,iterasyon_sayisi+1))
    
    
    x_k.append(X0)   
    
    
    for i in range(0,iterasyon_sayisi):   
        X.append(X0-(birinci_turev(X0)/ikinci_turev(X0)))
        
        
        ilk_turev_sonuc.append(birinci_turev(X0))
        ikinci_turev_sonuc.append(ikinci_turev(X0))
        ilk_bolu_ikinci_sonuc.append(birinci_turev(X0)/ikinci_turev(X0))       
        X0=X[i] 
        x_k.append(X0)
        
    ilk_turev_sonuc.append(birinci_turev(X0))
    ikinci_turev_sonuc.append(ikinci_turev(X0))
    ilk_bolu_ikinci_sonuc.append(birinci_turev(X0)/ikinci_turev(X0))
    X.append(X0-(birinci_turev(X0)/ikinci_turev(X0)))
        
    
    for i in range(len(X)):
       
       frame_label=tk.Label(labelframe,text=str(X[i]))
       frame_label.grid(row=i,column=5)
       labelframe_labels.append(frame_label)
       
    for i in range(len(x_k)):
       xklabel=tk.Label(xk_labelframe,text=str(x_k[i]))
       xklabel.grid(row=i,column=1)
       xk_labelframe_labels.append(xklabel)
       
    for i in range(len(ilk_turev_sonuc)):
        turev_label=tk.Label(birinci_turev_labelframe,text=str(ilk_turev_sonuc[i]))
        turev_label.grid(row=i,column=2)
        birinci_turev_labels.append(turev_label)
       
    for i in range(len(ikinci_turev_sonuc)):
        ikinci_label=tk.Label(ikinci_turev_labelframe,text=str(ikinci_turev_sonuc[i]))
        ikinci_label.grid(row=i,column=3)
        ikinci_turev_labels.append(ikinci_label)
        
    for i in range(len(ilk_bolu_ikinci_sonuc)):
        iki_bir_label=tk.Label(ilk_bolu_ikinci_labelframe,text=str(ilk_bolu_ikinci_sonuc[i]))
        iki_bir_label.grid(row=i,column=4)
        ilk_bolu_ikinci_labels.append(iki_bir_label)
        
    for i in range(len(ite_list)):
        ite_label=tk.Label(ite_list_labelframe,text=str(ite_list[i]))
        ite_label.grid(row=i,column=0)
        ite_list_labels.append(ite_label)
        
    def graph():
        plt.scatter(ite_list,X,edgecolors="red",marker="x")
        plt.xlabel("İterasyon ")
        plt.ylabel("Fonksiyon Değeri")
        plt.xticks(range(1,iterasyon_sayisi+1))
        plt.legend()
        plt.show()
        
        
    
        
    graph=tk.Button(root,text="GRAFİK OLUŞTUR",command=graph,fg="blue")
    graph.grid(row=10,column=0)
    
    
    
Exit=tk.Button(root,text="ÇIKIŞ",width=5,bg="red",fg="white",font="helvetica",command=exit_window).grid(row=6,column=0)
Enter=tk.Button(root,text="KATSAYI GİR",width=16,bg="white",fg="blue",command=entry_uret)
Enter.grid(row=6,column=1)
coz=tk.Button(root,text="NEWTON RHAPSODY",width=16,bg="white",fg="blue",command=newton_rhapsody)
coz.grid(row=8,column=1)


root.mainloop()
















