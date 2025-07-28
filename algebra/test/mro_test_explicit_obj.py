class A:
    def greet(self):
        print(f"A: {self}")

class B(A):
    def greet(self):
        print(f"B: {self}")
        super(B, self).greet()  # Start after B in MRO of self

class C(A):
    def greet(self):
        print(f"C: {self}")
        super(C, self).greet()  # Start after C in MRO of self

class D(B, C):  # MRO: D → B → C → A
    def greet(self):
        print(f"D: {self}")
        super(D, self).greet()  # Start after D in MRO of self

d = D()
d.greet()
