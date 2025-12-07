def turn(dial, nzero, code):
    dzero = dial == 0
    
    n = int(code[1:])

    nzero = nzero + int(n / 100)
    n = n % 100

    d = n * (-1 if ("l" in code.lower()) else 1)

    dial = dial + d
    
    if (dial < 0 or dial > 100) and not dzero:
        nzero = nzero + 1

    return dial % 100, nzero

dial = 50

#with open('codes.txt', 'r') as f:
with open('realcodes.txt', 'r') as f:
    codes = f.read().splitlines()

nzero = 0
for code in codes:
    dial, nzero = turn(dial, nzero, code)
    if dial==0:
        nzero = nzero + 1

print()
print()
print(str(nzero) + " zeros")
