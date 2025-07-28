class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        print("B")
        super(B, self).greet()  # Start after B in MRO of self

class C(A):
    def greet(self):
        print("C")
        super(C, self).greet()  # Start after C in MRO of self

class D(B, C):  # MRO: D → B → C → A
    def greet(self):
        print("D")
        super(D, self).greet()  # Start after D in MRO of self

d = D()
d.greet()
