with open('day5_prob1.txt', 'r') as f:
#with open('day5_sample.txt', 'r') as f:
    inventory = [x.splitlines() for x in f.read().split("\n\n")]

fresh_list = [[int(y) for y in x.split('-')] for x in inventory[0]]
goods = [int(x) for x in inventory[1]]

# sort the list by first element
fresh_list_sorted = sorted(fresh_list, key=lambda item: item[0])

print(fresh_list_sorted)

final_list = []
last_x = None
for i, x in enumerate(fresh_list_sorted):
    if i==0:
        last_x = x
        continue
    
    if x[0] <= last_x[1]:
        new_x = x + last_x
        new_x.sort()
        new_x = [new_x[0], new_x[-1]]
        last_x = new_x
    else:
        final_list.append(last_x)
        last_x = x

final_list.append(last_x)

nfresh = sum(map(lambda x: x[1]-x[0]+1, final_list))


print()
print()
print(str(nfresh) + " fresh goods")
