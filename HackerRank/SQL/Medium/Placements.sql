with union_data(person_id, person_name, person_salary, friend_id, friend_salary)as (
select 
    s.id as person_id,
    s.name as person_name,
    p.salary as person_salary,
    f.friend_id as friend_id,
    pk.salary as friend_salary
from students as s
inner join packages as p on s.id=p.id
inner join friends as f on s.id=f.id
inner join packages as pk on f.friend_id=pk.id)

select person_name from union_data
where friend_salary>person_salary
order by friend_salary;