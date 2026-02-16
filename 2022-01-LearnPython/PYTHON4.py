#while循环
current_number = 1 
while current_number <= 5: 
    print(current_number) 
    current_number += 1

#2使用while 模仿 for循环
num_i = 0                       #int i
new_bool1 = num_i < 6           #执行条件判断
while new_bool1: 

    print(num_i)                #循环体内部的代码块：当前为一句显示本代码块内num_i大小的指令

    num_i += 1                  #执行尾部对 i 进行次数的递增
    new_bool1 = num_i < 6       #执行条件判断

#3无限循环 并使用输入判断跳出--break
while True:
    message = input("lets input some thing")
    if message == "break":              
        print("input is " + message)
        break;
    print("your input is " + message)       #一个隐匿的else条件


#4 continue and break;
    #break 会直接结束整个循环并继续执行循环之后的代码
    #continue 则是跳过本次循环 回到while的条件判断处
current_number = 0 
while current_number < 10: 
    current_number += 1 
    if current_number % 2 == 0: 
        continue 
 
    print(current_number)

#5 无限循环的标志(bool)写法
bool2 = True
while bool2:
    message = input("lets input some thing")
    if message == "break":              
        bool2 = False
    else:
        print("your input is " + message)       
#6删除列表中特点元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets) 
while 'cat' in pets: 
    pets.remove('cat') #删除第一个找到的cat
 
print(pets)






#################

#函数的书写
#1关键字实参     在使用函数时指定性的传递 实参值
def func1(type1,type2):
    print(type1.title())
    print(str(type2) + "too")
        #下面的三种形式的结果相同
func1(type1 = 'bb',type2 = 'aa')
func1(type2 = 'aa',type1 = 'bb')
func1('bb','aa')
#2参数默认值     当函数的参数可以选择性不提供数值，则使用设定的默认值      #让函数的参数选择变成可选的
def func2(type1,type2 = 'none',type3 = 'none'):
    print(type1)
    print(str(type2) + "too")
        #一个形参设置了默认值，它后面的形参也都必须设置默认值
func2('bb')         
func2('aa','bb')
#3函数返回值
name = 100

def get_formatted_name(first_name, last_name): 
    full_name = first_name + ' ' + last_name + str(name) 
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)
#4函数对列表进行修改

list2 = [1,2,3]
def func3(list):
    list.append(4)
func3(list2)
print(list2)

tie = 100
def func31(list1):
    list1 = 10

func31(tie)
print(tie)      #100
#5  传入任意数量的参数 放入一个元组里
def make_pizza(*toppings): 
    list2 = list(toppings[:])      #把整个元组切片放到列表
    print(list2) 
 
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#结合任意实参和位置实参
def made(size,*toppings):   
    print("\nMaking a " + str(size) + 
    "-inch pizza with the following toppings:") 
    for topping in toppings: 
        print("- " + topping) 
 
made(16, 'pepperoni') 
made(12, 'mushrooms', 'green peppers', 'extra cheese')
#字典的实参 关键字实参

def build_profile(first, last, **user_info): 
    profile = {} 
    profile['first_name'] = first 
    profile['last_name'] = last 
    for key, value in user_info.items(): 
        profile[key] = value 
    return profile 
user_profile = build_profile('albert', 'einstein', location ='princeton',key = 'value',key2 = 'value2')
 
#6 函数模块化
import wall
wall.wall(3)       #module_name.function_name()


from wall import wall2   #从wall模块里导入wall2函数
wall2()

#7 as指令使得导入的内容有别名 
from wall import wall3 as valent
    #导入了wall3函数 但使用方法是用as后的名称而不是原名

import wall as wa
wa.wall3        #对导入的模块进行别名化

#8导入模块时的全部导入
from wall import *
#使用时则直接使用函数名 

    #直接import模块在使用内部函数时必须要module_name.function_name()，而from导入则直接使用函数名或者别名






























