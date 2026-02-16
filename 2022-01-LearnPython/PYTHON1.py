name = [1,'ssd',1.0]
print("\n\n+++++++++++++++++++++++++")

magicians = ['alica', 'david', 'lirolina','hi my classmate'] 
for magician in magicians:      # ":"不可以被遗忘
    print(magician.title().upper().lower().title()) #.title()对象是字符串大写,大写后全部大写再小写再大写
    #magician.replace('a','OoOoO',2)
    print(magician.find("li"))  #.find表示寻找该片段 并返回第一个索引：搜索从索引1到索引5(不包括)的子字符串,
    print(magician.rfind("li")) # 返回最后一个索引
    print(len(magicians))
    print(magician + ".....\n")

#for vava in range(len(magicians)): # 0 1 2 3
#    print(magicians[vava].upper())

for var in range(5 , len(magicians)+5): # 0 -- 5
    print(var)


step = 3
numlist0 = list(range(1,14,step))
print(numlist0)
#name = input() 函数吸收字符串进入声明的name里
print("------------------------------------")

squares = [] 
for value in range(1,11): 
    square = value**2 
    squares.append(square)  #在末尾加入 square
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares1 = [value**2 for value in range(1,12)] #列表解析模式
print(squares1)


print("更多字符串的处理手段")
#定向尺寸的切片
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[-3:1])  #返回一种切片  or [:3]{0-3个  ||   [3:] {3-end
print(players)
#players[-4:-1]  #负号索引表示距离末尾为a的元素
print(players[-2:4])    #example
#
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:") 
for player in players[:3]: 
   print(player.title())
#证明直接列表赋值实际上是赋值地址
players2 = players
players.append('sss')
print(players2)
print("\n--------\n")
#列表复制
players2 = players[:]
players.append('yyy')
print(players2)
print(players)      #说明切片是一种返回性，而名字代表地址
print("\n--------\n")
#元组 :元素不可修改，但可以为元组的标签yupl赋值同类型的不同元组和切片,定义用圆括号，访问同列表
yupl = (11,"ss","ss")

yupl2 = yupl[:]
strcin = "my name is jolene 3"
arr2 = strcin.split(" ") #切切
print(arr2)
#question 运用split创建全大写列表
# if 逻辑语句
copes = ["a","bb","ccc","dddd","eeeee"]
print(copes.index("ccc"))
for cope in copes:
    if cope.lower() == "dddd" and 2 == 2:
        print(cope)
    else:
        print(cope.upper())

banned_users = ['andrew', 'carolina', 'david'] 
user = 'andrew' 
if user  in banned_users:    # test
   print(user.title() + "in the list")
user = 'and0rew' 
if user not in banned_users:    # test
   print(user.title() + ", you can post a response if you wish.")

#BOOL
track = True
track = not(3 > 5 and 6 > 12)
if bool(1):
    print(" ")
if track:
    print("Fuck it`s doom!")

age = 12 
if age < 4: 
    price = 0
elif age < 18: 
    price = 5 
elif age < 65: 
    price = 10 
else: 
    price = 5 
print("Your admission cost is $" + str(price) + ".")

nun = 10
print(nun)
