def check_fresh(fresh_list, good):
    for x in fresh_list:
        if good>=x[0] and good<=x[1]:
            return 1

    return 0

with open('day5_prob1.txt', 'r') as f:
#with open('day5_sample.txt', 'r') as f:
    inventory = [x.splitlines() for x in f.read().split("\n\n")]

fresh_list = [[int(y) for y in x.split('-')] for x in inventory[0]]
goods = [int(x) for x in inventory[1]]

#print(fresh_list)
#print(goods)

nfresh = 0
for good in goods:
    nfresh = nfresh + check_fresh(fresh_list, good)
    
print()
print()
print(str(nfresh) + " fresh goods")
