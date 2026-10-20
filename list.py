# lst = [True,"salom",5,5.5]
# for a,i in enumerate(lst):
#     lst[a] = type(i)
# print(lst)


# ls = [7,8,1,3,4,6,7,5]
# for a,i in enumerate(ls):
#     if a%2:
#         ls[a]=i*i*i
#     else:
#         ls[a]=i*i
# print(ls)

# ls = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
# las = []
# m=0
# for a, i in enumerate(ls.copy()):
#     if i!=0:
#         las.append(i)
#     else:
#         m+=1
# for i in range(m):
#     las.append(0)         
# print(las)

# ls = [2,1,-4,-9,0,-5,8,3]
# ls.sort()
# a= max(ls)
# for q,i in enumerate(ls):
#     if i==a:
#         p=ls[q-1]
#         # print(q)
# print(p)


# ls = [2,5,4,3,1,1,6,8,5,7,9]
# sa = []
# for i in ls.copy():
#     if i not in sa:
#         sa.append(i)
# print(sa)

# ls = [11,33,50]
# a=[]
# for i in ls.copy():
#     a = a + str(i)
# print(a)
            
# lst = [1,2,4,5,6]
# ls = []
# for i in range(min(lst),max(lst)+1):
#     if i not in ls:
#         ls.append(i)
# p


# strs = ["flower","flow","flight"]
# new=''
# for i,x,w in zip(strs[0],strs[1],strs[2]):
#     if i==x and x==w:
#         new +=i
# print(new)

# strs = ["interspecies","interstellar","interstate"]
# new=''
# for i,x,w in zip(strs[0],strs[1],strs[2]):
#     if i==x and x==w:
#         new +=i
# print(new)

# lst = [11,33,50]
# n = ''
# for i in lst:
#     n+=str(i)
# print(n)

# a1 = [1,1,3,4,4,5,6,7]
# a2 = [0,1,2,3,4,4,5,7,8]
# l2 = len(a2)+len(a1)
# su = ''
# for i in  a1:
#     su += i 
# for i in a2:
#     su +=i
# print(su/l2)


# l = ['ada',212,False,"aziza"]
# for i in l:
#     s = str(i)
#     if s == s[::-1]:
#         print(i)

        
# l = ['abc','len','bolib','aba',1221]
# son = 0
# for i in l:
#     i = str(i)
#     if len(i)>2 and i[0]==i[-1]:
#         son +=1
# print(son)


# l = [123,54,65,8,78,89]
# ls = l.copy()
# for x,i in enumerate(ls):
#     if i%2==0:
#         l.remove(i)
# print(l)

# l = [[1,2,3],[4,5,6],[9,27],[2,0,10],[0,1],[1],[2,2,2]]
# for i in l:
#     if len(i)>=2:
#         print(max(l, key=sum))
#         break

# l = [1,2,3]
# ls = ''
# for i in l:
#     i = str(i)
#     ls+=i
# l.clear()
# ls = int(ls)+1
# for i in str(ls):
#     l.append(i)
# print(l)

# a = [1,5,6,9,12,54,6,5,55,98]
# b = [4,56,5,9,8,7,65,45,44,69]
# c =[]
# for x in a:
#     if x  in b:
#         c.append(x)
# print(c)

    
# a = [5,3,8,1]
# c = a.copy()
# b = a.copy()
# b.reverse()
# a.sort()
# if c==a:
#     print("sortlangan")
# elif c==b:
#     print("sortlanmagan")
# else:
#     print("aralash")


#  dict

# dct={
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "M": 1000,
#     "C": 100,
#     "D": 500,
#     "L": 50
# }
# rim=input(">>>> ").upper()
# jami=0
# l = True
# if dct[rim[0]]<dct[rim[-1]]:
#     for i in rim:
#         if dct[i]==dct[rim[-1]]:
#             jami = dct[rim[-1]]-jami
#         else:
#             jami = jami+dct[i]

# print(jami)



    


 



         