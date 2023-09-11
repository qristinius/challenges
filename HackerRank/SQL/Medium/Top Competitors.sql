select h.hacker_id,h.name from submissions as s 
inner join challenges as c on s.challenge_id=c.challenge_id
inner join difficulty as d on c.difficulty_level=d.difficulty_level
inner join hackers as h on s.hacker_id=h.hacker_id
where s.score=d.score
group by h.hacker_id,h.name
having count(h.hacker_id)>1
order by count(h.hacker_id) desc,h.hacker_id asc; 