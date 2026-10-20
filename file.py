ptr = open("sa.txt")
# dik = {}

# for i in ptr.read().split('\n'):
#     a = i.split(',')
#     a = str(a[-1])
#     if a not in dik:
#         dik[a]=1
#     else:
#         dik[a]=dik[a]+1
# print(dik)
# =============================1
# ls = []
# for i in ptr.read().split('\n'):
#     i=i.split(',')
#     # print(i)
#     if i[1] == 'visa':
#         ls.append(i)

# ls.sort(key=lambda x: x[-1])
# print(ls)
# ptr.close()
# ===============================2
# st = set()
# for i in ptr.read().split('\n'):
#     bolak=i.split(',')
#     if len(set(bolak[0]))==10:
#         print(i)
# ptr.close()
# ==================================3
# ======================================
# for mac in ptr.read().split("\n"):
#     bolak = mac.split(",")
#     for adres in bolak[-2].split("-"):
#         if adres.isdigit():
#             break
#     else:
#         print(mac)
# ptr.close()
# =========================================1
# dc = {}
# for i in ptr.read().split('\n'):
#     bol = i.split(',')
#     if bol[0].split('.')[1] not in dc:
#         dc[bol[0].split('.')[1]]=1
#     else:
#         dc[bol[0].split('.')[1]]=dc[bol[0].split('.')[1]]+1
# print(dc)
# ===========================================2
# for i in ptr.read().split('\n'):
#     a = i.split(',')
#     b = a[-1]
#     a = (a[2].split('-'))[-1]
    
#     if 2026-int(a)>=50 and b=="false":
#         print(i)

# ===================================================3
# import csv

# with open('sa.txt', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # Birinchi qatorni o'tkazib yuboradi
    
#     for row in reader:
#         print(row)
              

        


