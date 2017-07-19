init_str=input('Insert a string')
l = []
'''Алгоритм:
1. делаем список, элементами которого являются строки, состоящие только из больших (маленьких)
букв
2. в списке смотрим на элементы, состоящие из строк в верхнем регистре, длиной больше 3 букв:
если слева от них - элемент списка состоит из букв нижнего регистра длиной больше 2 - это нужный нам элемент
'''
add = ''
i = 0
while init_str[i] in init_str:
    if init_str[i].isupper():
        j = 1
        while init_str[i:i+j].isupper() and i+j <= len(init_str):
            j += 1
        add = init_str[i:i+j-1]
        i = i+j-1
        l.append(add)
        '''print('index:{} and add string: {}'.format(i, add))'''
    elif init_str[i].islower():
        j = 1
        while init_str[i:i+j].islower() and i+j <= len(init_str):
            j += 1
        add = init_str[i:i+j-1]
        i = i+j-1
        l.append(add)
        '''print('index:{} and add string: {}'.format(i, add))'''
    if i == len(init_str):
         break
'''print(l)'''
new_l = []
for i in range(len(l)-1):
    if l[i].isupper() and len(l[i])>=3:
        if l[i-1].islower() and len(l[i-1])>=2 and i-1 >=0:
            new_l.append(l[i][0:-2])
            '''здесь мы убираем ненужные символы в верхнем регистре'''
print(new_l)

            
    
        
    
        
  
        
    
        
