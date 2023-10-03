#string datatype

#implicit
name = "satya"
print(name)
print(type(name))

#explicit
name = str("satya")
print(name)
print(type(name))

#datatype annotation
name: str = "satya"
print(name)
print(type(name))

#string type conversion
#integer-string
name = str(10)
print(name)
print(type(name))

#bool-str
a= str(True)
print(a)
print(type(a))

#binary-str
a= str(0b1010)
print(a)
print(type(a))

#octal-str
a= str(0o1234)
print(a)
print(type(a))

#hexa-str
a= str(0xface)
print(a)
print(type(a))

#float-str
a= str(10.21)
print(a)
print(type(a))

#exp-str
a= str(1.2e2)
print(a)
print(type(a))

#complex-str
a = str(1+2j)
print(a)
print(type(a))










