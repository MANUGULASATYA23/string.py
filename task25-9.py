#by using operator
fname = "satya"
lname = "swamy"
print(fname +" " +lname)
print("fullname:"+fname+" "+lname)

#by using f'string/interpolation
fname = "satya"
lname = "swamy"
fullname = f"{fname} {lname}"
print(fullname)
print(f"fullname:{fname} {lname}")

#by using string join method
fname = "satya"
lname = "swamy"
lst =(fname,lname)
print(" ".join(lst))
print("fname:",fname,lname)

#string split
#split
email = "satya@gmail.com"
print(email.split("@"))

#split line
address: str =""" 2-84
lampakalova,
prathipadu(m)
eastgodavari(d)
"""
print(address.splitlines())

#partition
email = "a@satya@gmail.com"
print(email.partition("@"))

#rpartition
email = "a@satya@gmail.com"
print(email.rpartition("@"))






