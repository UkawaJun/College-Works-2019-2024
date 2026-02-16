# 1类 和其实例化的对象
class Dog():        #名称
    def __init__(self, type1 = 'name', type2 = 10):  #初始化其成员变量 及参数列表
        self.name = 'name'                #成员表
        self.age = 10                   #每次创建实例时运行
        self.new01 = 1.0
        self.new02 = type1
#self参数放置在第一位，是一个指向实例本身的引用
    def sit(self): 
        print(self.name.title() + " is now sitting.") 
    def roll_over(self): 
        print(self.name.title() + " rolled over!")
    def change(self):
        self.name = 'fun'
        self.age  =  0
#2实例化
dog0 = Dog('name8',12)
name = 'fun'


manydogs = [Dog('names' + str(value),value) for value in range(1,10)] 
print(manydogs[0].name)  #打印其地址
#3访问其成员
Dog.roll_over()         #用类来访问 成员函数
manydogs[0].name        #用实例化对象访问 成员变量
manydogs[0].sit()       #用实例化对象访问 成员函数、
manydogs[1].name = 'white big dog' #修改对象的成员直接使用点访问

manydogs[2].change()            #第一种并没有实际对象而没有实际的修改

#4继承
class Dog_next(Dog):  #指定父亲的名称
    #Dog_next的初始化函数
    def __init__(self, name, age=10):
        #在其初始化函数内对父类的初始化部分
        super().__init__(name, age)
        self.name = 's'
        self.type0 = Dog('name9',10)
    def func0():    #子类方法
        print("ss")
next_dog = Dog_next('black dog')


from wall import Dog2,Dog3