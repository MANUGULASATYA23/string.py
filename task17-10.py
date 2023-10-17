#clear
a=["satya","amma","dady"]
print(a.clear())
print(type(a))
print(a)

#delete
a=["satya","amma","dady"]
del a
print(a)
del a
print(a)

a1=input("enter a1 name:")
a2=input("enter a2 name:")
a3=input("enter a3 name:")
a=[]
a.append(a1)
a.append(a2)
a.append(a3)
print(a)

#sort list
lst=[1,6,4,2]
lst.sort()
print(lst)

#sort a list without sort method
list = ["satya","swamy","salmon"]
for i in range(len(list)):
    for j in range(i + 1, len(list)):

        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

print(list)

#reverse
lst=["g","s","a","y"]
lst.reverse()
print(lst)

#tuple
#implicit
tpl=(1,2,3)
print(tpl)
print(type(tpl))
#explicit
tpl=tuple((1,2,3))
print(tpl)
print(type(tpl))
#implicit
tpl:tuple=(1,2,3)
print(tpl)
print(type(tpl))

#tuple methods
#count
tpl=tuple((1,2,3,1,2))
print(tpl.count(5))
print(tpl.count(2))

#index
tpl=tuple((1,2,3,5,7))
print(tpl.index(1))


tpl=tuple((1,2,3,1))
lst=list(tpl)
print(type(lst))
print(lst)










