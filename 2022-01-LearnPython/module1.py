#question 用函数递归制作一个n阶字典并打印

def function1(inti):
    dic = {}
    if inti != 0:
        dic['a'] = function1(inti - 1)
    else:
        return {'a':'b'}
    return dic




class class1():
    def __init__(self):
        self.ownname = 10
        self.page  = 'python'
        self.title = 'tide'
        print("")
name0 = class1()
name0.ownname = 1000
print(name0.ownname)
