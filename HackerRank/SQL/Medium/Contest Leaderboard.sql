with 
max_score as(
select max(score) as mscore, challenge_id, hacker_id from submissions
group by challenge_id,hacker_id )

select h.hacker_id , h.name, sum(msc.mscore)
from hackers as h 
inner join max_score as msc on h.hacker_id = msc.hacker_id
group by h.hacker_id, h.name
having sum(msc.mscore) != 0
order by sum(msc.mscore) desc, hacker_id asc;