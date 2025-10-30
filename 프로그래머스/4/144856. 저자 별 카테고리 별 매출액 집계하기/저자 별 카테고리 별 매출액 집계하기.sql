with total_sales as (
    select b.AUTHOR_ID, b.CATEGORY, (s.SALES * b.PRICE) as TOTAL_SALES
    from BOOK b join (
        select BOOK_ID, sum(SALES) as SALES
        from BOOK_SALES
        where DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-01'
        group by BOOK_ID
    ) s
    on b.BOOK_ID = s.BOOK_ID
)

select t.AUTHOR_ID, a.AUTHOR_NAME, t.CATEGORY, sum(t.TOTAL_SALES) as TOTAL_SALES
from AUTHOR a join total_sales t
on a.AUTHOR_ID = t.AUTHOR_ID
group by t.AUTHOR_ID, a.AUTHOR_NAME, t.CATEGORY
order by t.AUTHOR_ID asc, t.CATEGORY desc;