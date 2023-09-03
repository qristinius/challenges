/*
first part of the code creates subquery named 'student_challenges' where we pick hacker id , name and
count of how many challenges each hacker has done
*/

/*
the second part of the code checks how many challenges done is max challenge
*/

/*
the third part of the code queries total challenges and how many times that number of challenge was done for 
ex: how many students did 1 challenge or 2 challenges or 3 etc... 
*/

/*
the fourth part of the code finally excecutes all of three together and queries hacker id, name and total challenges 
they did, but the ones that are less then max totall challenges and aren't unique (this means only unique students that did
less than max challnge is included in result) are excluded
*/
WITH student_challenges(hacker_id, name, total_challenges) AS (
    SELECT 
        h.hacker_id hacker_id,
        h.name name,
        COUNT(c.challenge_id) total_challenges
    FROM Hackers h 
    JOIN Challenges c 
    ON h.hacker_id=c.hacker_id
    GROUP BY h.hacker_id, h.name
),

max_challenge(max_count) AS (
    SELECT MAX(total_challenges) max_count FROM student_challenges
),
unapproved_challenges( total_challenges, no_of_hackers ) AS (
    SELECT 
        total_challenges,
        COUNT(total_challenges) no_of_hackers
    FROM student_challenges
    GROUP BY total_challenges
)

select hacker_id, name, total_challenges from student_challenges
where total_challenges IN (SELECT max_count FROM max_challenge) 
or total_challenges not in (select total_challenges from unapproved_challenges where no_of_hackers>1)
ORDER BY total_challenges DESC, hacker_id;



