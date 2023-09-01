select format(round(s.lat_n, 4),'0.0000') from station as s
where (select count(lat_n) from station where lat_n < s.lat_n )=
(select count(Lat_N) from station where Lat_N > S.LAT_N);