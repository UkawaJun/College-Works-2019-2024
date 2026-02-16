--注释使用双减号
--[[
多行注释
为了保存一一对应，下面加了两个减号
标识符：少用_+大写，不用@ $ %这种的
--]]

--Beginning
print("First Time Sest");

--变量
a = 101     --nil表示没定义,不存在
print(a)    --默认情况下，变量总为全局的

--数据类型: nil boolean number string userdata function thread table
print(type("Hallo world"))  --string '原始字符串' "字符串"    [[一块字符串]]
print(type(10.4*3))         --number 2 0.2 2e+1 2e-5 7.5e-02
print(type(type))
print(type(true))
print(type(type(a)))
print(type("Hallo world"))
tab1 = {}
print(type(tab1))

--条件语句的简述
if (tab1) then  --对于 false nil 和 没定义变量 都是假
    print("OK1")
end
if (tab1) then
    print("OK2")
else
    print("No2")
end