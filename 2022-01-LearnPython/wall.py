def wall(int):  #实参 带入 形参
    print("----------------------" + str(int) +  "----------------------")

def wall2(int):  #实参 带入 形参
    print("----------------------" + str(int) +  "----------------------")

def walls(str):
    print("----------------------" + str +  "----------------------")

class Dog2():        #名称
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

class Dog3():        #名称
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



