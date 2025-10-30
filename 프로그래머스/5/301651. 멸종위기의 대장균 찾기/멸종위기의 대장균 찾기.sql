with RECURSIVE PARENT as (
    select ID, PARENT_ID, 0 DEPTH
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all
    
    select ED.ID, ED.PARENT_ID, P.DEPTH + 1 DEPTH
    from PARENT P
    left outer join ECOLI_DATA ED
    on P.ID = ED.PARENT_ID
    where P.ID is not null
)
select count(1) as COUNT, DEPTH GENERATION
from PARENT
where ID is null
group by ID, DEPTH
order by DEPTH