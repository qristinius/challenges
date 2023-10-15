create table Prime_Numbers(numbers INT); 

declare @num_var INT;
declare @divider INT;
declare @prime BIT;

select @num_var = 1 ;

while @num_var <= 1000
    begin 
    select @divider = @num_var - 1;
    select @prime = 1 
    -- checking if it is a prime number
    while @divider > 1
        begin
        if @num_var % @divider = 0 
            select @prime = 0;
        select @divider = @divider - 1
        end
    if @prime = 1 and @num_var != 1
        insert into Prime_Numbers(numbers) values(@num_var)
    select @num_var = @num_var + 1 
    end

select string_agg(numbers,'&') from Prime_Numbers;