with TOTAL as (
    select distinct USER_ID
    from USER_INFO
    where year(JOINED) = '2021'
)

select year(SALES_DATE) as 'YEAR',
        month(SALES_DATE) as 'MONTH',
        count(distinct USER_ID) as PURCHASED_USERS,
        round(count(distinct USER_ID) / (select count(*) from TOTAL), 1) as PURCHASED_RATIO
from ONLINE_SALE
where USER_ID in (
    select *
    from TOTAL
)
group by year(SALES_DATE), month(SALES_DATE)
order by year asc, month asc;