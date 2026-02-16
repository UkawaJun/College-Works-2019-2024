def wall(int):  #实参 带入 形参
    print("----------------------" + str(int) +  "----------------------")


#函数之后的数据结构
name2 = {}
def func1(inti1):
    name = {}
    for i in range(0,inti1):
        name[str(i)] = int(i + 1)
    name2 = name                    #创造了新的name2
    return name
name = func1(5)
print(name2)

#赋值号 -- 表达式  在python    ：： 表达式的值对应的类和方法   ：：函数的属性和返回值   ：：值和地址的标签性
#1  
def func1(list1):
    print("copy")
    return list1
list1 = [1,3,5]
func1(list1[:]) 

