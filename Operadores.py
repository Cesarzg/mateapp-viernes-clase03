#Operaciones con operadores de incremento
a=23
print("a=23--->",a)
a=a+1
print("a=a+1-->",a)
a+=1
print("a+=1-->",a)
a*=2
print("a*=2-->",a)
a/=2
print("a/=2-->",a)
a-=2
print("a--=2--->",a)
a**=2
print("a**=2--->",a)
from decimal import Decimal
a=Decimal('4.2')
b=Decimal('2.1')
c=a+b
print("el valor de c es ", c)
if c == a-b:
    print("Correcto")
elif c == a+b:
    print("incorrecto")

