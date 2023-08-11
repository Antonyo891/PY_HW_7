def rhythm(str):
    list1:list=str.split()
    set1:set=set()
    vowels:list='ё у е ы а о э я и ю'.split()
    for word in list1:
        result=len(list(filter(lambda x:x in vowels,word)))
        if result==0:
            set1.add(0)
        else:
            set1.add(result)
    return len(set1)==1



import os
os.system('cls')
str1:str=input('Введите песенку Винни Пуха ')
if rhythm(str1):
    print('Парам пам пам')
else:
    print('Пам парам')

        
