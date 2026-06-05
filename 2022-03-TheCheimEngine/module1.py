class Person:
	def __init__(a,name):
		a.name = name
	def func():
		print("123")

p1 = Person("jstr")
p1.func()

###
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Bill", 63)
p1.myfunc()    # Hello my name is Bill
###