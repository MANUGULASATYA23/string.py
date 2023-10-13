#string slicing
name="satya"
print(name[0:3])

#start ana end is optional
print(name[:])
print(name[0:])
print(name[:4])

#negative
print(name[-5:-1])
print(name[-5:])
print(name[:-1])

#list data type
#implicit:
attendees =["satya","devi","amma"]
print(type(attendees))
#explicit
attendees =list(("satya","devi","amma"))
print(type(attendees))
#datatype/variable annotation
attendees:list=list(("satya","devi","amma"))
print(type(attendees))
attendees:list=["satya","devi","amma"]
print(type(attendees))

#accesssing list item
attendees:list=["satya","devi","amma"]
print(attendees[0])
print(attendees[-1])

#list slicing
attendees:list=["satya","devi","amma"]
print(attendees[0])
print(attendees[-1])
print(attendees[:])
print(attendees[0:2])
print(attendees[-2:-1])
print(attendees[-2:])

#reverse a string
name="satya"
print(name[::-1])

#reverse a string without slicing
a="satya"
b=""
for i in a:
    b=i+b
print(b)


#reverse of a list item
attendees:list=["satya","devi","amma"]
print(attendees[::-1])








