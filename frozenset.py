#intersection update
a:set={'satya','devi','amma'}
b:set={'devi','amma','daddy'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
a:set={'1'}
b:set={'2'}
print(a.isdisjoint(b))

#difference
a:set={'1','2','3'}
b:set={'2','3','4'}
print(a.difference(b))
print(b.difference(a))
print(b.difference(b))

#symmetric_difference
a:set={'1','2','3'}
b:set={'2','3','4'}
print(a.symmetric_difference(b))

#symmetric_difference_update
a:set={'1','2','3'}
b:set={'2','3','4'}
a.symmetric_difference_update(b)
print(a)
print(b)

#issubset
a:set={'1','2','3'}
b:set={'2','3','4'}
print(a.issubset(b))

a:set={'1'}
b:set={'2','3','4'}
print(a.issubset(b))

a:set={'2'}
b:set={'2','3','4'}
print(a.issubset(b))


#issuperset
#issubset
a:set={'1','2','3'}
b:set={'2','3','4'}
print(a.issuperset(b))

a:set={'1','2','3'}
b:set={'2'}
print(a.issuperset(b))

a:set={'1','2','3'}
b:set={'4'}
print(a.issuperset(b))


#frozen set
fs=frozenset(('a','b','c'))
print(type(fs))
print(fs)

#union
fs1=frozenset(('a','b','c'))
fs2=frozenset(('b','c','d'))
print(fs1.union(fs2))

#intersection
fs1=frozenset(('satya','amma','dady'))
fs2=frozenset(('amma','dady','swamy'))
print(fs1.intersection(fs2))

#isdisjoint
fs1=frozenset(('satya'))
fs2=frozenset(('swamy'))
print(fs1.isdisjoint(fs2))

fs1=frozenset(('1'))
fs2=frozenset(('2'))
print(fs1.isdisjoint(fs2))


#difference
fs1=frozenset(('satya','amma','dady'))
fs2=frozenset(('amma','dady','swamy'))
print(fs1.difference(fs2))
print(fs2.difference(fs1))

#symmetric_difference
fs1=frozenset(('satya','amma','dady'))
fs2=frozenset(('amma','dady','swamy'))
print(fs1.symmetric_difference(fs2))

#issubset
fs1=frozenset(('1'))
fs2=frozenset(('1','2'))
print(fs1.issubset(fs2))

fs1=frozenset(('satya','amma','dady'))
fs2=frozenset(('amma','dady','swamy'))
print(fs1.issubset(fs2))

#issuperset
fs1=frozenset(('5','9','4'))
fs2=frozenset(('4'))
print(fs1.issuperset(fs2))

fs1=frozenset(('satya','amma','dady'))
fs2=frozenset(('amma','dady','swamy'))
print(fs1.issuperset(fs2))

#copy
fs1=frozenset(('satya','amma','dady'))
fs2=frozenset(('amma','dady','swamy'))
fs3=fs1.copy()
print(fs3)



























"""#dictionary data type
#implicit
userdetails={'fname':'v','lname':'s','email':'satya@gmail.com'}
print(type(userdetails))
print(userdetails)

#explicit
userdetails=dict({'fname':'v','lname':'s','email':'satya@gmail.com'})
print(type(userdetails))
print(userdetails)

#datatype/variable annotation
#implicit
userdetails:dict={'fname':'v','lname':'s','email':'satya@gmail.com'}
print(type(userdetails))
print(userdetails)"""












