from my_class import MyClass, Subclass

myInstance = MyClass("Viraj")
print (myInstance.data)
myInstance.data = "anand"
print(myInstance.data)

print(myInstance.public_member)
myInstance.public_method()

#print(myInstance.__private_member)

obj = Subclass("anand")
obj.access_protected()
obj._protected_method()

print(obj._protected_member)
