from math import sin, cos


def tg(i: float) -> float:
    return sin(i) / cos(i)


def inp(msg, alwd):
    while True:
        t = input(msg)
        if isinstance(alwd, type) and all(map(lambda el: el.isdigit(), t.split("."))):
            return float(t)
        if t in alwd:
            return t


def e(i):
    print(i)
    exit(0)


funcs = "* + - / exp root sin cos tg ctg"
f = inp(funcs + "  -> ", funcs.split())
a = inp("a = ", float)
if f not in "sin cos tg ctg".split():
    b = inp("b = ", float)

if f == "*":
    e(a * b)
if f == "+":
    e(a + b)
if f == "-":
    e(a - b)
if f == "/":
    e(a / b)
if f == "exp":
    e(a**b)
if f == "root":
    e(a ** (1 / b))
if f == "sin":
    e(sin(a))
if f == "cos":
    e(cos(a))
if f == "tg":
    e(tg(a))
if f == "ctg":
    e(1 / tg(a))
