declare @consistent_hackers TABLE   --declaring table that will consist consistent hackers who are submitting everyday
(hacker_id int, 
 submission_date date);
 
declare @counted_hackers TABLE   --declaring table that will consist counted consistent hackers from @consistent_hackers table
( counted int,
  submission_date date 
);
 
declare @subdate date;
declare @remaining_date date;

insert into @consistent_hackers                     --inserting data in variable table for the 1st march after that we will use while loop for the next days 
select hacker_id , submission_date from submissions
where submission_date LIKE '2016-03-01';

set @subdate = '2016-03-01';
set @remaining_date = '2016-03-01';

while @subdate < '2016-03-15'     --inserting consistent hackers in table from 2n march to 15 
begin 
    set @subdate = dateadd(day,1,@subdate);  --what am i adding,how many i am adding, which variable am i adding
    
    insert into @consistent_hackers
    select s.hacker_id, s.submission_date from submissions as s
    join @consistent_hackers as ch on ch.hacker_id=s.hacker_id and ch.submission_date like      @remaining_date
    where s.submission_date like @subdate;
    
    set @remaining_date = dateadd(day,1,@remaining_date);
end;

insert into @counted_hackers --inserting counted hackers from @consistent_hackers table 
select count(distinct hacker_id), submission_date from @consistent_hackers
group by submission_date;

--from 37 to 46 line code is for third and fourth columns of output 
with maxed_hacker as(  
select 
    row_number()over(partition by submission_date order by count(s.hacker_id) desc, s.hacker_id asc) as row# , 
    submission_date,
    s.hacker_id,
    h.name
from Submissions as s 
inner join Hackers as h on h.hacker_id=s.hacker_id
group by submission_date,s.hacker_id,h.name
)

select --final select 
    s.submission_date,
    ch.counted,
    mh.hacker_id,
    mh.name
from submissions as s
inner join maxed_hacker as mh on mh.submission_date=s.submission_date 
and row# = 1   -- to get maxed hacker info 
inner join @counted_hackers as ch on ch.submission_date=s.submission_date
group by s.submission_date, mh.hacker_id, mh.name, ch.counted
order by s.submission_date