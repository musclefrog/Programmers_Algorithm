with CODE_SUM as (
    select
        (select sum(CODE) from SKILLCODES where CATEGORY = 'Front End') as FRONT_END,
        (select sum(CODE) from SKILLCODES where NAME = 'Python') as PYTHON,
        (select sum(CODE) from SKILLCODES where NAME = 'C#') as CSHARP
),
CTE as (
    select
        case
            when SKILL_CODE & c.FRONT_END > 0 and SKILL_CODE & c.PYTHON > 0 then 'A'
            when SKILL_CODE & c.CSHARP > 0 then 'B'
            when SKILL_CODE & c.FRONT_END > 0 then 'C'
        end as GRADE,
        ID, EMAIL
    from DEVELOPERS, CODE_SUM c
)
select *
from CTE
where GRADE is not null
order by GRADE, ID;