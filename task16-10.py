#append
lst=["satya",1,False]
print(lst)

lst:list=[]
lst.append("satya")
print(lst)

#insert
a=["satya","swamy","amma"]
a.insert(1,"dady")
print(a)

#count
a=["satya","swamy","amma"]
print(a.count("satya"))

print(a.count("abc"))

a=["satya","swamy","amma"]
if(a.count("neeraja")>0):
    print(a.inert("neeraja"))

#update
a=["satya","swamy","amma","swamy"]
a[0]="pandu"
print(a)

#extend
a=["satya","devi"]
a1=["naveen","ganesh","swamy"]
a.extend(a1)
print(a)
print(a1)

#delete
a=["satya","swamy","amma"]
a.remove("satya")
print(a)

a=["satya","swamy","amma"]
a.pop(2)
print(a)

a=["satya","swamy","amma","naveen","ganesh","devi","pandu"]
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
print(a)