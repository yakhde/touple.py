# def firs(n:str)->dict :
#     d={}
#     for i in n:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     return d

# a = 'f3wefrf'
# print(firs(a))
# -----------------------------------1
# def m(a:int,b:int)->int:
#     a=str(a)
#     b=str(b)
#     a=a+b
    # a=int(a)
#     return a
# k=9 
# n=6532 
# print(m(k,n))
# ------------------------------------------2
# def m(a:str)->str:
#     lst = []
#     for i in a.split():
#         lst.append(i[-1] + i[1:-1] + i[0])
#     return " ".join(lst)

# a = 'salom ali vali'
# print(m(a))
# -------------------------------------------------3
# def w(a:dict,b:dict)->dict:
#     s={}
#     for i,x in zip(a,b):
#         s[i]=a[x]+b[x]
#     return s
        
# a = {'a':100, 'b':200, 'd':300}
# b = {'a':400, 'b':200, 'd':400}
# print(w(a,b))
# -----------------------------------------------4
# def w(a:list)->list:
#     q=[]
#     for i in a:
#         q.append(i.split('@')[1])
#     return set(q)

# a = ["user1@gmail.com","user2@gmail.ru","user3@gmail.com"]
# print(w(a))
# --------------------------------------------------------5
# def w(a:list)->list:
#     q=[]
#     for i in a:
#         q.append(i+(i*1.2)//10)
#     return q

# a = [10000, 25000, 5000]
# print(w(a))
# ------------------------------------------------6
# def w(a:list)->list:
#     x=[]
#     for i in a:
#         for b in i:
#             if b=='@':
#                 x.append(i)
#     return x

# a = ["Ali, ali@gmail.com", "Vali, vali123@mail.ru", "Aziza, aziza@outlook.com"]
# print(w(a))
# ---------------------------------------------------------7

