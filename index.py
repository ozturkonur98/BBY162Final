from tkinter import * # * tüm paremetleri kullanıcağımızı belirtmek için koyduk.
import tkinter.messagebox
import tkinter as tk
from PIL import Image, ImageTk
###from final2.py import *

girisbilgi = ["1", "1"]
def dosyaac():
    c = open("eserler.txt", "a", encoding='utf8')
    c.close()
    c2 = open("üyeler.txt", "a", encoding='utf8')
    c2.close()
    tkinter.messagebox.showinfo("BİLGİLENDİRME !", " GEREKLİ DOSYALAR AÇILDI !")
def dosyasil1():
    c = open("eserler.txt", "w+", encoding='utf8')
    c.close()
    tkinter.messagebox.showinfo("BİLGİLENDİRME !", " ESER LİSTESİ TEMİZLENDİ !")
def dosyasil2():
    c2 = open("üyeler.txt", "w+", encoding='utf8') # dosya temizler
    c2.close()
    tkinter.messagebox.showinfo("BİLGİLENDİRME !", " ÜYE LİSTESİ TEMİZLENDİ !")
def girbilgiler():
    h = Tk()
    h.resizable(FALSE, FALSE)
    h.title("Giriş Bilgileri")
    h.geometry("200x30")
  # YAZI LABELI  Label(sh, text=(p,"Kullanıcı Adı : ", (girisbilgi[0]), "Şifre : ", girisbilgi[1]), fg="darkgreen", justify=CENTER).pack()
    tkinter.messagebox.showinfo ("HATIRLATICI", ("Kullanıcı Adı : ", girisbilgi[0],"Şifre : ", girisbilgi[1]))
def gir():
    kadi = kadial.get()
    sifre = sifreal.get()
    print("Giriş bilgileriniz kontrol ediliyor...")

    if kadi == girisbilgi[0] and sifre == girisbilgi[1]:
        print("Hoşgeldiniz !")
        tkinter.messagebox.showinfo("BHKS 1.0","Başarıyla Giriş Yapıldı.")
        ekranısil()


    elif kadi != girisbilgi[0] and sifre == girisbilgi[1]:
        print("Kullanıcı adını hatalı girdiniz.")
        tkinter.messagebox.showinfo("BHKS 1.0", "Başarıyla Giriş Yapıldı.")


    elif kadi == girisbilgi[0] and sifre != girisbilgi[ 1]:
        print("Şifreyi hatalı girdiniz.")
        tkinter.messagebox.showerror("BHKS 1.0", "Bilgileriniz yanlış. Tekrar deneyiniz!")


    else:
        print("Bilgileri yanlış girdiniz. Lütfen tekrar giriş yapınız.")
        tkinter.messagebox.showerror("BHKS 1.0", "Bilgileriniz yanlış. Tekrar deneyiniz!")
def ekranısil():
    kadisor.destroy()
    kadial.destroy()
    sifresor.destroy()
    sifreal.destroy()
    girb.destroy()
    mesaj = Button(p)
    mesaj.config(text="SİSTEME HOŞGELDİNİZ.\n Sistem menüsüne geçmek için tıklayınız...", width=45, height=40, bg= "black", fg= "yellow",font=("Comic Sans MS",15,"bold"),command=menu)
    girbilgi.destroy()
    mesaj.pack(fill=X)
    dosyaac()
   # yapımcı = Label(p)
   # yapımcı.config(text="Tasarlayan : ONUR ÖZTÜRK", bg="black", fg="white", font=("Times New Roman", 10))
    #yapımcı.pack

    ####
 # üst 3 oky
p = Tk()
p.title("KÜTÜPHANE OTOMASYONU 1.0")
p.geometry("500x250") # ayarlarını sonra yap genişlik yükseklik
p.resizable(FALSE, FALSE) # küçültüp büyütmeyi kapatıyor
p.config(bg="black") # config komutu o kutucuğu vs. ayarlıyor.

girbilgi = Button(p)
girbilgi.config(text="Sifre Hatırla",bg="black", fg="yellow", font=("Comic Sans MS", 10),justify=CENTER, command=girbilgiler)
girbilgi.pack()

kadisor = Label(p)
kadisor.config(text="Kullanici adiniz : ", bg="black", fg="red", font=("SHOWCARD GOTHIC", 30),justify=CENTER)
kadisor.pack()

kadial = Entry(p,justify=CENTER, width=30) #entry kullanıcı girişi için input verr
kadial.pack()

sifresor = Label(p)
sifresor.config(text="Sifreniz : ", bg="black", fg="red", font=("SHOWCARD GOTHIC", 25),justify=CENTER)
sifresor.pack()

sifreal = Entry(p, width="15", show="*",justify=CENTER)
sifreal.pack()

girb = Button(p)
girb.config(text="GİRİŞ", bg="black", fg="red", activebackground="blue", activeforeground="white", font=("Comic Sans MS", 12),justify=CENTER, command=gir)
girb.pack(side=LEFT)

çıkb = Button(p)
çıkb.config(text="ÇIKIŞ", bg="black", fg="red", activebackground="blue", activeforeground="white", font=("Comic Sans MS", 12),justify=CENTER, command=quit)
çıkb.pack(side=RIGHT) # pack modülü uygulamaya, ekrana eklemek için kullanılır.
#tkinter.messagebox.askyesno("KÜTÜPHANE OTOMASYONU", "Çıkış yapmak istediğinizden emin misiniz?")
# ANA MENÜ
def menu():
    p = Tk()
    p.title("Kütüphane Otomasyonu")
    p.resizable(FALSE, FALSE)
    frame = Frame(p)
    frame.pack()

    bottomframe = Frame(p)
    bottomframe.pack(fill=BOTH, side = BOTTOM )

    b1 = Button(frame, text="ESER EKLE", fg="red", font=("Comic Sans MS ",25),width=25,justify=CENTER, command=kitap_ekle)
    b1.pack()
#    b1.grid(column=0, row=3)

    b2 = Button(frame, text="ESERLERİ TEMİZLE", fg="brown", font=("Comic Sans MS ",25),width=25,justify=CENTER, command=dosyasil1)
    b2.pack()
 #   b1.grid(column=1, row=3)
    b3 = Button(frame, text="ÜYE EKLE", fg="black", font=("Comic Sans MS ",25),width=25,justify=CENTER, command=üyeekle)
    b3.pack()
  #  b1.grid(column=2, row=3)
    b4 = Button(frame, text="ÜYELERİ TEMİZLE", fg="blue", font=("Comic Sans MS ",25),width=25,justify=CENTER, command=dosyasil2)
    b4.pack()
   # b1.grid(column=3, row=3)
    b5 = Button(frame, text="ESER ARAMA ( EKLENECEK,  ) ", fg="orange", font=("Comic Sans MS ",25),width=25,justify=CENTER, command=ara)
    b5.pack()
    b6 = Button(frame, text="ESER LİSTESİ", fg="red", font=("Comic Sans MS ", 25), width=25, justify=CENTER, command=eserlist)
    b6.pack()
    #    b1.grid(column=0, row=3)

    b7 = Button(frame, text="ÜYE LİSTESİ", fg="brown", font=("Comic Sans MS ", 25), width=25, justify=CENTER,command=uyelist)
    b7.pack()
    #b1.grid(column=4, row=3)
    p.mainloop()

def ara():
  tkinter.messagebox.showerror("HATA", "BURA TAMAMLANAMADI!")
  #  with open("eserler.txt", "r", encoding="utf-8") as file:
  #          sorgu = str(input('Aranan eser girdilerini yazınız: '))
  #          if sorgu ==file:
  #              print("Bulundu.!")
  #          else:
  #              print("Eser Bulunamadı.!")
  #              file.seek(0)  # reset file to the beginning for next search
  #  file.close()
"""    o = open("eserler.txt", "r", encoding='utf8')  # encodingi yap çünkü yapmazsan tr harfler değişiyor.
    sorgu = str(input('Aranan eser girdilerini yazınız: '))
    for sorgu in o:  # readlines ibaresi her satırı tek tek okumaya yarıyor.
        print("Aradığınız eser kütüphanemizde mevcut.")
"""
########################################
def kitap_ekle():
        global kitap_adi,yazar_adi,yy,p1
        p1 = Tk()
        p1.resizable(FALSE, FALSE)
        baslik1 = p1.title("Kitap Ekleme")
        p1.configure(background="black")

        kitap_adi= Entry(p1,width=27)
        kitap_adi.grid(column=2, row=2)
        yazar_adi = Entry(p1, width=27)
        yazar_adi.grid(column=2, row=3)
        yy = Entry(p1, width=27)
        yy.grid(column=2, row=6)

        kaydet = Button(p1, text= "Kaydet",command=kitap_kaydet, fg="black", bg="red")
        kaydet.grid(column=1, row=9)
        kapat = Button(p1 ,text = "Kapat", command=p1.destroy, fg="black", bg="red")
        kapat.grid(column=3, row=9)
        Label(p1,bg="black",fg="orange", text='Lütfen "*" alanları doldurunuz.').grid(column=1, row=1)
        Label(p1,bg="black",fg="orange", text='*Kitap Adı: ').grid(column=1, row=2)
        Label(p1,bg="black",fg="orange", text='*Yazar Adı: ').grid(column=1, row=3)
        Label(p1,bg="black",fg="orange", text='*Yayın Yılı :').grid(column=1, row=6)
def kitap_kaydet():

        sistem = str((" ◯◯ Kitap Adı : " +kitap_adi.get() + "    Yazar Adı : " + yazar_adi.get()+ "   Yayın Yılı : " + yy.get()) + "\n")
        dosya = open("eserler.txt", "a", encoding="utf-8")
        for x in sistem:
            dosya.write(x)
        dosya.close()
        print("KAYDEDİLDİ..")
        tkinter.messagebox.showinfo("BİLGİ", "ESER KAYDEDİLDİ..", command= p1.destroy())
def üyeekle():
    global üyeadisoyadi, üyeno, üyeyaş, p1
    p1 = Tk()
    p1.resizable(FALSE, FALSE)
    baslik1 = p1.title("Üye Ekleme")
    p1.configure(background="black")

    üyeadisoyadi = Entry(p1, width=27)
    üyeadisoyadi.grid(column=2, row=2)
    üyeno = Entry(p1, width=27)
    üyeno.grid(column=2, row=3)
    üyeyaş = Entry(p1, width=27)
    üyeyaş.grid(column=2, row=6)

    kaydet = Button(p1, text="Kaydet", command=üyekaydet, fg="black", bg="red")
    kaydet.grid(column=1, row=9)
    kapat = Button(p1, text="Kapat", command=p1.destroy, fg="black", bg="red")
    kapat.grid(column=3, row=9)
    Label(p1, bg="black", fg="orange", text='Lütfen "*" alanları doldurunuz.').grid(column=1, row=1)
    Label(p1, bg="black", fg="orange", text='*Üye Ad Soyad: ').grid(column=1, row=2)
    Label(p1, bg="black", fg="orange", text='*Üye No: ').grid(column=1, row=3)
    Label(p1, bg="black", fg="orange", text='*Üye Yaş :').grid(column=1, row=6)
def üyekaydet():
    sistem = str((" ◯◯ Üyenin Adı Soyadı:" + üyeadisoyadi.get() + "   Üye Kayıt No:" + üyeno.get() + "   Üyenin Yaşı:" + üyeyaş.get()) + "\n")
    dosya = open("üyeler.txt", "a", encoding="utf-8")
    for x in sistem:
        dosya.write(x)
    dosya.close()
    print("KAYDEDİLDİ")
    tkinter.messagebox.showinfo("BİLGİ", "ÜYE KAYDEDİLDİ..")
def eserlist():
    p = Tk()
    ebaslık = p.title("KAYITLI ESERLER")
    p.configure(background="black")
    file = open("eserler.txt", "r", encoding='utf8')
    data = file.read()
    file.close()
    eser_liste = Label(p, text=data, fg="yellow", bg="black",justify=CENTER)
    eser_liste.pack()
    totaleser = Button(p, text="TOPLAM KAYITLI ESERLER",justify=CENTER, command=esersayi)
    totaleser.pack()
    kapat = Button(p, text="Kapat", command=p.destroy, fg="black", bg="RED")
    kapat.pack()
    p.mainloop()

    # bu 3 def oky
def uyelist():

    p = Tk()
    üyebaslık = p.title("KAYITLI ÜYELER")
    p.configure(background="black")
    file = open("üyeler.txt", "r", encoding='utf8')
    data = file.read()
    file.close()
    üye_liste = Label(p, text=data, fg="yellow", bg="black",justify=CENTER)
    üye_liste.pack()
    totalüye = Button(p, text="TOPLAM KAYITLI ÜYELERİMİZ",justify=CENTER, command=uyesayi)
    totalüye.pack()
    kapat = Button(p, text="Kapat", command=p.destroy, fg="black", bg="RED")
    kapat.pack()
    p.mainloop()
def esersayi():

    teser = open('eserler.txt', "r", encoding="utf-8")
    count = 0
    for eser in teser:
        count = count + 1
    print('Toplam eser:', count)
    tkinter.messagebox.showinfo('Toplam eser:', count)
def uyesayi():

    tüye = open('üyeler.txt', "r", encoding="utf-8")
    count = 0
    for üye in tüye:
        count = count + 1
    print('Toplam üye:', count)
    tkinter.messagebox.showinfo('Toplam üye:', count)  #

    ####
#########################################


p.mainloop() # pencereyi ekranda göstermesi, kalmasını sağlar.
