function Tips() for i=0,0,1 do print("----------")end end

--构造传统数组
local list ={}
for i =0,10,1 do
    list[i] = i
end
local lens = #list
for i = 0,lens,1  do
    print(list[i])
end

--构造二维数组

local constSize = 10
list = {}
function Build(list,constSize)
    for i = 1,constSize,1 do
        local list2 = {}
        for j = 1,constSize,1 do
            list2[j] = i*constSize + j
        end
        list[i] = list2
    end
end
Build(list,constSize)

print(list[1][2])
Tips()
--table常用函数
tt = {"a","b","c","d"}
local str = table.concat(tt,",")
print(str)