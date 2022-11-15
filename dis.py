a=input('Значение a: ')
b=input('Значение b: ')
c=input('Значение c: ')
a=float(a)
b=float(b)
c=float(c)
dis=b**2 - 4*a*c
if dis<0:
    print('Корней нет')
elif dis==0:
    x = -b/(2*a)
    print('x= ' + str(x))
else:
    x1 = (-b + dis**0.5)/(2*a)
    x2 = (-b - dis ** 0.5) / (2 * a)
    print('x1='+str(x1))
    print('x2=' + str(x2))
