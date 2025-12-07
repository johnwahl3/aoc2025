def turn(dial, code):
    d = int(code[1:]) * (-1 if ("l" in code.lower()) else 1)
    return (dial + d) % 100

dial = 50

with open('realcodes.txt', 'r') as f:
#with open('codes.txt', 'r') as f:
    codes = f.read().splitlines()

nzero = 0
for code in codes:
    dial = turn(dial, code)
    if dial==0:
        nzero = nzero + 1

print()
print()
print(str(nzero) + " zeros")
