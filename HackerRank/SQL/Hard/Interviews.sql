with total_sub as (
select 
        coll.contest_id as contest_id,
        sum(substat.total_submissions) as tot_sub,
        sum(substat.total_accepted_submissions) as tas
    
from Colleges as coll
inner join Challenges as chall on chall.college_id=coll.college_id
inner join Submission_Stats as substat on chall.challenge_id=substat.challenge_id
group by contest_id
    ),

total_view as (

    select
            coll.contest_id,
            sum(vstat.total_views) as tviews,
            sum(vstat.total_unique_views) as tuviews
from        Colleges coll
inner join  Challenges chall on chall.college_id = coll.college_id
inner join  View_Stats vstat   on chall.challenge_id = vstat.challenge_id
group by    coll.contest_id

)

    
select  cont.contest_id, 
        cont.hacker_id,
        cont.name,
        ts.tot_sub,
        ts.tas,
        tv.tviews,
        tv.tuviews
from Contests as cont
inner join total_sub as ts on ts.contest_id=cont.contest_id
inner join total_view as tv on tv.contest_id=cont.contest_id

where ts.tot_sub > 0 
or ts.tas > 0
or tv.tviews > 0
or tv.tuviews > 0

order by cont.contest_id
