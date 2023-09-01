declare @counter INT
set @counter = 20

while @counter >= 1
begin 
print replicate("* ", @counter)
set @counter = @counter-1
end 