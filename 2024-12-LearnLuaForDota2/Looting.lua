-- Looping Code Block

local a = 0
while a < 20 do
    print("a",a)
    a = a + 1
end

for i=0,6,1 do 
    print(i)
end

local tbl_data = {name = "Luohan",
                money = 9999999,
                Level = 100,
                HealthP = 100}

for k,v in pairs(tbl_data) do
    print(k..':',v)
end


-- do  while
i = 0
repeat
    print("repeat"..i)
    i = i+1
until i >= 15