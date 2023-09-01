select case when grade > 7 then name else null end, grade, marks
from students, grades
where marks between min_mark and max_mark
order by grade desc, name, marks ;