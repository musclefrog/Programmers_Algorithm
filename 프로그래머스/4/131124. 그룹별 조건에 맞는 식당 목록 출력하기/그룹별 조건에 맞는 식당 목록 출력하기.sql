with review as (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by count(*) desc
    limit 1
)

select MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW r
join MEMBER_PROFILE m
on r.MEMBER_ID = m.MEMBER_ID
where r.MEMBER_ID = (select MEMBER_ID from review)
order by REVIEW_DATE, REVIEW_TEXT