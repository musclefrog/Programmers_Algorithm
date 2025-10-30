with users as (
    select WRITER_ID, sum(PRICE) as TOTAL_SALES
    from USED_GOODS_BOARD
    where STATUS = "DONE"
    group by WRITER_ID
    having sum(PRICE) >= 700000
)

select a.USER_ID, a.NICKNAME, b.TOTAL_SALES
from USED_GOODS_USER a join users b
on a.USER_ID = b.WRITER_ID
order by TOTAL_SALES