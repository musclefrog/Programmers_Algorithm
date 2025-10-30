with gen2 as (
    select ID
    from ECOLI_DATA
    where PARENT_ID in (select ID
                        from ECOLI_DATA
                        where PARENT_ID IS NULL)
)

select ID
from ECOLI_DATA
where PARENT_ID in (select ID from gen2)