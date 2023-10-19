#set data type
#implicit
a={'a','b','c'}
print(a)
print(type(a))
#explicit
a=set(('a','b','c'))
print(a)
print(type(a))
#datatype/variable annotation
a=set(('a','b','c'))
print(a)
print(type(a))

#create
#add
a:set={'a','b','c'}
a.add('d')
print(a)

#update
a:set={'a','b','c','d'}
b:set={'c','d','e','f'}
a.update(b)
print(a)

#remove
a:set={'a','b','c','d'}
a.remove('b')
print(a)

#discard
a:set={'a','b','c','d'}
a.discard('c')
print(a)

#pop
a:set={'a','b','c','d'}
a.pop()
print(a)

#some methods of set
#union
a:set={'a','b','c','d'}
b:set={'c','d','e','f'}
print(a.union(b))

#intersection
a:set={'a','b','c','d'}
b:set={'c','d','e','f'}
print(a.intersection(b))







