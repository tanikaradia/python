class A:
    a=1

class B(A):
    b=2

class C(B):
    c=3

z=A()
print(z.a)

z=B()
print(z.a,z.b)

z=C()
print(z.a,z.b,z.c)