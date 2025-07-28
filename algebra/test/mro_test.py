class A:
    def greet(self):
        print(f"A: {self}")

class B(A):
    def greet(self):
        print(f"B: {self}")
        super().greet()

class C(A):
    def greet(self):
        print(f"C: {self}")
        super().greet()

class D(B, C):  # MRO: D → B → C → A
    def greet(self):
        print(f"D: {self}")
        super().greet()

d = D()
d.greet()
