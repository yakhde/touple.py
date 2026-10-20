# print("salom")
# ism=input("ismingizni kiriting: ")
# print("salom ",ism)
# ism = "ali"
# yosh = 19
# boyi = 1.75
# print(f"salom {ism} yoshi {yosh} boyi {boyi} dan")

# ism = input("ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# print(f"Salom {ism} {yosh}da")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh>15:
#     print("ok")

# mevalar = ["olma", "banan", "olcha", 100, True]
# mevalar.append("uzum")
# print(meva)

# mevalar = [1 , 2 , 3 , 4 , 5 ,True ]
# mevalar.append('uzum')
# print(mevalar)

# son = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] 
# print(son[2:6])
# print(son[:4])
# print(son[5 :])
# print(son[::2])
# print(son[::-1])

# juft_sonlar = []
# for x in range(10):
#     juft_sonlar.append(x)


# a = int(input("Togilgan kuningizni kiriting: "))
# b = int(input("Togilgan oyingizni kiriting: "))
# print(f"Brithday is {a} {b}")

# a = int(input("3 xonali son kiriting: "))
# b = a//100
# c = (a//10)%10
# d = a%10
# print((b+c+d)*(b+c+d)*b+c+d)

# a = int(input("1 son: "))
# b = int(input("2 son: "))
# print((a+b)/2)

# a = int(input("2 xonali son kiriting: "))
# b = a%10
# c = a//10
# a = b*10+c
# print(a)

# a = input("ismni kiriting: ")
# b = input("Familyani kiriting: ")
# print(f"salom {a} {b}")

# a = int(input("1 son: "))
# b = int(input("2 son: "))
# k = a*b
# ay = a-b
# bol = a/b
# q = a+b
# print(f" Qoshish: {q} \n Ayirish: {ay} \n Kopaytirish: {k}\n bolish: {bol} ")

# a = input("harf kiriting: ")
# a = ord(a)-96
# print(f"alfabit boyicha {a}")

# a = input("soz kiriting: ")
# a = len(a)**3
# print(f"Kub= {a}")

# a = int(input("Tugilgan yilingizni kiriting: "))
# a = 2026-a
# print(f"Yoshingiz: {a}")

# a = input("Harf kiriting: ")
# a = chr(ord(a)-32)
# print(a)

# a = input("Harf kiriting: ")
# a = chr(ord(a)+1)
# print(a)

# b = int(input("Rni kirting: "))
# c = 3.14
# a = (b*b)*c
# print(f"Yuza = {a}")

# massiv = []
# for i in range(5): 
#     son = int(input("Son kirit: "))
#     massiv.append(son)
# print(massiv)    

# a = int(input("Yoshingiz: "))
# print(2026-a)
    

# s = int(input("Sukund kiritng: "))
# s = s//3600
# print(f"soat= {s}")

# a = input("ism: ")
# s = int(input("nechta dosting bor: "))
# print(f"{a}ning {s}ta dosti bor")

# a = int(input("maxsulot narxi: "))
# s = int(input("nchta olding: "))
# s = s*a
# print(f"umumiy summa {s}")

# a = input("Ism: ")
# b = int(input("yosh: "))
# c = input("shashar: ")
# print(f"Ism: {a}\n Yoshi: {b}\n Shahar: {c}")


# a = int(input("3xonali son kirti: "))
# b = a%10
# c = (a//10)%10
# d = a//100
# q = (b*100)+(c*10)+d
# if a == q:
#     print("ha")
# else:
#     print("yoq")

# a = int(input("son kirit: "))
# b = int(input("son kirit: "))
# c = int(input("son kirit: "))

# if a > b and b>c or a<b and b<c:
#     print(a*2,b*2,c*2)
# else:
#     print(a*(-1),b*(-1),c*(-1))

# n = int(input("son: "))
# a = n*'()'
# q = 0
# while q<n:
#     print(f'["{a}"],',end=" ")
#     a = a.replace("()","",1)
#     q=q+1

# nums = [13,25,83,77]
# nat = []
# for i in nums:
#     for x in str(i):
#        nat.append(int(x))
# print(nat)

# nam = input("matn: ")
# nat = []
# for i in nam:
#     for x in str(i):
#         nat.append(str(x))
# print(nat)

# nums = [1, 3, 3, 4, 2]
# nums.sort()
# print(nums)
# n = len(nums)
# lamp=0
# for i in nums:
#     if nums[n-1]==i:
#         # print(i,end=" ")
#         lamp = lamp+1
#     if nums[-1] == 
# if n-1==nums[-1] and lamp==2:
#     print("True")



# dct={
#     47485:"Raxmanoli",
#     45072: "Shohrux",
# }
# print(dct)

# dct={
#     "apple":"olma",
#     "banana":"banan"
# }









# lst=[]
# lst.append(23)
# # lst.append(int(input("- ")))
# a=78
# lst.append(a)

# print(lst)

# natija=lst.copy()  # nusxa qilish
# indx=natija.index(78)  #  indxini bilish
# sanaldi=natija.count(78)  # shu qiymatdan nechta borligini bilish
# natija.pop(0)  # index orqali ochirish
# natija.remove(78) # qiymat bilan list ichidagi qiymatni ochirish
# natija.sort()   # oziga tasir qiluvchi sortlash
# sortlandi=sorted(lst) # sortlangan xolatni qaytarib beradi oziga tasir korsatmaydi
# natija.clear()  # tozalash

# print(natija)


# lst=[]
# while 1:
#     son=int(input())
#     if son == 0:
#         break
#     else:
#         lst.append(son)
# natija=sorted(lst)
# lst.sort()
# print(natija)

# lst = []
# while 1:
#     son = int(input("->"))
#     if son==0:
#         break
#     else:
#         lst.append(son)

# print(lst.count(int(input("k="))))

# lst=[int(input()), input("- "), ]


# lst = []
# while 1:
#     son = int(input("-> "))
#     if son==0:
#         break
#     else:
#         lst.append(son)
# print(f"MAX: {max(lst)} \n Index: {lst.index(max(lst))}")

# lst = []
# while 1:
#     son = input("s= ")
#     if son=='0':
#         break
#     else:
#         lst.append(son)
# print(lst)
# for i in lst:
#     for x in lst:
#         if i==x:
#             lst.remove(i)
# print(lst)



# lst=[1, 2, 2, 3, 4, 1, 5, 3]
# natija=[]
# for i in lst:
#     if i not in natija:
#         natija.append(i)
# print(natija)


# #    0  1  2  3  4  5  6  7
# lst=[1, 2, 2, 2, 3, 4, 1, 5, 3]
# for i in lst[::]:
#     if lst.count(i) >1:
#         lst.remove(i)
# print(sorted(lst))





# lst=[1, 2, 2, 2, 3, 4, 1, 5, 3]

# while 1:
#     son=int(input("- "))
#     if son in lst:
#         print("bor")
#     else:
#         print("Yoq")


# lst=[1, 2, 2, 2, 3, 4, 1, 5, 3]
# nat = []
# for i in lst:
#     if i not in nat:
#         nat.append(i)
# print(nat)

# st="1,2,2,1,3,5,5,2"
# aq = []
# for i in st:
#    if i>='0' and i<='9':
#       aq.append(int(i))
# print(aq)

# for i in aq:
#    if aq.count(i)==1:
#       print(i)


# print(max(aq))


# st="1,2,2,1,3,5,5,2"
# lst=st.split(",")
# print(min(lst, key=lst.count))



# st="1,2,4,2,1,3,5,5,2"
# natija=[int(i) for i in st if i>='0' and i<='9']
# print(set(natija))  # qiymatlarni unikal qilish

# ad = []
# for i in range(7):
#     h=int(input(f"{i+1} kun havo harorati: "))
    
#     if h>=0 and h<=15:
#         ad.append("Sovuq")
#     elif h>=15 and h<=25:
#         ad.append("normal")
#     if h > 25:
#         ad.append("juda issiq")
#     else:
#         ad.append("juda sovuq")
# print(s)














