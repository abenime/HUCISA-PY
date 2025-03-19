x=int(input("NO : "))
list=[1,1]

for y in range(x):
     num=list[-1] + list[-2]
     list.append(num)
print(list[:-2])

