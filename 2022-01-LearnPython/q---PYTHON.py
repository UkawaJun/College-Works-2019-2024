from wall import wall,walls
#读取文件 读取当前执行的py文件下的目录去查找它

with open('pi_.txt') as obj:        #with在不需要该文件时执行close()
    contents = obj.read()       
    print(contents + "\n")          #str.rstrip() 去除字符末尾的空字符串，换行符

#2对行遍历并操作
wall(2)
with open('pi_.txt') as obj:       
    for lines in obj:                #逐行读取的手段
        print(lines.rstrip())

#3使用变量储存
wall(3)
with open("pi_.txt") as obj:
    lines = obj.readline()         #读取一行的内容
    lines2  = obj.readlines()      #读取每个 一行的内容 
#上面两个方法都把行尾的结束号和空字符读下来了
print("return:     " + lines.rstrip())
print(lines2)
#4读取大型pi并处理
wall(4)
text0 = ""
with open('pi2.txt') as pip:
    for n in pip:
        text0 += n.rstrip()
print("return2:" + text0)
bool4 = " " in text0
list0 = text0.split(" ")
text0 = ""
for n in list0:
    text0 += n.rstrip()
print(text0)
pi = text0
pi_num = len(pi) #1002
#显示多少位的pi
def show_pi(size):
    new_pi = ""
    for inti in range(0,size + 2):
        if (inti == pi_num):
            break
        new_pi += pi[inti]
    return new_pi
print(show_pi(1003))

#show_pi(3)


#5写入内容到文件里
walls("     写入文件    ")
filename = 'fun\ininin.txt'           #当没有指定文件时，系统会自己创建一个
with open(filename, 'a') as file_object:
    for ini in range(0,20):
        file_object.write("I love you.\n".title())
    #open第二个参数指定模式   w写入 ，默认和r为只读模式， a为附加模式  ，r+为可以读写的模式
