class A: pass

class B(A): pass

class C(A): pass

class D(B, C): pass

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)
# OR
# print(D.mro())
