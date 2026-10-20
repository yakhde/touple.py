# grades = {
#     "Ali": 85,
#     "Vali": 78,
#     "Hasan": 90
# }
# a = input("ismingiz: ")
# if a not in grades:
#     print("Bunday talaba topilmadi")
# else:
#     grades[a]=int(input("yangi baho: "))
#     print(grades)
# -----------------------------------------
# store = {
#     "olma": 5000,
#     "banan": 7000
# }
# a = input("maxsulot nomi: ")
# if a in store:
#     print("Bu mahsulot allaqachon bor")
# else:
#     store[a]=int(input("narxi: "))
# print(store)
# ------------------------------------------------
# employees = {
#     "101": "Ali",
#     "102": "Bobur",
#     "103": "Madina"
# }
# i = input("ID: ")
# if i in employees:
#     employees.pop(i)
# print(employees)
# ----------------------------------------
# prices = {
#     "Laptop": 700,
#     "Phone": 350,
#     "Camera": 500
# }
# print(max(prices.values()))
# --------------------------------------
# cart = {
#     "olma": 3,
#     "banan": 5,
#     "uzum": 2
# }
# print(sum(cart.values()))
# ----------------------------------------
# student = {
#     "name": "Aziz",
#     "age": 20,
#     "contact": {
#         "phone": "+998971234567",
#         "email": "aziz@mail.com"
#     }
# }
# print(student["contact"]["phone"])
# ----------------------------------------
# d1 = {"olma": 5000, "banan": 7000}
# d2 = {"shaftoli": 8000, "olcha": 10000}
# result={}
# result.update(d1)
# result.update(d2)
# print(result)
# -----------------------------------

# orders = [
#     {"customer": "Ali", "amount": 15000},
#     {"customer": "Vali", "amount": 22000},
#     {"customer": "Ali", "amount": 8000}
# ]
# dct={}
# for i in orders:
#     if i["customer"] not in dct:
#         dct[i["customer"]]=i["amount"]
#     else:
#         dct[i["customer"]]+=i["amount"]

# print(dct)
# -----------------------------------------------

# #  Birinchi usuli

# matn="salom dunyo salom python".split()
# dct={}
# for i in matn:
#     if i not in dct:
#         dct[i]=matn.count(i)
# print(dct)


# #  Ikkinchi usuli

# matn="salom dunyo salom python".split()
# dct={}
# for i in matn:
#     if i  not in dct:
#         dct[i]=1
#     else:
#         dct[i]+=1
# print(dct)
# ------------------------------------------------------
# keys = ['ten','tveny','thirty']
# val = [10,20,30]
# d = {}
# for i,x in zip(keys,val):
#     d[i]=x
# print(d)
# ----------------------------------------
# a = {'a':100, 'b':200, 'c':300}
# if 200 in a.values():
#     print("bor")
# ----------------------------------------

    
