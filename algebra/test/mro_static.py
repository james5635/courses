class A:
    @classmethod
    def greet(cls):
        print(f"A: {cls}")

class B(A):
    @classmethod
    def greet(cls):
        print(f"B: {cls}")
        super().greet()  # cls is a class, not an instance

class C(B):
    @classmethod
    def greet(cls):
        print(f"C: {cls}")
        super().greet()

C.greet()
