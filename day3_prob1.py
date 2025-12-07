def max_joltage(battery):
    i_max10s = -1
    v_max10s = -1

    for i,v in enumerate(battery[:-1]):
        if int(v) > v_max10s:
            v_max10s = int(v)
            i_max10s = i

    i_max1s = -1
    v_max1s = -1

    for i,v in enumerate(battery[i_max10s+1:]):
        if int(v) > v_max1s:
            v_max1s = int(v)
            i_max1s = i + i_max10s + 1

    print(v_max10s)
    print(i_max10s)
    print(v_max1s)
    print(i_max1s)
    return 10*v_max10s + v_max1s
        
#with open('day3_prob1.txt', 'r') as f:
with open('day3_sample.txt', 'r') as f:
    batteries = f.read().splitlines()

joltage = 0
for battery in batteries:
    joltage = joltage + max_joltage(battery)
    
print()
print()
print(str(joltage) + " output joltage")
