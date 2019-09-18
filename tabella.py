import math
from prettytable import PrettyTable

x = -0.8

def soluzioni(x):
    fx = x**2 + 2*x + 1 - (math.log(-x) )
    der = 2*x + 2 - (1/x)
    diff = - (fx / der)
    va = abs(diff)
    return fx, der, diff, va

a = x;
print("x \t\t f(x) \t\t f'(x) \t\t -f(x)/f'(x) \t |xn- xn-1|")
t = PrettyTable([ 'x', 'f(x)',  "f'(x)", "-f(x)/f'(x)", '|xn- xn-1|'])

for i in range(0,4):
    b, c, d, e = soluzioni(a)
    print(f'{a:1.9f}, \t {b:1.9f}, \t {c:1.9f}, \t {d:1.9f}, \t {e:1.9f} ')
    t.add_row([f'{a:1.9f}', f'{b:1.9f}', f'{c:1.9f}', f'{d:1.9f}', f'{e:1.9f}'])
    a = d + a


f = open("ris.txt" , "w")
f.write(t.get_string());
f.close()

