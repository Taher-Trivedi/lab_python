#1 basic keyword argument
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest:", si)

simple_interest(p=1000, r=2.5, t=3)