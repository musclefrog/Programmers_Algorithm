select YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, i.GENDER, count(distinct s.USER_ID) as USERS
from USER_INFO i join ONLINE_SALE s
on i.USER_ID = s.USER_ID
where i.GENDER is not null
group by YEAR, MONTH, GENDER
order by YEAR, MONTH, GENDER;