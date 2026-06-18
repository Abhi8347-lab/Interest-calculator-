p = float(input('Enter the principal amount:'))
while p <= 0:
    print('Principal amount invalid')
    p = float(input('Enter the principal amount($):'))
r = float(input('Enter the rate of interest:'))
while r <= 0:
    print('rate of interest invalid')
    r = float(input('Enter the rate of interest:'))
t = int(input('Enter the time (in years):'))
while t <= 0:

    print('time is invalid')
    t = int(input('Enter the time (in years):'))
else:
    A = p * pow((1 + r / 100), t)
    Compound_interest = A - p
    r=round(A - p)
    print(f' The compound interest after {t} years is ${Compound_interest}  approximately ${r}')
    A = (p * r * t) / 100
    B=round((p * r * t) / 100)
    print(f'The simple interest after {t} years is ${A} approximately ${B}')
