#Copyright 2013 Rachel Kelly
#fibonaturally

a=1
b=1
c=0
i=1
while i <= 100:
    b = c
    c = b + a
    print("Fibonacci number",i,":",c,)
    a = b
    i=i+1
