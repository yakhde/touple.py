# a = int(input("dan-> "))
# c = int(input("gacha-> "))
# b = int(input("qidirsin-> "))
# for i in range(a,c,1):
#     if i==b:
#         print("bor")

# a = int(input("a-> "))
# b = int(input("b-> "))
# c = int(input("c-> "))
# co = 0
# if a>0:
#     co+=1
# if b>0:
#     co+=1
# if c>0:
#     co+=1
# print(co)

# a = int(input("a-> "))
# b = int(input("b-> "))
# c = int(input("c-> "))
# e = 0
# if a<c and a<b:
#     e += b+c
# if b<c and b<a:
#     e += a+c
# if c<a and c<b :
#     e += a+b
# print(e)



# a = int(input("a-> "))
# b=0
# c=0
# while b<=a:
#     if a%2==0:
#         c+=1
#     b+=1
# if c == 2 :
#     print("tub ")


# a = int(input("a-> "))
# b = int(input("b-> "))
# if a%2 and b%2:
#     print("toq")

# a = int(input("a-> "))
# if a%2==0 and len(str(a))==2:
#     print("2 juft")



# a = int(input("a-> "))
# if a%2 and len(str(a))==3:
#     print("ha")



# a = int(input("a-> "))
# a1 = a//100
# a2 = a//10%10
# a3 = a%10
# if a1!=a2 and a2!=a3 and a1!=a3:
#     print("ha")

# a = int(input("a-> "))
# if a>0:
#     print("musbat")
# else:
#     print("manfiy")
# print(len(str(a)))

# a = int(input("a-> "))
# a1 = a//100
# a2 = a//10%10
# a3 = a%10

# if a1>a2>a3:
#     print("osish")
# elif a1<a2<a3:
#     print("kamayish")


# a = input("film nomi-> ")
# b = int(input("yoshngiz-> "))

# if b<12:
#     print(f"{b} yoshli foydalanuvchi Animatsiya yoki Oila janiri tavsiya")
# elif 12<b<18:
#     print(f" {b} yoshli foydalanuvchi Action yoki Sarguzasht janrini tavsiya")
# elif 18<b<60:
#     print(f"{b} yoshli foydalanuvchi  Drama yoki Komediya janrini tavsiya")
# elif b>60:
#     print(f" {b} yoshli foydalanuvchi Dokumental yoki Klassik janrini tavsiya")


# a = int(input("1chi mahsulot narxini: "))
# b = int(input("2chi mahsulot narxini: "))
# c = int(input("3chi mahsulot narxini: "))
# j = a+b+c
# print(j)
# if j>100 and j<200:
#     print("10% chegirma")
#     print(j-(j*0.10))
# elif j>200  and j<500:
#     print("15% chegirma")
#     print(j-(j*0.150))
# elif j>500:
#     print("20% chegirma")
#     print(j-(j*0.20))


# while 1:
#     h = input("harorat: ")
#     if h == 'exit':
#         break
#     if h<'32':
#         print("muzlash")
#     elif h>'85':
#         print("issiq")
#     elif '32'<h<'85':
#         print("yaxhsi kun")


# a = int(input("yosh: "))
# b = int(input("necha yil obuna: "))
# oy = b*15
# if a>=50 and b>3 and b<5:
#     print(oy+(oy*0.30))
# elif a>=50 and b>5:
#     print(oy+(oy*0.35))
# elif a<50 and b>3 and b<5:
#     print(oy+(oy*0.10))
# elif a<50 and b>5:
#     print(oy+(oy*0.15))


# a = input("parol:")
# a.replace(" ","")
# if len(a)>=8 :
#     c=0
#     for i in a:
#         if i == '@' or i == '#' or i == '$' :
#             c+=1
#     if c>0:
#         print("Trua!! ")
#     else:
#         print("belgi yoo")
# else:
#     print("Juda qisqa")


# for i in range(3):
#     a = input(f"{i+1} kompaniya: ")
#     b = int(input(f"{i+1} aksiya: "))
#     if b>=150:
#         print("Qimmat")
#     elif b<=50:
#         print("Azon")
#     elif 50<b<150:
#         print("otacha")

# lst = ['32','9','123','1994','1024','998','1998']   
# for i in lst:
#     if len(i)==1:
#         yeg = int(i)
#     elif len(i)==2:
#         a1 = int(i)%10
#         a2 = int(i)//10
#         yeg = a1+a2
#     elif len(i)==3:
#         a1 = int(i)%10
#         a2 = int(i)//10%10
#         a3 = int(i)//100
#         yeg = a1+a2+a3
#     elif len(i)==4:
#         a1 = int(i)%10
#         a2 = int(i)//10%10
#         a3 = int(i)//100%10
#         a4 = int(i)//1000
#         yeg = a1+a2+a3+a4
#     if yeg%2==0:
#         lst = lst[i]+yeg
# print(lst)


# t =  "sAlOm lli"
# t = t.casefold()
# print(t)


# ism = input("i: ")
# ism = ism.capitalize()
# print(ism)


# a = "salom  man  ali gef"
# a = a.capitalize()
# print(a)


# a = "salom men kdjknjd"
# a = a.title()
# print(a)

# a = "salom ,sdnfjs jnsgfkosg"
# a = a.upper()
# print(a)

# a = "SADf kgmsdkjg kmkfgs" 
# a = a.swapcase()
# print(a)

# a = "salom  ali aASD"
# a = a.isupper()
# print(a)

# a = "salom file"
# # a = a.islower()
# # a = a.lstrip('e') # ondan ochiradi
# # a = a.rstrip('e') # chapdan ochiradi
# a = a.rjust(20)


# ism = "     aLI vALiYeV   "
# ism = ism.capitalize()
# ism = ism.title()
# ism = ism.lstrip()


# a = "Mening telegramim @Alisher_Dev, bog'lanishingiz mumkin."
# for i in a.split():
#     soz = i.strip(".,!'")
#     if soz=='@':
#         print(i)

# matn = "Mening telegramim. @Alisher_Dev, bog'lanishingiz mumkin."

# # username = "Username topilmadi"
# for i in matn.split():
#     toza = i.strip(",.!?")
    # if toza.startswith("@"):
#         username = toza.lower()
#         break
# print("")
# print(username)


# matn = "Mening telegramim. @Alisher_Dev, bog'lanishingiz mumkin."
# user = "no"
# for i in matn.split():
#     i = i.strip(".,'!")
#     if i.startswith("@"):
#         user = i
# print(user.lower())

# matn = "Mening telegramim. @Alisher_Dev, bog'lanishingiz mumkin."
# up = "no"
# for i in matn.split():
#     i.strip(".,!")
#     if i.startswith("@"):
#         up = i
# print(up)


# a = "python dasturlash tili"
# b = []
# for  i in a.split():
#     b.append(i.capitalize())
# print(b)


# a = "vaqtingizni qadrlang"
# print(a.upper())

# a = "PyThOn 3.12"
# print(a.swapcase())


# a = "   bot_user   "
# print(a.strip(" "))
# print(a)

# a = "fayl_nomi.pdf    "
# print(a.rstrip(" "))


# a = "...salom,,"
# print(a.strip('.,'))


# a = "###Xush kelibsiz!###"
# print(a.strip())

# a = "  aLiVaLiYeVs"
# print(a.lower.)

# a = "   bot_user   "
# print(a.lstrip(" "))


# a = "aLi VaLiYeVs"
# a = a.lower()
# print(a.title())


# a = "998901234567"
# print(a.isdigit())

# a = "Dasturchi"
# a = a.lower()
# print(a.isalpha())

# a = "User123"
# print(a.isalnum())


# a = "python"
# # print(a.islower())
# a = a.upper()
# print(a)


# a = "PYTHON"
# print(a.isupper())

# a = "Alisher Navoiy"
# a = a.istitle()
# print(a)

# a = "   \n\t  "
# print(a.isspace())


# a = "123.45"/
# print(a.isdigit())

# a = " [https://google.com](https://google.com) "
# print(a.startswith(" [https:"))

# a = "hujjat.docx"
# print(a.endswith("docx"))

# a = "banana"
# print(a.count('a'))


# a = "admin@site.com"
# print(a.find('@'))

# a = "index.old.backup.txt"
# print(a.find('.'))

# a = "abracadabra"
# print(a.count("ab"))

# a = "C:/Users/Admin/Desktop/file.py"
# print(a.rfind('/'))

# a = "admin@site.coma"
# print(a.find('a'))

# a = "C:/Users/Admin/Desktop/file.py"
# print(a.count("/"))

# a = "C:/Users/Admin/Desktop/file.py"
# print(a.find('C'))

# a = "Bugun havo juda yaxshi"
# # a = a.split()
# print(a.index("havo"))

# a = "abracadabra"
# print(a.center("a"))

# a = "olma,banan,uzum,gilos"
# print(a.split(','))

# a = "   sALoM dUNyo   "
# a = a.lower()
# # a = a.title()
# a = a.strip()
# print(a.capitalize())


# a = "USER.NAME@GMAIL.COM"
# a = a.lower()
# a = a.strip('.')
# print(a.strip('.'))


# a = "998901234567"
# print(a.isdigit())


# a = "Dasturchi"
# print(a.isalpha())


# a = "User123"
# print(a.isalnum())

# a = "python"
# print(a.upper())

# a = "PYTHON"
# print(a.isupper())

# a = "Alisher Navoiy"
# print(a.istitle())

# a = "   \n\t  "
# print(a.isspace())

# a = "123.45"
# print(a.isnumeric())

# a = "[https://google.com](https://google.com)"
# print(a.endswith(")"))

# a = "hujjat.docx"
# print(a.endswith("docx"))

# a = "banana"
# print(a.count("a"))

# a = "admin@site.com"
# print(a.index('@'))

# a = "index.old.backup.txt"
# print(a.rindex('.'))

# a = "Matn ichida dastur so'zi bor"
# # a = a.split()
# print(a.index("bor"))

# a = "salom dunyo"
# print(a.rfind(" "))

# a = "olma, banan, olma, uzum"
# print(a.count("olma"))

# a = "C:/Users/Admin/Desktop/file.py"
# print(a.index('/'))

# a = "0123456789"
# print(a.index('5'))

# a = "Bugun havo juda yaxshi"
# print(a.find('havo'))

# a = "abracadabra"
# print(a.count('ab'))

# a = "olma,banan,uzum,gilos"
# a = a.split(',')
# print(a)

# a = "Bugun havo ochiq"
# a = a.split()
# print(a)


# a = ['Python', 'Django', 'Flask']
# asd = " <-> ".join(a)
# print(asd)

# a = "olma,banan,uzum,gilos"
# # a.split(",")
# li = []
# li = a.split(",")
# print(li)


# a = "Bugun havo ochiq"
# a = a.split()
# print(a)

# a = ['Python', 'Django', 'Flask']
# asd = " ".join(a)
# print(asd)

# a = ['2026', '10', '05']
# asd = "-".join(a)
# print(asd)

# a = "Yomon odatni tashlang"
# a = a.replace("Yomon","Yaxshi")
# print(a)

# a = "+998 (90) 123-45-67"
# a = a.replace("+"," ").replace("(","").replace(")","").replace("-"," ")
# print(a)

# a = "bir-ikki-uch-to'rt"
# a = a.replace("-",":",1)
# print(a)


# a = "user@gmail.com"
# a = a.partition('@')
# print(a)


# a = "D:/Projects/Python/main.py"
# a = a.rpartition('/')
# print(a)


# a = "Qator1\nQator2\nQator3"
# a = a.splitlines('\n')
# print(a)

# a = "7"
# a = a.zfill(5)
# print(a)



# a = "SALOM"
# a = a.center(30,'-')
# print(a)


# a = "Menyu"
# print(a.ljust(20,'-'))

# a = "15000 SO'M"
# print(a.rjust(20,"-"))

# a = "45"
# a = a.zfill(5)
# print(a)

# a = "PYTHON"
# a = a.center(10,"*")
# print(a)


# a = "hello"
# a = a.ljust(10,"-")
# print(a)

# matn = 'sAlom foundation n227'
# natija = matn.lower().count('a')
# print(natija)

# lst = ['32','9','123','1994','1024','998','1998']  
# for q,i in enumerate(lst):
#     s = 0
#     for x in i:
#         s += int(x)
#     if s%2==0:
#         i = i+str(s)
#     lst[q]=i
# print(lst)   

    

# lst = [7, 4, 1, 6, 5]
# lst.sort()
# k = lst[0]
# # print(lst)
# for q,i in enumerate(lst):
#     if k!=i:
#         print(k)
#         k = k+1
#         if k!=i:
#             k = k+1
#             print(i-1)
        
#     k = k+1



# lst = [7, 4, 1, 6, 5, 9, 8, 12]
# for i in range(min(lst), max(lst)+1):
#     if i not in lst:
#         print(i)

# a = "   test   "
# a = a.strip(" ")
# print(a.zfill(20))



# a = "1234"
# a = a.zfill(6)
# print(a)

# lst = ["salom","molas",'dsl']
# lst.insert(0,'a')
# print(lst)


# lst = ["salom","molas",'dsl']
# lst1 = ["olma","anor"]
# lst.extend(lst1)
# print(lst)

# lst = ["salom","molas",'dsl']
# lst.remove('salom')
# print(lst)


# lst = ["salom","molas",'dsl']
# lst.pop()
# print(lst)


# lst = ["b", "a", "d", "c"]
# lst = ['1','9','5','3','7']
# lst.sort()
# print(lst)


# lst = ['1','2','3','4','5','6']
# lst.reverse()
# print(lst)

# ls = [1, 2, 3]
# b = ls.copy()
# print(b)

# sonlar = [1, 2, 3]
# sonlar.append(4)
# print(sonlar)

# mevalar = ["olma", "uzum"]
# mevalar.insert(0,"anor")
# print(mevalar)

# a = [1, 2]
# a = 