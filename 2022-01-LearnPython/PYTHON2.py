

from os import system


#补充 ：
#右键右侧解决方案资源管理器内.py文件 可以直接设置启动文件
#str()表示强制转换，出现在print内的非str型号在加法时应进行运算
list0 = [] # Empty List 
if list0:
    print(list0)
else:       #0
    print(" The List is empty")
###---------------------------###    

#客户点餐代码
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] 
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] 
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings: 
        print("Adding " + requested_topping + ".") 
    else: 
        print("Sorry, we don't have " + requested_topping + ".")


sTitle = "the new page of dictonary-- for xue"
system("title " + sTitle.title())

        # {Dictonary}
alien_0 = {'color': 'green'  ,  'points': 5} 
print(alien_0) 
alien_0['x_position'] = 0   # 键 - 值 对 此处表示添加 ————
alien_0['y_position'] = 25 
print(alien_0)
alien_empty = {}        #empty dictonary
cy = [alien_empty,alien_0,{'color':'pin back','sss':3}]  # create dictonary list

alien_0['color'] = 'orange'     #Change
cy[2]['new num'] = 'new'

print(alien_0)
print("\n对比：")
print(cy)
del cy[2]['new num']    #删除对应的键（书签）
print(cy)
#以下为标准书写，用途是为了更加直观
fs = {         #多行字典写法  左括号在上，右括号在下 每行末尾为","
 'jen': 'python', 
 'sarah':    'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 }                   #字典的书签（键）对应一种类型
ts = ['phil', 'sarah']
print("Sarah's favorite language is " + 
    fs['sarah'].title() + 
    ".")         #多行print是比较自由的：缩进方面，和括号方面，但这个更规格一点

for key1,var in fs.items():         #for 遍历
    print("\nkey name is:" +key1)
    print("and various is:" +var)       #灵感：python数组拼装int即c++函数递归指针的并转
for key1 in fs.keys():        # fs.values() 表示键对应的值  fs.keys 表示键
    print(" :"+ key1)
    if key1 in ts:
        print("This key is enable")
    else:
        print("     This key is disable")
#fs.clear()

print("\n------------------\n")

favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 

for name in sorted(favorite_languages.keys()):  #表示在被name获取前，对字典的keys进行排序再遍历
 print(name.title() + ", thank you for taking the poll.")

favorite_languages = sorted(favorite_languages) #为字典排序
print(favorite_languages)

lista = [1,2,2,3]
for box in set(lista): #表示删除目标元素堆里重复的部分         box in [1,2,3]
    print(box)

"""
favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 
print("The following languages have been mentioned:") 
for language in set(favorite_languages.values()): 
    print(language.title())
"""
#以下为几种程序: 字典列表 ; 列表列表
list30 = []
list6 = ["green","blue","red","blue","blue","green"]
list62 = ["5$","3$","7$","3$","3$","5$"]
for var in range(0,6):
    dic = {'color' : list6[var]}
    list30.append(dic)
print(list30)
print("-------列表列表-----")

dict0 = {}
for var in range(0,6):
    dict0[str(var) + '编号'] = {list6[var]:list62[var]}
print(dict0)

#list
listend = ["ss","ppp","ccc"]
listend[1] = 'ppd'          #对原列表实质性的内容修改
listend.append("aaaa")
listend = sorted(listend)[1:]   #强调排序的本质是返回一个list类型，所以可以切片操作
print(listend)
print("---------114")
listend.insert(0,{'1':'2'}) #插入内容于 0 索引处(可以理解为0处及它后面的元素均向右移动腾出位置)
del listend[0]              #删除索引位的元素
print(listend)
pop_item = listend.pop()    #pop!弹出末尾的元素，赋值给新的目标，并删除最初的元素
print(pop_item)
print(listend)              #pop以及在末尾元素传递后被删除
listend.pop(1)              #执行弹出操作在该索引处 像这样不赋值，导致数值丢失
print(listend)
listend.remove("ccc")       #删除找到的“ccc”种的第一个元素        #此时代码中listend是一个空list
#概念化 remove 删除检索目标群间的第一个元素

print("\n排序:\n")

list2 = ['b','e','f','t','i','p','a']
list3 = list2[:]
print(list2)
list2.sort()    #改变原数据：按字母排序，且不返回数据
print(list2)

print(sorted(list3))    #sorted函数表示一种临时排序，不改变原数据，返回排序好的list
print(list3)
list2.reverse()         #表示倒序排序原数据
print(len(list2))       #len()的参数是一种表:列表，元表或者字典，返回元素的int数量

#str
str0  = " a b c"
str0.replace('a','A')   #替换a 变成 A
print(str0)