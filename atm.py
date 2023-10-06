accountnumber=input("enter the accountnumber:")
if(accountnumber.isnumeric() and len(accountnumber)==10):
    print("valid accountnumber")
else:
    print("not valid accountnumber")
pin= input("enter the pin:")
if (pin.isnumeric() and len(pin) == 4):
    print("valid pin")
else:
    print("not valid pin")
if (accountnumber==1234567890 , pin==1234):
    print("select 1 to with draw ,2 to balance enquiry")
    option = int(input("choose 1 or 2 :"))
    if (option==1):
         withdraw= int(input("withdraw amount: "))
         if (withdraw > 150000):
            print("Insufficient balance.")
         else:
            option = (150000 - withdraw)
            print("debited sucessfully")
            print("remaining your balance:", option)
    elif(option==2):
        print("total amount= 150000")
    else:
        print("click the valid option")
else:
    print("invalid accountnumber and pin:")
    print("please enter the valid details.")


