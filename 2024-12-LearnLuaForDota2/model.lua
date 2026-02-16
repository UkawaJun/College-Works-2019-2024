Tab0 = {}
Tab0.constant = 10
function Tab0.max(a,b)
    if a > b then
        return a
    else
        return b
    end
end
local function double(x)
    return x*x
end

function Tab0.CallDouble(y)
    return double(y)
end

return Tab0