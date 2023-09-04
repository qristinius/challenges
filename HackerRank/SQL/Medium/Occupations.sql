/*
first part creates subquery to collect names from certain occupations and the next part divides it into pivot 
for specific occcupation*/
with all_names (name, occupation, rn) as(
select 
    name ,
    occupation,
    row_number() over(partition by occupation order by name) as rn 
from occupations )

select Doctor,Professor, Singer, Actor from all_names
pivot(
    max(name)
for occupation in ([Doctor], [Professor],[Singer],[Actor])) as pivot_table;