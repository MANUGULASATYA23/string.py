#string datatype:implicit
name="satya"
print(type(name))

#explicit
a=str(10)
print(type(a))

#variable anotation
name:str="satya"
print(type(name))

#boolean datatype:implicit
bln=True
print(type(bln))

#explicit
bln=bool(True)
print(type(bln))

#varaiable anotation
bln:bool=False
print(type(bln))

#binary system examples
#implicit
a=0b1010
print(a)
print(type(a))

#explicit
a=bin(0b1010)
print(a)
print(type(a))

#datatype annotation
a:bin=0b1010
print(a)
print(type(a))


#explicit
a=bin(10)
print(a)

a=bin(False)
print(a)

a=bin(True)
print(a)


#octal number system
#implicit
a=0O1234
print((8*8*8*1)+(8*8*2)+(8*3)+(1*4))
print(a)
print(type(a))

#explicit
a=oct(0o1234)
print(a)
print(type(a))

#datatype
a:oct=0o1234
print(a)
print(type(a))

a=oct(0b1010)
print(a)

a=oct(True)
print(a)

#hexadecimal
#implicit
a= 0xFace
print(a)
print(type(a))

#explicit
a= hex(0x12ab)
print(a)
print(type(a))

#datatype annotation
a:hex=0x1234
print(a)
print(type(a))


#implicit
name="satya"
print(type(name))

#explicit
name=str(10)
print(type(name))

#datatype annotation
name:str="satya"
print(type(name))

#integer
#implicit
num = 10
print(num)
print(type(num))

#explicit
num = int(10.10)
print(num)
print(type(num))

#datatype annotation
num: int = 10
print(num)
print(type(num))

#float
#implicit
num = 10.23
print(num)
print(type(num))

#explicit
num = float (10.3012)
print(num)
print(type(num))

#datatype annotation
num: float = 10.72
print(num)
print(type(num))

#exponential
num = float (16326733388888888888888888888888888888888888888675)
print(num)
print(type(num))

num = 6.2e2
print(num)

#complex number
#impicit
a = 1 + 2j
b = 3 + 4j
print(a+b)
print(type(a+b))
print(a.real)
print(a.imag)

#explicit
a = complex(1)
print(a)

#datatype annotation
a: complex = 1
print(a)

#explicit
#integer-binary
a = bin(10)
print(a)
print(type(a))

#octal-binary
a=oct(0b1001)
print(a)
print(type(a))

#integer-octal
a=oct(10)
print(a)
print(type(a))

#binary-octal
a=bin(0o1234)
print(a)
print(type(a))

#hexa-binary
a=bin(0x12547)
print(a)
print(type(a))

#binary-integer
a=int(0b1001110)
print(a)
print(type(a))

#octal-integer
a=int(0o163467677)
print(a)
print(type(a))

#hexadecimal-integer
a=hex(0x546deff)
print(a)
print(type(a))

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

#int-str
a= str(6743)
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

#boolean type coversation
#str-bool
a=bool("deba")
print(a)
print(type(a))

#bin-bool
a=bool(0b01010)
print(a)
print(type(a))

#hex-bool
a=bool(0x034ad)
print(a)
print(type(a))

#oct-bool
a=bool(0o2456)
print(a)
print(type(a))

#int-bool
a=bool(3874)
print(a)
print(type(a))

#string datatype
#implicit
name = "satya"
print(type(name))


#float-bool
a=bool(0.0)
print(a)
print(type(a))

#expotential-bool
a = bool(0.0e0)
print(a)
print(type(a))

#complex-bool
a = 0 +1j
b = 0j
print(a+b)
print(type(a+b))
print(a.real)
print(a.imag)


















