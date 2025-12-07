def find_max(battery, start, digits, jolts, total):
    v_max = -1
    i_max = -1
    if digits>1:
        scan_battery = battery[start:-digits+1]
    else:
        scan_battery = battery[start:]

    for i,v in enumerate(scan_battery):
        if int(v) > v_max:
            v_max = int(v)
            i_max = start + i
    jolts.append(v_max)
    total = total + v_max*10**(digits-1)
    digits = digits - 1
    if digits:
        jolts, total = find_max(battery, i_max+1, digits, jolts, total)

    return jolts, total


def max_joltage(battery, digits):
    jolts = []
    total_joltage = 0
    jolts, total_joltage = find_max(battery, 0, 12, jolts, total_joltage)

#    print(jolts)
#    print(total_joltage)

    return total_joltage
        
with open('day3_prob1.txt', 'r') as f:
#with open('day3_sample.txt', 'r') as f:
    batteries = f.read().splitlines()

joltage = 0
for battery in batteries:
    joltage = joltage + max_joltage(battery, 12)
    
print()
print()
print(str(joltage) + " output joltage")
