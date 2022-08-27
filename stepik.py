# a=(4, 8, 15, 16, 23, 42)
# for i in a:
#     print(i)


# a=8
# for i in range(a):
#     for j in range(0,i+1):
#         print('*',end='')
#     print()


# print('Mercury', 'Venus', sep='*', end='!')
# print('Mars', 'Jupiter', sep='**', end='?')

# a=input('1')
# b=input('2')
# c=input('3')
# e=input('4')
# print(b,c,e,sep=a)


# a=input()
# print(f'Привет, {a}!')

# print('Python', end='+')
# print('C#', end='=')
# print('awesome')


# def f(a, b):
#     c=3*(a+b)**3+275*(b**2)-127*a-41
#     return c
#
# a = float(input('1'))
# b = float(input('2'))
# a = f(a, b)


# a=int(input())
# print(f'Следующее за числом {a} число:',a+1)
# print(f'Для числа {a} предыдущее число:',a-1)

# a=int(input())
# b=int(input())
# c=int(input())
# e=int(input())
# q=a+b+c+e
# print(q*3)

# a= int(input('1'))
# b=int(input('1'))
# c= a+b
# d=a-b
# e=a*b
# print(a,'+',b,'=',c)
# print(a,'-',b,'=',d)
# print(a,'*',b,'=',e)



# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

# def vis (year):
#     return year%4==0 and year!=0
# print(vis(int(input('год; '))))

# import math
#
# def square(st):
#     p= 4*st
#     s=st**2
#     d=math.sqrt(2)*2
#
#     return p,s,d
# print(square(int(input('сьрона;'))))



# a1=int(input('число:'))
# d=int(input('число:'))
# n=int(input('число:'))
# an=a1+d*(n-1)
# print(an)


# a=int(input())
# print(a*1,a*2,a*3,a*4,a*5,sep='---')

# a = 82 // 3 ** 2 % 7
# print(a)


# a=int(input('1'))
# print(a//100)


# a=int(input('1'))
# b=int(input('1'))
# print(b//a)
# print(b%a)


# n=int(input('1'))
# if n%2==0:
#     print(n//2)
# if n%2!=0:
#     print((n+2)//2)


# a=int(input())
# print(abs(a//-4))

# a=int(input('1'))
# print(a,'мин - это', a//60, 'час', a%60, 'минут.')

# a=int(input())
# print('Сумма цифр =',a//100+ a//10%10+a%10)
# print('Произведение цифр =',(a//100)*(a//10%10)*(a%10))


# a=int(input('1'))
# print((a//100),(a//10%10),(a%10),sep='')
# print((a//100),(a%10),(a//10%10),sep='')
# print((a//10%10),(a//100),(a%10),sep='')
# print((a//10%10),(a%10),(a//100),sep='')
# print((a%10),(a//100),(a//10%10),sep='')
# print((a%10),(a//10%10),(a//100),sep='')



# a= int(input())
# print('Цифра в позиции тысяч равна', a//1000)
# print('Цифра в позиции сотен равна', a//100%10 )
# print('Цифра в позиции десятков равна', a//10%10 )
# print('Цифра в позиции единиц равна',a%10 )



# a=int(input())
# if a<=13:
#     print('детство')
# elif a>=14 and a<=24:
#     print('молодость')
# elif a>24 and a<=59:
#     print('зрелость')
# else:
#     print('старость')

# a=int(input('8'))
# b=int(input('8'))
# c=int(input('8'))
# summ=0
# for i in a,b,c:
#     if i>0:
#         summ+=i
# print(summ)


# a=int(input())
# if a in range(-29,-2) and (8,25):
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# k= int(input())
# n= int(input())
# if n<k:
#     print('NO')
# elif n>k:
#     print('YES')
# else:
#     print("Don't know")


# a=int(input('1'))
# b=int(input('1'))
# c=int(input('1'))
# if a!=b and b!=c and c!=a :
#     print('Разносторонний')
# elif a==b and a==c and b==c:
#     print('Равносторонний')
# else:
#     print('Равнобедренный')



# a=int(input('1'))
# b=int(input('1'))
# c=int(input('1'))
# if c<a<b or b<a<c:
#     print(a)
# elif a<b<c or c<b<a:
#     print(b)
# elif a<c<b or b<c<a:
#     print(c)


# a=int(input())
#
# if a==1 or a==3or a==5or a==7or a==8or a==10or a==12:
#     print(31)
# if  a==2:
#     print(28)
# if a==4 or a==6 or a==9 or a==11:
#     print(30)



# a=int(input())
# if a<60:
#     print('Легкий вес')
# elif a<64:
#     print('Первый полусредний вес')
# else:
#     print('Полусредний вес')



# a=int(input('1'))
# b=int(input('1'))
# c=input('2')
# if c=='+':
#     print(a+b)
# elif c=='-':
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=='/':
#     if b==0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a/b)
# else:
#     print('Неверная операция')

# a=input('1')
# b=input('1')
# if a==b:
#     print(a)
# elif a=='красный' and b=='синий':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый':
#     print('оранжевый')
# elif a== 'синий ' and b==' желтый':
#     print('зеленый')
#
# else:
#     print('ошибка цвета')


# a=int(input('1'))
#
# if a >36 or a<0:
#     print('ошибка ввода')
#
# elif 1<=a<=10 and a%2==0:
#     print('черный')
# elif 1<=a<=10 and a%2!=0:
#     print('красный')
# elif 11<=a<=18 and a%2==0:
#     print('красный')
# elif 11 <= a <= 18 and a % 2 != 0:
#     print('черный')
# elif 19<=a<=28 and a%2==0:
#     print('черный')
# elif 19 <= a <= 28 and a % 2 != 0:
#     print('красный')
# elif 29<=a<=36 and a%2==0:
#     print('красный')
# elif 29 <= a <= 36 and a % 2 != 0:
#     print('черный')



# a1=int(input('1'))
# b1=int(input('1'))
# a2=int(input('1'))
# b2=int(input('1'))
# if b1<a2 or b2<a1:
#     print('пустое множество')
# elif b1==a2:
#     print(b1)
# elif a1==b2:
#     print(a1)
# elif a1<=a2<b1<b2:
#     print(a2,b1)
# elif a2<=a1<b2<b1:
#     print(a1,b2)
# elif a1<a2<b2<=b1:
#     print(a2,b2)
# elif a2<a1<b1<=b2:
#     print(a1,b1)
# elif a1==a2 and b1==b2:
#     print(a1,b1)



# a=int(input('1'))
# if a%100==0:
#     print('YES')
# else:
#     print('NO')


# a=int(input('1'))
# b=input('2')
# if 10<=a<=15 and b=='f':
#     print('YES')
# else:
#     print('NO')




# a=int(input('1'))
# if a==1:
#     print('I')
# elif a==2:
#     print('II')
# elif a==3:
#     print('III')
# elif a==4:
#     print('IV')
# elif a==5:
#     print('V')
# elif a==6:
#     print('VI')
# elif a==7:
#     print('VII')
# elif a==8:
#     print('VIII')
# elif a==9:
#     print('IX')
# elif a==10:
#     print('X')
# else:
#     print('ошибка')


# a=int(input('1'))
# if a%2!=0:
#     print('YES')
# elif 2<=a<=5 and a%2==0:
#     print('NO')
# elif 6<=a<=20 and a%2==0:
#     print('YES')
# elif a>20 and a%2==0:
#     print('NO')


# a1=int(input())
# b1=int(input())
# a2=int(input())
# b2=int(input())
# if abs(a1-a2)==abs(b1-b2) or (a1==a2 and b1!=b2)\
#         or (a1!=a2 and b1==b2):
#     print('YES')
# else:
#     print('NO')


# x1=int(input())
# x2=int(input())
# y1=int(input())
# y2=int(input())
# if (x2 != x1 and y2 != y1) and ((x2 - x1) == (y2 - y1) or (x2 - x1)*(-1) == (y2 - y1) or (x2 - x1) == (y2 - y1)*(-1)):
#     print('YES')
# else:
#     print('NO')


# a=float(input())
# if a!=0:
#     print(a**-1)
# elif a == 0:
#     print('Обратного числа не существует')


# a=float(input('1'))
# c=(5/9)*(a-32)
# print(c)

# a=float(input('1'))
# if a <= 2:
#     print(a*10.5)
# elif a>2:
#     print(21+(a-2)*4)

# a=float(input())
# b=a%1
# c=b%10
#
# print(c)


# a=float(input())
# b=float(input())
# c=float(input())
# d=float(input())
# e=float(input())
# print('Наименьшее число',min(a,b,c,d,e))
# print('Наибольшее число',max(a,b,c,d,e))


# a=int(input('1'))
# b=int(input('1'))
# c=int(input('1'))
# e=[]
# e.append(a)
# e.append(b)
# e.append(c)
# e.sort(reverse=True)
# for i in e:
#     print(i)


# a=int(input('1'))
# b=int(input('1'))
# c=int(input('1'))
# e=max(a,b,c)-min(a,b,c)
# print(max(a,b,c))
# print(e)
# print(min(a,b,c))

# a=int(input())
# b=a//100
# c=a//10%10
# d=a%10
# if max(b,c,d)-min(b,c,d)==(b+c+d)-max(b,c,d)-min(b,c,d):
#     print('Число интересное')
# else:
#     print('Число неинтересное')


# a=float(input())
# b=float(input())
# c=float(input())
# d=float(input())
# e=float(input())
# print(abs(a)+abs(b)+abs(c)+abs(d)+abs(e))


p1=int(input())
p2=int(input())
q1=int(input())
q2=int(input())

print(abs(p1-q1)+abs(p2-q2))