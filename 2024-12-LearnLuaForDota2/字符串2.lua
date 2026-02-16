
Block = [[

Table-Date:
live_games = 56
future_features = 23
game_Players = 5
]]
print(Block)
print('10' + 6,type('10' + 6)) --16
print('10' + '6',type('10' + '6')) --16

--字符串连接
print("connect".."String")
print(156 .. 562,type(156 .. 562))

--获取字符串长度
str0 = 'Time to Lua'
print("Str0 len is:"..#str0)
print('-------------------------Table-------------------------')

--形式1 字典
tbl1 = {}
tbl1["health"] = 10

--形式2 数组
tbl2 = {"health","Bar_Size","Time","Money"}
print(tbl2[1]..tbl2[2])

--键值对构造
tb3 = {red = 10,blue = 2,pink = 5}
print(tb3["red"])       --Ok
print(tb3[0])           --nil 0 is key index,not location

for i,v in pairs(tb3) do
    print(i..":",v)

end

--翻译字符

local tt = [["string all size"]]
print(tt)
local tt2 = "\"ab\""
print(tt2)

--Common Function

--大小写
local toUp = 'aBc'
print(string.upper(toUp))
print(string.lower(toUp))

--替换
local nameList,size = "Alan is AlansCool",0
nameList,size = string.gsub(nameList,"Alan","Jun",2)
print(nameList,size)
print("-----------")

--查找
print(nameList)
--"Jun is JunsCool"
a = string.find(nameList,"Jun",1)
-- 1
a = string.find(nameList,"Jun",2)
-- 8
print(a)

--format
print(string.format("my name is %s,age is %d","Jun",15))