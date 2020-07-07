import datetime
import random
'''
Функция и переменное количество параметров.

Позиционные и ключевые параметры. 
'''
def total(str1='Друг', *args, **kwargs):
    print(f'Привет, {str1}!')
    if len(args)>0:
        for arg in args:
            print(f'Вот, что прилетело в позиционных аргументах: {arg}')
    else:
        print('Позиционные аргументы не указаны!')
    for key,value in kwargs.items():
        print(f'Вот, что прилетело в ключевых аргументах: {key}:{value}')
    #print(f'Вот, что прилетело в ключевом параметре: {extra_param}')


def main():
    name=input("Введите имя: ")
    timestamp=datetime.datetime.today()
    rand1=random.randint(0,5)
    rand2=random.randint(0,5)
    total(name,rand1,rand2,year=timestamp.year,month=timestamp.month,extra_param="Oops!")
    total(name,date=str(timestamp.year)+'-'+str(timestamp.month)+'-'+str(timestamp.day))


'''if __name__=='__main()__':
    main()
else:
    print('Hi')'''
main()