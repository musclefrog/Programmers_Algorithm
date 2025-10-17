select ID,
case
    when SIZE_RANK = 1 then 'CRITICAL'
    when SIZE_RANK = 2 then 'HIGH'
    when SIZE_RANK = 3 then 'MEDIUM'
    when SIZE_RANK = 4 then 'LOW'
    else 'UNKNOWN'
end as COLONY_NAME
from (select ID, SIZE_OF_COLONY, NTILE(4) over (order by SIZE_OF_COLONY desc) SIZE_RANK
    from ECOLI_DATA) as RANKEDCOLONY
order by ID