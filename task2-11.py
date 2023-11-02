#abstraction with function
class employee:
    __fname:str="satya"
    __lname:str="swamy"
    def fullname(self):
        return self.__nameformat(self.__fname,self.__lname)
    def __nameformat(self,fname:str,lname:str):
        return f"{fname}{lname}"

emp=employee()
emp.__fname="ABC"
print(emp.fullname())
print(emp.__nameformat('satya','swamy'))


#single inheritance
class address:
    __address:str=""
    def addaddress(self,address):
        self.__address=address
    def getaddress(self):
        return self.__address
class employee(address):
    __fname:str=""
    __lname:str=""
    __sname:str=""
    def setname(self,f1name:str,l1name:str,s1name:str=""):
        self.__fname = f1name
        self.__lname = l1name
        self.__sname = s1name
    def __nameformat(self):
        return f'{self.__fname}{self.__lname}{self.__sname}'
    def getfullname(self):
        return self.__nameformat()
emp=employee()
emp.setname(l1name="swamy",s1name="#",f1name="satya")
emp.addaddress("hyd")
print(emp.getfullname())
print(emp.getaddress())



