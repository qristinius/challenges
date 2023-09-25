select w.id, wp.age , w.coins_needed, w.power from wands as w
inner join wands_property as wp on w.code=wp.code
where wp.is_evil=0 and w.coins_needed=
(select min(coins_needed)
from wands as x 
inner join wands_property as y on (x.code=y.code)
where x.power = w.power AND y.age = wp.age
)
order by w.power desc, wp.age desc;