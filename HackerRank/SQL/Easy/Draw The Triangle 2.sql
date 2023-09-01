Declare @counter INT 
Set @counter = 1 

while @counter <= 20 
begin
    print replicate(' * ', @counter)
    set @counter = @counter+1
end