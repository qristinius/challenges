select 
 ceiling(avg(cast(salary as decimal))- avg((cast(replace(salary, "0", "") as decimal))))
from employees;