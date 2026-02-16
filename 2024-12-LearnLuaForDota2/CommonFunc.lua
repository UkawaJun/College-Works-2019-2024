function Tips() for i=0,0,1 do print("----------")end end


--function作为一种数据类型

Line = Tips
Line()

--function的自由插入变量

function addP (...)
    local sums = 0
    for v in ipairs{...} do
        sums = sums + v
    end
    return sums
end

local c = addP(1,2,5,6,4,5,5)
print(c)