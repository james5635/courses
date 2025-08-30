
from typing import Literal


x = 1
# y: str = x
y: str = x
def a(b: int):
    global x
    x = b


print(type(x))
