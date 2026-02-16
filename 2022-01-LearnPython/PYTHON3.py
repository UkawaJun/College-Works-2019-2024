#1 input
message = input(("let`s input something ok?\n").title())
print(message.title() + " too!!!!")

#2 用字符变量作为input参数
message2 = " The python is a easy language"
message2 +="      \n do you agree with me?"
new_str = input(message2)
print(new_str + "That is ok!")

#3 int()转化输入的str类型转化为int  ：当需求为获取用户输入的数字时
#input获取的任意内容均为str
new_str = input("please input some numbers")
num0 = int(new_str)         #如果不转化，与60比较时会是str与int类型的比较，将会报错
bool1 = num0 > 60
print(bool1)

#4求模运算符  :表示整除并返回余数 如判断函数奇偶即 mol 2
num1 = num0 % 5
print(str(num0) + " mol 5 is :" + str(num1))
    

