select F1.X, F1.Y from Functions as F1 
join Functions as F2 on F1.X=F2.Y and F1.Y=F2.X
group by F1.X,F1.Y
having count(F1.X)>1 or F1.X<F1.Y
order by F1.X ASC;