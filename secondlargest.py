# DAY - 2
# find the second largest number in a list 
""" PC 1 """ 
# max = list[0]
# for index in ranage(len(list))
# if max < index[index-1]
# max = list[index]


listnum1 = [2,4,1,5,6]
# listnum = [1,2,4,0,22,3,10]
""" using alg unordered """
s = max(listnum1)
listnum1.remove(s)
r = max(listnum1)
print(f"\n1. Unordered list. \nlist = {listnum1} \nsecond max num = {r}")

""" ordered """
olist = [1,2,3,4,5,6]
print(f"\n\n2. Unordered list. \nlist = {olist} \nsecond max num = {olist[-2]}")

""" without alg """
listnum = [1,4,0,22,3,10]
print(f"\n\n3.Without using builtin functions - less optimal approach(not scalable). \nlist = {listnum}")
largest = []
maxim = float("-inf") #listnum[0]
for i in range(len(listnum)):
    if  listnum[i]>maxim:
        maxim = listnum[i]
        largest.append(maxim)

lar = largest[-1]
listnum.remove(lar)

maxim = float("-inf")
for i in range(len(listnum)):
    if  listnum[i]>maxim:
        maxim = listnum[i]
        largest.append(maxim)
print(f"Second largest - {largest[-1]}")
# print(largest)

""" PC 2 """
list_of_num = [1,8,2,3,6,5,3]
print(f"\n\n4.Without using builtin functions. decent scalability and slightly more optimized \nlist = {list_of_num}")

max1 = float("-inf")
max2 = float("-inf")

if len(list_of_num) < 2:
    print ("Stopping")
else:
    for num in list_of_num:
        print(f"\n  Entered FOR loop element = {num}")
        if num > max1:
            print(f"    inside IF condition where current element {num} > max element{max1}")
            max2 = max1
            max1 = num
            print(f"      Numbers status => max1 = {max1} , max2 = {max2}")
        elif max1 > num > max2:
            print(f"    Entered ELSEIF {max1} > {num} > {max2}")
            max2 = num
            print(f"      current second largest = {max2}")
    print(f"End of FOR loop")
    print(f"Second largest number = {max2}")
