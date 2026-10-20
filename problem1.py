def format_date(a :str):#02.05.2025
    a = a.split(".")
    dct = {"01":"yanvar",
           "02":"febral",
           "03":"matr"}

    print(f"{a[0]}-kun {dct[a[1]]} oy  {a[2]} yil ")
    
def get_top_user(d:list[tuple[str,int]])->str:
    a = max(d , key=(lambda x : x[1]))
    l = 1
    # for i,m in d:
    #     for x,a in d[0::]:
    #         if i==x:
    #             d[i]=m+a
    for  i,x in d:
        if i==a[0] or x>a[1]:
            print(i,x)

def ball(a:list)->int:
    b=0
    for i in a:
        if i >=60:
            b+=1
    return b

