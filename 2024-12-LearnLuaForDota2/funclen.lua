
-- standard function
function add(a,b)
    print(a+b)
end

add(5,10)

-- unnamed function
function tabPrint(table,func)
    for k,v in pairs(table) do
        func(k,v)
    end
end
tab1 = {red = 10,blue = 20}
tabPrint(tab1,function (a,b)
    print(a..":",b)
end)

--function return value
function distanceFunc(a,b)
    if a>b then
        return a-b
    else
        return b-a
    end
end
c = distanceFunc(5,10)
print(c)

--运算符
print("----------calculate Language----------")


--算术运算符 
--[[
    + - * / % 10^2 == 100 
--]]

--关系运算符
--[[
    == ~= > < >= <=
--]]

--逻辑运算符
--[[
    and or not
--]]

--连接运算符.. 求长运算符 #
--伪随机 
function random(seed,a,b)
    y = 56135*math.sin(562641*(seed+0.145) + (0.632+seed)*seed) + 56135
    clamp = 0.5*(y/56135)
    return((b-a)*clamp + a)
end
list0 = {0,1,2,3,4,5,6,7,8,9}
tab2 = {}
for k,v in pairs(list0) do
    y = random(v,10,20)
    tab2[k] = y
end

for k,v in pairs(tab2) do
    print(k..":",v)
end
