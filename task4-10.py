#even number
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("given number is even.")
else:
   print("given number is not.")

#prime number
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

#palindrome
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")


#armstrong
def is_armstrong_number(number):
	return sum(int(digit)**len(str(number)) for digit in str(number)) == number
num = 153
if is_armstrong_number(num):
	print(f"{num} is an Armstrong number")
else:
	print(f"{num} is not an Armstrong number")


#arthematic operation
#addition
a = input("enter a value: ")
b = input("enter b value: ")
print(int(a) + int(b))

#substation
a = input("enter a value: ")
b = input("enter b value: ")
print(int(a) - int(b))

#multiflication
a = input("enter a value: ")
b = input("enter b value: ")
print(int(a) * int(b))

#division
a = input("enter a value: ")
b = input("enter b value: ")
print(int(a) /int(b))

#modulus
a = input("enter a value: ")
b = input("enter b value: ")
print(int(a) % int(b))

#floor division
a = input("enter a value: ")
b = input("enter b value: ")
print(int(a) // int(b))


