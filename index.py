from tkinter import * # * tüm paremetleri kullanıcağımızı belirtmek için koyduk.
import tkinter.messagebox
import tkinter as tk
#from PIL import Image, ImageTk
###from final2.py import *

girisbilgi = ["1", "1"]
def girbilgiler():
    h = Tk()
    h.title("Giriş Bilgileri")
    h.geometry("200x30")
  # YAZI LABELI  Label(sh, text=(p,"Kullanıcı Adı : ", (girisbilgi[0]), "Şifre : ", girisbilgi[1]), fg="darkgreen", justify=CENTER).pack()
    tkinter.messagebox.showinfo ("TEST", ("Kullanıcı Adı : ", girisbilgi[0],"Şifre : ", girisbilgi[1]))

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
    mesaj.config(text="SİSTEME HOŞGELDİNİZ.\n Sistem menüsüne geçmek için tıklayınız...", bg= "black", fg= "pink",font=("Comic Sans MS",15,"bold"),command=menu)
    girbilgi.destroy()
    mesaj.pack()

   # yapımcı = Label(p)
   # yapımcı.config(text="Tasarlayan : ONUR ÖZTÜRK", bg="black", fg="white", font=("Times New Roman", 10))
    #yapımcı.pack




    ####
 # üst 3 oky
p = Tk()
p.title("KÜTÜPHANE SİSTEMİ 1.0")
p.geometry("800x250") # ayarlarını sonra yap genişlik yükseklik
p.resizable(FALSE, FALSE) # küçültüp büyütmeyi kapatıyor
p.config(bg="black") # config komutu o kutucuğu vs. ayarlıyor.

girbilgi = Button(p)
girbilgi.config(text="Sifre Hatırla",bg="black", fg="yellow", font=("Comic Sans MS", 10),justify=CENTER, command=girbilgiler)
#girbilgi.grid(row=3, columnspan=15, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
girbilgi.pack()

kadisor = Label(p)
kadisor.config(text="Kullanıcı adınız : ", bg="black", fg="red", font=("Comic Sans MS", 20),justify=CENTER)
kadisor.pack()

kadial = Entry(p,justify=CENTER) #entry kullanıcı girişi için input verr
kadial.pack()

sifresor = Label(p)
sifresor.config(text="Şifreniz : ", bg="black", fg="red", font=("Comic Sans MS", 20),justify=CENTER)
sifresor.pack()

sifreal = Entry(p, width="15", show="*",justify=CENTER)
sifreal.pack()

girb = Button(p)
girb.config(text="GİRİŞ", bg="black", fg="red", activebackground="blue", activeforeground="white", font=("Comic Sans MS", 12),justify=CENTER, command=gir)
girb.pack(side=LEFT)

çıkb = Button(p)
çıkb.config(text="ÇIKIŞ", bg="black", fg="red", activebackground="blue", activeforeground="white", font=("Comic Sans MS", 12),justify=CENTER, command=quit)
##tkinter.messagebox.showwarning("BHKS 1.0", "Çıkış yapmak istediğinizden emin misiniz?")
çıkb.pack(side=RIGHT) # pack modülü uygulamaya, ekrana eklemek için kullanılır.


def menu():
    p = Tk()
    p.title("Kütüphane Otomasyonu")
    frame = Frame(p)
    frame.pack()

    bottomframe = Frame(p)
    bottomframe.pack(fill=BOTH,expand=5, side = BOTTOM )

    b1 = Button(frame, text="ESER EKLE", fg="red", font=("Comic Sans MS ",25),width=25,justify=CENTER, command=kitap_ekle)
    b1.pack()
#    b1.grid(column=0, row=3)

    b2 = Button(frame, text="ESER SİL ( EKLENECEK )", fg="brown", font=("Comic Sans MS ",25),width=25,justify=CENTER)
    b2.pack()
 #   b1.grid(column=1, row=3)
    b3 = Button(frame, text="ÜYE EKLE", fg="black", font=("Comic Sans MS ",25),width=25,justify=CENTER, command=üyeekle)
    b3.pack()
  #  b1.grid(column=2, row=3)
    b4 = Button(frame, text="ÜYE SİL ( EKLENECEK )", fg="blue", font=("Comic Sans MS ",25),width=25,justify=CENTER)
    b4.pack()
   # b1.grid(column=3, row=3)
    b5 = Button(frame, text="ESER ARAMA ( EKLENECEK ) ", fg="orange", font=("Comic Sans MS ",25),width=25,justify=CENTER) # ayarlacommand=uyelist)
    b5.pack()
    b6 = Button(frame, text="ESER LİSTESİ", fg="red", font=("Comic Sans MS ", 25), width=25, justify=CENTER, command=eserlist)
    b6.pack()
    #    b1.grid(column=0, row=3)

    b7 = Button(frame, text="ÜYE LİSTESİ", fg="brown", font=("Comic Sans MS ", 25), width=25, justify=CENTER,command=uyelist)
    b7.pack()
    #b1.grid(column=4, row=3)
    p.mainloop()
#side = LEFT


########################################
def kitap_ekle():
        global kitap_adi,yazar_adi,yy,p1
        p1 = Tk()
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

        sistem = str(("Kitap Adı:" +kitap_adi.get() + "-Yazar Adı:" + yazar_adi.get()+ "-Yayın Yılı:" + yy.get()) + "\n")
        dosya = open("eserler.txt", "a", encoding="utf-8")
        for x in sistem:
            dosya.write(x)
        dosya.close()
        print("KAYDEDİLDİ..")
        #messagebox.showinfo('Mesaj', 'Kitap Başarıyla Eklendi..', command= p1.destroy())
def üyeekle():
    global üyeadisoyadi, üyeno, üyeyaş, p1
    p1 = Tk()
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
    sistem = str(("Üyenin Adı Soyadı:" + üyeadisoyadi.get() + "~ Üye Kayıt No:" + üyeno.get() + "~ Üyenin Yaşı:" + üyeyaş.get()) + "\n")
    dosya = open("üyeler.txt", "a", encoding="utf-8")
    for x in sistem:
        dosya.write(x)
    dosya.close()
    print("KAYDEDİLDİ..")
    # messagebox.showinfo('Mesaj', 'Kitap Başarıyla Eklendi..', command= p1.destroy())
def eserlist():
    p = Tk()
    ebaslık = p.title("KAYITLI ESERLER")
    p.configure(background="black")
    file = open("eserler.txt", "r", encoding='utf8')
    data = file.read()
    file.close()
    üye_liste = Label(p, text=data, fg="yellow", bg="black",justify=CENTER)
    üye_liste.pack()
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

    üye_liste = Label(p, text=data, fg="yellow", bg="black")
    üye_liste.pack()

    cıkıs = Button(p, text="Kapat", command=p.destroy, fg="black", bg="RED",justify=CENTER)
    cıkıs.pack()
    p.mainloop()
def esersayi():

    teser = open('eserler.txt', "r", encoding="utf-8")
    count = 0
    for eser in teser:
        count = count + 1
    print('Toplam eser:', count)
    tkinter.messagebox.showinfo('Toplam eser:', count,)
def uyesayi():

    tüye = open('üyeler.txt', "r", encoding="utf-8")
    count = 0
    for üye in tüye:
        count = count + 1
    print('Toplam üye:', count)
    tkinter.messagebox.showinfo('Toplam üye:', count,)  #

    ####
#########################################



p = mainloop() # pencereyi ekranda göstermesi, kalmasını sağlar.
