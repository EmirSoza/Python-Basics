#SAYILAR VE STRINGLERE GIRIS

print("Hello AI ERA")

9*2


"Hello AI ERA"

'Hello AI ERA'

9 #int

9.2 #float

9 + 9 #matematiksel islem

#STRINGLER

type(123)

type("Ali")

type("123")


#STRING METODLARI

len("Merhabalar!")

len("MVK")

#atama islemi ve degisken olusturma

hi = "Hello AI ERA"

#del hi

len(hi)


#upper() & lower()

UP_HI = hi.upper()

UP_HI

hi

UP_HI.lower()

hi.isupper()
UP_HI.isupper()
UP_HI.islower()


#replace()

hi = hi.replace("l","p")

hi

dir(hi)


a = "123"

a.isdigit()


hi.title()



txt = "Welcome to My world"

x = txt.title()

print(x)

x.capitalize()


# SUBSTRINGLER

hi = "Hello AI ERA"

hi[0]

hi[7]

hi[6:8] #slicing

hi[9:12]

#DEGISKENLER

a = 9
a

b = 10

a * b

#KULLANICIDAN BILGI ALMA & TIP DONUSUMLERI

number = input()
number*3

type(number)


type(int(number))

int(number)*3

num1 = int(input())
num2 = int(input())

num1*num2

def topla():
    
    print("Toplama yapmak için birinci sayıyı giriniz:")
    
    num1 = int(input())
    
    print("Toplama yapmak için ikinci sayıyı giriniz:")
    
    num2 = int(input())
    
    print("İşlem sonucunuz:")
    
    print(num1 + num2)
    
    
topla()


# VERI YAPILARI

## Listeler

notes = [1, 2, 3, 4]

type(notes)

notes[0:2]

names = ["Python", "R","SPSS"]

notNam = [1,2,3, "R","SPSS"]


notNam[3]


len(notes)

all_list = [names, notes]

all_list[0]

all_list[1]


# Liste Eleman İşlemleri


names = ["Ali","Veli","berkcan", "ayse"]


names[1] = "velinin_babasi"

names[3] = "ayse_new"


# Liste Metodları

"abc".upper()

names

#listeye eleman eklemek icin kullanılır
names.append("Mehmet")


#remove
names.remove("Mehmet")

#insert

names.insert(0, "Mehmet")

names = ["Ali","Veli","berkcan", "ayse"]

names.insert(0, "Mehmet")

names


#pop

names.pop(0)
names

dir(names)
names.insert(0, "ali")


liste_yedek = names.copy()

dir(list)


names.index("ayse")


dir(list)

# TUPLE

t = ("ali","veli",1,2)
t
type(t)
len(t)
t[0:3]
t[2] = 9

names = ["Ali","Veli","berkcan", "ayse"]
names[0] = "FILIZ"



# Dictionary (Sözlükler)

sozluk = {"REG": "Regresyon Modeli",
          "LOG": "Logistic Regression",
          "CART" : "Classification and Reg"}



sozluk

len(sozluk)

sozluk["REG"]


sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}

sozluk["REG"]

sozluk = {"REG" : ["RMSE", 10],
          "LOJ" : ["MSE", 20],
          "CART" : ["SSE", 30]}


sozluk["REG"]




sozluk = {"REG": "Regresyon Modeli",
          "LOG": "Logistic Regression",
          "CART" : "Classification and Reg"}



sozluk["GBM"] = "Gradient Boosting Mac"


sozluk


#Veri Yapıları Özet Tablosu













#FUNCTIONS


def topla(a, b):
    print(a + b)
    
topla(3, 4)



def kare_al(x):
    print(x**2)


kare_al(9)

print("a", "b", sep = "_")

?print


def kare_al(x):
    
    """
    "Bu benim ilk fonksiyonumdur."
    
    x: karesini almak istediğin sayıyı gir
   
    """
    print("Girilen Sayının Karesi:" + str(x**2))


kare_al(10)


def carpma(a, b):
    print(a * b)

carpma(5,7)


liste = [9, 4]
    
liste.append(9*4)
    
print(liste)



def karmasik(a, b):
    
    liste = [a, b]
    
    liste.append(a*b)
    
    print(liste)

karmasik(9, 4)



def karNo():
    
    liste = [1, 2]
    
    liste.append(9*9)
    
    liste.append(9999)
    
    print(liste)

karNo()



#On tanimli argumanlar


def carpma_yap(x, y = 1):
    print(x*y)


carpma_yap(9)

#Argumanlarin siralamasi


carpma_yap(y = 8, x = 9)

#Ne zaman fonksiyon yazilir?


a = "Data Scientist"

len(a)


#isi, nem, sarj

(56 + 15)/80

def hesaplama(isi, nem, sarj):
    
    print((isi + nem)/sarj)



hesaplama(90, 18, 87)**2

cikti = hesaplama(90, 18, 87)

cikti*2

print(cikti)



def hesaplama(isi, nem, sarj):
    
    return int((isi + nem)/sarj)

hesaplama(90,9,1)*2

cikti = hesaplama(1,2,3)
cikti
cikti*2



#Local ve Global Değişkenler

x = 1
y = 10

def carpma_yap(x = 2, y = 1):
    return x*y



liste = []



def eleman_ekle(y):
    
    liste.append(y)
    
    
eleman_ekle()  
  
eleman_ekle(10)

eleman_ekle("abc")



# Karar & Kontrol Yapıları

1 == 2
1 == 1

sinir = 1000


sinir == 3000



sinir > 4500

sinir > 4500


sayi_gir = int(input())

if sayi_gir > 4500:
    print(sayi_gir * 999)
    
else:
    print(sayi_gir*1) 



def if_func():
    
    sayi_gir = int(input())

    if sayi_gir > 4500:
        print(sayi_gir * 999)
    else:
        print(sayi_gir*1) 


if_func()


#elif
sinir = 5000

gelir = int(input())

gelir > sinir


if gelir > sinir:
    print("Tebrikler ikramiye kazandiniz")
    
elif gelir < sinir:
    print("Daha cok calis")    
    
else: 
    print("Takibe devam")






#Donguler - for 

ogrenciler = ["ali","veli","isik","berk"]

ogrenciler[0]
ogrenciler[1]
ogrenciler[2]
ogrenciler[3]

ogrenciler[0].upper()


for ogrenci in ogrenciler:
    print(ogrenci, ogrenci.upper())


maaslar = [1000, 2000, 3000, 4000, 5000]

maaslar[0]

def kare_al(mvk):
    print(mvk**2)

kare_al(10)


1000*20/100 + 1000

maaslar[2]*20/100 + maaslar[2]

def yeni_maas(x):
    print(x*20/100 + x)
    
yeni_maas(1000)


for maas in maaslar:
    yeni_maas(maas)




def bolme(a,b):
    print(a/b)


bolme(6,7)


a = 1
b = 10
c = a*b*9
print(c)


def islem():
    a = 1
    b = 10
    c = a*b*9
    print(c)


islem()

#if, for ve fonksiyonlarin beraber kullanımı


maaslar = [1000, 2000, 3000, 4000, 5000]

def maas_ust(x):
    print(x*10/100 + x)

def maas_alt(x):
    print(x*20/100 + x)


for maas in maaslar:
    
    if maas >= 3000:
        
        maas_ust(maas)
        
    else:
        maas_alt(maas)

#break & continue

maaslar = [8000,5000,2000,1000,3000, 7000, 1000]


maaslar.sort()

maaslar

for maas in maaslar:
    if maas == 3000:
        print("Kesildi")
        break
    
    print(maas)


for maas in maaslar:
    if maas == 3000:
        continue
    print(maas)


#while 

sayi = 1

while sayi < 9:
    sayi += 1
    print(sayi)

def kenan(a,b):
    print(a)
    return a * b

kenan(1,2)

x = range(3, 6)

for n in x:
  print(n)


for i in range(1,100):    
    print(i)



maaslar = [1000, 2000, 3000, 4000, 5000]

 

for i in maaslar:
    if i >= 3000 :
        print(i*10/100 + i)
    else:
        print(i*20/100 + i)
        
        
#PYTHON V3        

def old_sum(a,b):
    return a + b

old_sum(4,5)



new_sum = lambda a, b, c: a + b + c


new_sum(4,5,6)

#map

maaslar = [1000, 2000, 3000, 4000, 5000]

for maas in maaslar:
    print(maas*2)
    
list(map(lambda x: x*20/100 + x, maaslar))


#filter


liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, liste))

#reduce

from functools import reduce

liste = [1,2,3,4]

reduce(lambda a,b: a+b, liste)


        
        