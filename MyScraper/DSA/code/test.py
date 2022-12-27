given1 = [1,2,3,4,100]

given = [1,1,5,5,10,8,7]
given.sort()
print(given)
new_l = given[1:-1]


sum = 0
for i in new_l:
    sum = sum + i
avg = sum/len(new_l)
print(int(avg))
